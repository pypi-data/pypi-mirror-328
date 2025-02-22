"""
An element produces blocks of content to display in the status bar.

When the status bar is running, every configured element will be prompted for
updates at the configured interval. Once every element has replied with their
output, it's all encoded and sent to swaybar via stdout.

Elements can produce zero or more blocks at each update.
"""

import os
from types import MethodType
from typing import Any, Callable

from .logging import logger
from .subprocess import PopenStreamHandler, StreamHandler

type Seconds = float
type Block = dict[str, Any]
type Output = list[Block]
type PointerButton = int
type ClickEvent = dict[str, Any]
type ClickHandler = str | list[str] | Callable[[ClickEvent], None]


class BaseElement:
    """
    This base class should be subclassed in a swaystatus module package, i.e.
    the `modules` package in the configuration directory or a python package
    with a `swaystatus:modules` entry point. The subclass should be named
    `Element` and be contained in a file named according to how its
    corresponding block should be named.

    For example, if there is a file named `clock.py` in the modules package, an
    instance of the element class would have `self.name` set to "clock".

    The module file could have the following code:

        from swaystatus.element import BaseElement
        from time import strftime

        class Element(BaseElement):
            def on_update(self, output):
                output.append(self.create_block(strftime("%c")))

    Enable the module by adding it to the configuration:

        order = ["clock"]

        # You could also add a click handler:
        [settings.clock]
        on_click.1 = "foot --hold cal"

    All this would need to be put in the configuration directory:

        $XDG_CONFIG_HOME/swaystatus/
        ├── config.toml      # <= configuration goes here
        └── modules/
            ├── __init__.py  # <= necessary, to tell python this is a package
            └── clock.py     # <= module goes here
    """

    name: str | None
    instance: str | None
    env: dict

    def __init__(
        self,
        name: str | None = None,
        instance: str | None = None,
        env: dict | None = None,
        on_click: dict[PointerButton, ClickHandler] | None = None,
    ) -> None:
        """
        Intialize a new status bar content producer.

        If the status bar is configured for click events, then `name` and,
        optionally, `instance` should be set, as they will uniquely identify
        the block that was clicked.

        In order for click events to be useful, handlers for the relevant
        pointer buttons should be defined.

        Ultimately, there should be a method defined in this class named like
        `on_click_<button>` where `<button>` is the pointer button number.

        These methods can be defined explicitly in the element class. This way
        offers the most flexibility and the least hand-holding. They can also
        be defined at runtime by passing a callable to the initializer in the
        `on_click` keyword argument:

            def my_function(event):
                print(f"Got event: {event!r}")

            Element(on_click={1: my_function})

        The `on_click` argument also accepts handlers as a shell command,
        similar to what `subprocess.run` would accept:

            Element(on_click={1: 'foot top', 2: ['foot', '--hold', 'free']})

        If this form is used, the commands are executed in a shell context,
        with all the superpowers that implies, as well as logging stdout and
        stderr to the root logger. This type of handler can also be defined in
        the configuration file, and will be passed to the element class
        automatically.

        Additionally, if the `env` keyword argument is given, it will be added
        to the environment visible to these handlers. It should be a dictionary
        defining any environment variables that should be set when running
        shell command click handlers.

        Building on the earlier example, configurability can be added to the
        clock module by adding an initialization method to the class:

            def __init__(self, *args, full_text=None, **kwargs):
                super().__init__(*args, **kwargs)
                self._full_text = full_text or "%c"

        The update method would need to be changed, as well:

            def on_update(self, output):
                full_text = strftime(self._full_text)
                output.append(self.create_block(full_text))

        This alone will behave exactly as it did before, but it can also be
        configured. For example, you might add this to the module's settings in
        the configuration file:

            [settings.clock]
            ...
            full_text = "The time is now: %r"
        """
        super().__init__()
        self.name = name
        self.instance = instance
        self.env = env or {}
        if on_click:
            for button, handler in on_click.items():
                self._set_on_click_handler(button, handler)

    def __str__(self) -> str:
        return self.key() or super().__str__()

    def _set_on_click_handler(self, button: int, handler: ClickHandler):
        if callable(handler):

            def method(self, event: dict):
                logger.info(f"Executing module {self} handler (button {button}, function)")
                return handler(event)

        else:

            def method(self, event: dict):
                env = os.environ.copy()
                env.update(self.env)
                env.update({key: str(value if value is not None else "") for key, value in event.items()})

                def create_log_handler(log: StreamHandler):
                    def handler(line: str):
                        log(f"Output from module {self} button {button} handler: {line.strip()}")

                    return handler

                stdout = create_log_handler(logger.debug)
                stderr = create_log_handler(logger.error)

                logger.info(f"Executing module {self} handler (button {button}, shell)")
                return PopenStreamHandler(stdout, stderr, handler, shell=True, text=True, env=env)

        setattr(self, f"on_click_{button}", MethodType(method, self))
        logger.debug(f"Module {self} set click handler for button {button}: {handler}")

    def key(self) -> str | None:
        """Return a string uniquely identifying this element."""
        if self.name and self.instance:
            return f"{self.name}:{self.instance}"
        if self.name:
            return self.name
        return None

    def create_block(self, full_text: str, **params) -> Block:
        """
        Helper for creating a block of content for output to the status bar.

        If `self.name` or `self.instance` are set, they will be included
        automatically.

        The only required parameter is `full_text` as it's the only required
        field for a viable content block.

        Any extra keyword arguments are set directly in the block.
        """
        block = {"full_text": full_text}
        if self.name:
            block["name"] = self.name
        if self.instance:
            block["instance"] = self.instance
        block.update(params)
        return block

    def on_update(self, output: Output):
        """
        Perform some action on every update loop iteration.

        For anything to appear on the status bar, a block should be added to
        `output` in this method. For a description of blocks, see the "BODY"
        section of swaybar-protocol(7).

        There are no requirements for the presence or absence of a block nor
        how many are added.

        It's recommended to use `self.create_block` to create the blocks:

            output.append(self.create_block("hello, world"))

        But they can also be added directly:

            output.append({"full_text": "hello, world"})
        """
        pass

    def on_click(self, event: ClickEvent):
        """
        Perform some action when a status bar block is clicked.

        If `click_events` is set to `True` in the configuration and `self.name`
        (and possibly `self.instance`) is set, any time the user clicks a
        block, this method will be called on the element that produced it and
        passed an event object describing the click. For a description of click
        events, see the "CLICK EVENTS" section of swaybar-protocol(7).

        If blocks are created using `self.create_block`, the name and instance
        keys will be set automatically in the block.

        This method can be overridden to provide direct control on how click
        events should be handled, but, by default, will delegate the events to
        other methods, e.g. `self.on_click_<button>` where `<button>` is the
        pointer device button number.
        """
        try:
            return getattr(self, f"on_click_{event['button']}")(event)
        except AttributeError:
            pass
