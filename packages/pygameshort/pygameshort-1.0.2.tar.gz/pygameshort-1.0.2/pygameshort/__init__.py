"""
A UI extention onto the already existing library called "pygame", 
it also allows for easy multi-networking with the "secure_network" 
library that's also made by me. 

Parts of the code may not be as professional as I'd like as there 
is a huge time gap between different systematic schemes and also, 
there has been a lot of debugging and work to make this function.
"""

import secure_network
import pygame
import time
import base64
import pyperclip
from dataclasses import dataclass
from collections.abc import Iterable
from typing import Union, Callable, Any, Generator, Optional, overload
# We'll define ReadableBuffer as a 'Any' for now.

pygame.init()

SCREEN_SIZE: tuple[int, int] = (800, 600)

EventType = Union[pygame.event.EventType, secure_network.EventType]
Event = Union[pygame.event.Event, secure_network.Event]
ConnType = Union[secure_network.SERVER, secure_network.CLIENT]

class Key:
    def __init__(self, key: Optional[bytes] = None):
        self.key: bytes = key if key else Key.generate_key()

    def extract(self) -> tuple[bytes, bytes]:
        fernet_key, hmac_key = Key.deinterleave_keys(self.key)
        fernet_key = base64.urlsafe_b64encode(fernet_key)
        return fernet_key, hmac_key
    
    @staticmethod
    def generate_key() -> bytes:
        fernet_key = secure_network.generate_key()
        hmac_key = secure_network.generate_hmac_key()
        return Key.interleave_keys(fernet_key, hmac_key)
    
    @staticmethod
    def interleave_keys(fernet_key: bytes, hmac_key: bytes) -> bytes:
        return bytes(a for pair in zip(fernet_key, hmac_key) for a in pair)
    
    @staticmethod
    def deinterleave_keys(combined_key: bytes) -> tuple[bytes, bytes]:
        fernet_key = combined_key[0::2]  # Extract every even byte (starting at 0)
        hmac_key = combined_key[1::2]    # Extract every odd byte (starting at 1)
        return fernet_key, hmac_key

class Connection:
    """
    Manages secure network connections using the secure_network library.

    Provides a simplified interface for establishing and managing encrypted
    network connections, handling authentication, and message passing.

    Attributes:
        conn (ConnType): The underlying network connection (SERVER or CLIENT)
        ip (str): Server IP address
        port (int): Server port number
        type (ConnType): Connection type (SERVER or CLIENT)
        on_event (Callable[[secure_network.Event], Any]): Event callback function

    Args:
        key (bytes): Encryption key for secure communication
        hmac_key (bytes): HMAC key for message authentication
        ip (str): Server IP address
        port (int): Server port number
        type (ConnType): Connection type (SERVER or CLIENT)
        on_event (Callable[[secure_network.Event], Any]): Event callback function
        *args: Additional arguments passed to the connection
        **kwargs: Additional keyword arguments passed to the connection
    """
    def __init__(self, key: bytes, hmac_key: bytes, ip: str, port: int, type: ConnType, on_event: Callable[[secure_network.Event], Any] = (lambda event: None), *args, **kwargs):
        self.conn: ConnType = type(key, hmac_key, (ip, port), on_event, *args, **kwargs)
        self.ip: str = ip
        self.port: int = port
        self.type: ConnType = type
        self.on_event: Callable[[secure_network.Event], Any] = on_event

        self.init: Callable[[], None] = self.conn.init
    
    def set_address(self, ip: str, port: int) -> None:
        """
        Update the connection address.

        Args:
            ip (str): New server IP address
            port (int): New server port number
        """
        self.conn.address = (ip, port)
    
    def auth(self, username: str, password: str) -> None:
        """
        Authenticate with the server (client-side only).

        Args:
            username (str): Authentication username
            password (str): Authentication password

        Raises:
            RuntimeError: If called on a server connection
        """
        if self.type == secure_network.CLIENT: self.conn.auth(username, password)
        else: raise RuntimeError("Cannot auth on a server connection.")
    
    def send(self, data: Any, /) -> None:
        self.conn.send(data)
    
    def close(self) -> None:
        self.conn.close()

class CursorHandler:
    def __init__(self): 
        self.last_id: Any = None
    
    def set_cursor(self, id: Any, cursor: int) -> None:
        if not id == self.last_id:
            pygame.mouse.set_cursor(cursor)
            self.last_id = id
    
    def reset(self, id: Any) -> None:
        if id == self.last_id:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.last_id = None

_window: 'Window' = None

class Window:
    """
    A central window class that manages all UI resources and rendering.

    The Window class serves as the main container for the UI system, handling:
    - Event management and distribution
    - Scene rendering and display
    - Network connection management
    - Frame rate control and timing
    - Resource management for UI components

    Attributes:
        screen (pygame.Surface): The main display surface
        clock (pygame.time.Clock): Clock for controlling frame rate
        running (bool): Flag indicating if the window is running
        delta_time (float): Time elapsed since last frame
        fps (float): Current frames per second
        cursor_handler (CursorHandler): Manages cursor states
        scroll_speed (int): Pixels per scroll event
        scroll (int): Current scroll position
        on_render (list[Callable[[], Any]]): Render callback functions
        event_parser (EventParser): Handles event distribution
        conn (Connection): Optional network connection

    Args:
        title (str): Window title to display
        connection (Connection): Network connection handler
        on_render (Callable[[], Any]): Main render callback function
        *args: Additional arguments passed to pygame.display.set_mode
        **kwargs: Additional keyword arguments passed to pygame.display.set_mode
    """
    class EventParser:
        """
        This event parser helps parsing both pygame events and network events to 
        registered callbacks that have their own tickets for specific event types.
        """
        class Ticket:
            def __init__(self, event_type: EventType, callback: Callable[[Event], Any]):
                self.event_type: EventType = event_type
                self.callback: Callable[[Event], Any] = callback
            
            def check(self, event: Event) -> None:
                if self.event_type == event.type: 
                    self.callback(event)
        
        class MultiTicket(Ticket):
            def __init__(self, event_types: list[EventType], callback: Callable[[Event], Any]):
                self.event_type: list[EventType] = event_types
                self.callback: Callable[[Event], Any] = callback
            
            def check(self, event: Event) -> None:
                if any(event_type == event.type for event_type in self.event_type):
                    self.callback(event)

        def __init__(self, tickets: list[Ticket] = []):
            self.tickets: list[Window.EventParser.Ticket] = tickets
            self.on_all: list[Callable[[Event], Any]] = []
        
        def append(self, ticket: Ticket, /) -> None:
            self.tickets.append(ticket)
        
        def remove(self, ticket: Ticket, /) -> None:
            self.tickets.remove(ticket)
        
        def pop(self, index: int = -1, /) -> None:
            self.tickets.pop(index)
        
        def __getitem__(self, key: int) -> Union['Window.EventParser.Ticket', None]:
            return self.tickets[key]
        
        def __setitem__(self, key: int, value: Ticket) -> None:
            self.tickets[key] = value
        
        def __iter__(self) -> iter: return iter(self.tickets)

        def __len__(self) -> int: return len(self.tickets)

        def parse(self, event: Event) -> None:
            for ticket in self.tickets:
                ticket.check(event)
                for callback in self.on_all: 
                    callback(event)

    def __init__(self, title: str, connection: Connection, on_render: Callable[[], Any], /, *args, **kwargs):
        self.screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE, *args, **kwargs)
        pygame.display.set_caption(title)

        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.running: bool = False
        self.delta_time: float = 0
        self.fps: float = 0

        self.cursor_handler: CursorHandler = CursorHandler()
        self.scroll_speed: int = 20
        self.scroll: int = 0

        self.on_render: list[Callable[[], Any]] = [on_render]
        self.event_parser: Window.EventParser = Window.EventParser()
        self.event_parser.append(Window.EventParser.Ticket(
            pygame.MOUSEWHEEL,
            self._on_scroll
        ))
        self.event_parser.append(Window.EventParser.Ticket(
            pygame.QUIT,
            self.quit
        ))

        if connection:
            self.conn: Connection = connection
            self.conn.on_event = self.event_parser.parse
        else: self.conn = None
        
        global _window
        if _window: _window.quit()
        _window = self
    
    def _on_scroll(self, event: Event) -> None:
        self.scroll += event.y * self.scroll_speed
    
    def set_address(self, ip: str, port: int) -> None:
        """Set the connection address."""
        if self.conn: self.conn.set_address(ip, port)
    
    def connect(self) -> None: 
        """Start the connection."""
        if self.conn: self.conn.init() # Start the connection in the background

    def run(self, framerate: int = 60) -> None: 
        """Start running the window - the function returns as the window closes."""
        self.running = True
        try:
            while self.running:
                self.delta_time = self.clock.tick(framerate)
                self.fps = self.clock.get_fps()
                for event in pygame.event.get(): 
                    self.event_parser.parse(event)
                for callback in self.on_render: callback()
                pygame.display.flip()
        finally:
            self.running = False # Ensures the attributes consistency over errors.
    
    def quit(self, *args) -> None:
        """Quit the window."""
        self.running = False
        self.conn.close()

class Cooldown:
    """
    Helps with cooldown operations - almost always neccissary.
    """
    def __init__(self, cooldown: float): 
        self.cooldown: float = cooldown
        self._last_time: float | None = None
    
    def check(self) -> None:
        current_time = time.time()
        if self._last_time is None or current_time - self._last_time >= self.cooldown:
            self._last_time = current_time
            return True
        return False
    
    def reset(self) -> None:
        self._last_time = None

class Matrix: 
    """A matrix that can be applicated in metrical value attribution."""

@dataclass
class Pos(Matrix):
    """A postitional metrical value."""
    x: int = 0
    y: int = 0

    def __getitem__(self, key: int | str) -> int:
        return {0: self.x, 1: self.y, "x": self.x, "y": self.y}[key]
    
    def __setitem__(self, key: int | str, value: int) -> None:
        if isinstance(key, int): 
            key = {0: "x", 1: "y"}[key] # either x or y
        setattr(self, key, value)
    
    def copy(self) -> 'Pos': 
        return Pos(self.x, self.y)
    
    def __iter__(self) -> iter: return iter((self.x, self.y))

@dataclass
class Size(Matrix):
    """A areal metrical value."""
    width: int = 0
    height: int = 0

    def __getitem__(self, key: int | str) -> int:
        return {0: self.width, 1: self.height, "width": self.width, "height": self.height}[key]
    
    def __setitem__(self, key: int | str, value: int) -> None:
        if isinstance(key, int): 
            key = {0: "width", 1: "height"}[key] # either width or height
        setattr(self, key, value)
    
    def copy(self) -> 'Size': 
        return Size(self.width, self.height)
    
    def __iter__(self) -> iter: return iter((self.width, self.height))

@dataclass
class ColorData:
    """
    A set of colors.
    """
    background: pygame.Color
    border: pygame.Color

    foreground: Optional[pygame.Color] = None
    primary: Optional[pygame.Color] = None
    secondary: Optional[pygame.Color] = None

    @classmethod
    def create_light_theme(cls) -> 'ColorData':
        """Get a light theme color data set."""
        return cls(
            background=pygame.Color(255, 255, 255),
            border=pygame.Color(200, 200, 200),
            foreground=pygame.Color(0, 0, 0),
            primary=pygame.Color(0, 120, 255),
            secondary=pygame.Color(100, 100, 100)
        )
    
    @classmethod
    def create_dark_theme(cls) -> 'ColorData':
        """Get a dark theme color data set."""
        return cls(
            background=pygame.Color(50, 50, 50),
            border=pygame.Color(100, 100, 120),
            foreground=pygame.Color(0, 0, 0),
            primary=pygame.Color(200, 220, 255),
            secondary=pygame.Color(200, 200, 200)
        )

@dataclass
class FontSet:
    """
    A font set - it has different sizes of a font.
    """
    small: Optional[pygame.font.Font] = None
    medium: Optional[pygame.font.Font] = None
    large: Optional[pygame.font.Font] = None

    def load_system_font(self, name: str | bytes | Iterable[str | bytes] | None, sizes: tuple[int, int, int]) -> 'FontSet':
        """Load font by name from system."""
        self.small = pygame.font.SysFont(name, sizes[0])
        self.medium = pygame.font.SysFont(name, sizes[1])
        self.large = pygame.font.SysFont(name, sizes[2])
        return self
    
    def load_font(self, name: str, sizes: tuple[int, int, int]) -> 'FontSet':
        """Load font by path to a font-file."""
        self.small = pygame.font.Font(name, sizes[0])
        self.medium = pygame.font.Font(name, sizes[1])
        self.large = pygame.font.Font(name, sizes[2])
        return self

@dataclass
class FontData:
    """
    A set for different fonts for different scenarios.
    """
    titles: Optional[FontSet] = None
    primary: Optional[FontSet] = None
    secondary: Optional[FontSet] = None

class Box(Pos, Size):
    """A box. It simplifies mobility over metrical values in one entity."""
    
    @overload
    def __init__(self, pos: Pos, size: Size): ...

    @overload
    def __init__(self, x: int, y: int, width: int, height: int): ...

    def __init__(self, *args):
        if len(args) == 2 and isinstance(args[0], Pos) and isinstance(args[1], Size):
            pos, size = args
            Pos.__init__(self, pos.x, pos.y)  # Call Pos.__init__
            Size.__init__(self, size.width, size.height)  # Explicitly call Size.__init__
        
        elif len(args) == 4 and all(isinstance(arg, int) for arg in args):
            x, y, width, height = args
            Pos.__init__(self, x, y)  # Call Pos.__init__
            Size.__init__(self, width, height)  # Explicitly call Size.__init__
        
        else:
            raise TypeError("Invalid arguments for Rect initialization.")
    
    def copy(self) -> 'Box':
        return Box(self.x, self.y, self.width, self.height)

    @property
    def pos(self) -> Pos:
        return Pos(self.x, self.y)
    
    @property
    def size(self) -> Size:
        return Size(self.width, self.height)

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def get_rect(self, offset_pos: tuple[int, int] = (0, 0), offset_size: tuple[int, int] = (0, 0)) -> pygame.Rect:
        return pygame.Rect(self.x + offset_pos[0], self.y + offset_pos[1], self.width + offset_size[0], self.height + offset_size[1])

class Object(pygame.Surface):
    """
    Base class for all UI components in the pygameplus library.

    The Object class serves as the foundation for building interactive UI elements,
    providing core functionality for rendering, event handling, and state management.
    All custom UI components should inherit from this class.

    Key Features:
        - Automatic event handling and distribution
        - Frame-based updates and rendering
        - State tracking for drawing and interactions
        - Integration with window management
        - Position and size management via Box system
        - Consistent styling through ColorData and FontSet

    Attributes:
        window (Window): Reference to the parent window
        box (Box): Position and dimensions of the object
        color (ColorData): Color scheme for the object
        font (FontSet): Font configuration for text rendering
        drawn (bool): Whether the object was drawn in the current frame
        was_drawn (bool): Whether the object was drawn in the previous frame

    Args:
        box (Box): Position and size configuration
        color (ColorData): Color scheme for the object
        font (FontSet): Font configuration
        events (list[EventType]): List of event types this object should handle

    Implementation Requirements:
        1. Event Handling:
           - Override `on_event(self, event: Event) -> None`
           - Will receive events of types specified in constructor
           - Events are automatically filtered and distributed

        2. Update Cycle:
           - Override `update(self) -> None`
           - Called every frame
           - Must call super().update() FIRST
           - Use for continuous state updates (e.g., cursor management)

        3. Drawing:
           - Override `draw(self, offset: tuple[int, int] = (0, 0)) -> None`
           - Called when object should be rendered
           - Must call super().draw(offset) LAST
           - Offset parameter handles scrolling and positioning

    Example:
        ```python
        class CustomButton(Object):
            def __init__(self, box: Box, color: ColorData, font: FontSet):
                super().__init__(
                    box,
                    color,
                    font,
                    [pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION]
                )
                self.hover = False

            def update(self) -> None:
                super().update()  # Call first
                if self.drawn and self.hover:
                    self.window.cursor_handler.set_cursor(
                        self, 
                        pygame.SYSTEM_CURSOR_HAND
                    )

            def on_event(self, event: Event) -> None:
                if event.type == pygame.MOUSEMOTION:
                    self.hover = self.box.rect.collidepoint(*event.pos)

            def draw(self, offset: tuple[int, int] = (0, 0)) -> None:
                # Render custom graphics
                pygame.draw.rect(self, self.color.background, self.rect)
                super().draw(offset)  # Call last
        ```

    Notes:
        - The `drawn` attribute should be used for state management rather than
          `was_drawn`, as it represents the current frame's state
        - Event handlers are automatically registered with the window's event parser
        - The object's surface is automatically created with SRCALPHA for
          transparency support
        - The window reference is automatically set during initialization
    """
    def __init__(self, box: Box, color: ColorData, font: FontSet, events: list[EventType]):
        pygame.Surface.__init__(self, tuple(box.size), pygame.SRCALPHA)
        self.window: Window = _window
        self.window.on_render.append(self.update)
        self.window.event_parser.append(Window.EventParser.MultiTicket(events, self.on_event))
        self.box: Box = box
        self.color: ColorData = color
        self.font: FontSet = font
        self.drawn: bool = False
        self.was_drawn: bool = False
    
    def update(self) -> Any: 
        if self.was_drawn == True:
            self.was_drawn = False
            self.drawn = True
        else: self.drawn = False
    
    @overload
    def on_event(self, event: Event) -> Any: ...

    def draw(self, offset: tuple[int, int] = (0, 0)) -> None: 
        self.was_drawn = True
        self.window.screen.blit(self, (self.box.x + offset[0], self.box.y + offset[1]))

class Scene:
    def __init__(self, objects: list[Object] = []):
        if not isinstance(objects, list): objects = [objects]
        self.objects: list[Object] = objects
        self.window: Window = _window
    
    def draw(self):
        for object in self.objects: object.draw((0, -self.window.scroll))

def calculate_derivative_size(
    used_width: float, used_height: float, 
    original_width: float, original_height: float, 
    target_scale_offset: float, smoothing: float, snapping_threshold: float
) -> tuple[float, float]:
    """
    Calculate smooth size transitions for UI elements.

    This function implements a smooth resizing algorithm that maintains aspect ratio
    and provides smooth transitions between sizes with optional snapping.

    Args:
        used_width (float): Current width of the element
        used_height (float): Current height of the element
        original_width (float): Original width of the element
        original_height (float): Original height of the element
        target_scale_offset (float): Desired scale change from original size
        smoothing (float): Smoothing factor (0-1), higher values = smoother
        snapping_threshold (float): Distance threshold for snapping to target size

    Returns:
        tuple[float, float]: Width and height changes to apply
            - First value is the width change
            - Second value is the height change

    Example:
        >>> # Calculate size changes for a button growing on hover
        >>> dw, dh = calculate_derivative_size(
        ...     100, 50,  # Current size
        ...     100, 50,  # Original size
        ...     10,       # Grow by 10 units
        ...     0.3,      # Smooth transition
        ...     0.5       # Snap when close
        ... )
    """
    
    current_scale = used_width + used_height
    original_scale = original_width + original_height
    target_scale = original_scale - target_scale_offset

    # Ensure gradual resizing
    scale_factor = target_scale / current_scale
    smooth_factor = 1 - smoothing  # Adjust smoothing behavior

    new_width = (target_scale * (used_width / current_scale) - used_width) * smooth_factor
    new_height = (target_scale * (used_height / current_scale) - used_height) * smooth_factor

    # Check if close enough to snap
    if abs((new_width + new_height) - target_scale) < snapping_threshold:
        return target_scale * (original_width / original_scale), target_scale * (original_height / original_scale)
    
    return new_width, new_height

class Text(pygame.Surface):
    def __init__(self, text: str, font: pygame.font.Font, size: Size, 
                 antialias: bool = True,
                 font_color: tuple[int, int, int] = (0, 0, 0), 
                 cursor_blink_interval: int = 300,
                 cursor_width: int = 2, 
                 cursor_color: tuple[int, int, int] = (0, 0, 0),
                 max_width: int = 300,
                 max_lines: int = 5) -> None:
        pygame.Surface.__init__(self, tuple(size), pygame.SRCALPHA)
        self.text: str = text
        self.font: pygame.font.Font = font
        self.antialias: bool = antialias
        self.font_color: tuple[int, int, int] = font_color
        self.cursor_blink_interval: int = cursor_blink_interval
        self.cursor_active: bool = False
        self.cursor_pos: int = 0
        self.cursor_width: int = cursor_width
        self.cursor_color: tuple[int, int, int] = cursor_color
        self.active: bool = False
        self.hover: bool = False
        self.editable: bool = True
        self.max_width: int = max_width
        self.max_lines: int = max_lines
        self.lines: list[str] = self._wrap_text(text)
        self.selection_start: int = None
        self.selection_end: int = None
        self.selection_color: tuple[int, int, int, int] = (30, 150, 245, 75)
        self.selection_border_color: tuple[int, int, int, int] = tuple(max(min(color - 20, 255), 0) for color in self.selection_color)
        self.selection_border_color = (self.selection_border_color[0], self.selection_border_color[1], self.selection_border_color[2], self.selection_border_color[3] + 10)
        self.undo_stack: list = []
        self.redo_stack: list = []
        self.last_blink_time: int = pygame.time.get_ticks()
        self.margin: int = 5  # Clicking margin in pixels

    def _wrap_text(self, text: str) -> list[str]:
        """Wrap text into multiple lines based on max_width."""
        lines = []
        current_line = ""

        for char in text:
            if char == '\n':
                lines.append(current_line)
                current_line = ""
                continue
            
            if self.font.size(current_line + char)[0] <= self.max_width:
                current_line += char
            else:
                # Try to break at word boundary
                words = current_line.split()
                if words:
                    lines.append(" ".join(words[:-1]))
                    current_line = words[-1] + char
                else:
                    lines.append(current_line)
                    current_line = char

        if current_line:
            lines.append(current_line)

        return lines[:self.max_lines]

    def _get_total_chars(self) -> int:
        """Get total number of characters including newlines."""
        return sum(len(line) + 1 for line in self.lines[:-1]) + len(self.lines[-1])

    def _get_selected_text(self) -> str:
        """Get currently selected text."""
        if self.selection_start is None or self.selection_end is None:
            return ""
        start = min(self.selection_start, self.selection_end)
        end = max(self.selection_start, self.selection_end)
        return self.text[start:end]

    def draw(self, surface: pygame.Surface, pos: tuple[int, int]) -> None:
        """Render text, cursor, and selection."""
        self.fill((0, 0, 0, 0))
        current_time = pygame.time.get_ticks()

        # Update cursor blink
        if current_time - self.last_blink_time > self.cursor_blink_interval:
            self.cursor_active = not self.cursor_active
            self.last_blink_time = current_time

        # Draw text and selection
        y_offset = 0
        char_count = 0
        for line in self.lines:
            # Draw text
            rendered_line = self.font.render(line, self.antialias, self.font_color)
            self.blit(rendered_line, (0, y_offset))

            # Draw selection highlight if exists
            if self.selection_start is not None and self.selection_end is not None:
                sel_start = min(self.selection_start, self.selection_end)
                sel_end = max(self.selection_start, self.selection_end)

                line_start = char_count
                line_end = char_count + len(line)

                if line_start <= sel_end and line_end >= sel_start:
                    highlight_start = max(0, sel_start - line_start)
                    highlight_end = min(len(line), sel_end - line_start)
                    size = (self.font.size(line[highlight_start:highlight_end])[0], self.font.get_height())
                    highlight_surface = pygame.Surface(
                        size, flags = pygame.SRCALPHA
                    )
                    highlight_surface.fill((0, 0, 0, 0))  # Selection color
                    pygame.draw.rect(highlight_surface, self.selection_color, pygame.Rect(0, 0, *size), 0, 3)
                    pygame.draw.rect(highlight_surface, self.selection_border_color, pygame.Rect(0, 0, *size), 1, 3)
                    self.blit(highlight_surface, (self.font.size(line[:highlight_start])[0], y_offset))

            # Prepare for the next line
            char_count += len(line) + 1  # +1 for newline
            y_offset += self.font.get_linesize()

        # Draw cursor if active and text is selected
        if self.active and self.cursor_active:
            cursor_x, cursor_y = self._calculate_cursor_position()
            pygame.draw.rect(self, self.cursor_color,
                           (cursor_x, cursor_y, self.cursor_width, self.font.get_height()))

        surface.blit(self, pos)

    def _calculate_cursor_position(self) -> tuple[int, int]:
        """Calculate the pixel position of the cursor."""
        x, y = 0, 0
        char_index = self.cursor_pos
        for line_index, line in enumerate(self.lines):
            if char_index <= len(line):  # Cursor is within this line
                x = self.font.size(line[:char_index])[0]
                y = line_index * self.font.get_linesize()
                break
            char_index -= len(line) + 1  # Move to next line (include newline character)
        return x, y

    def parse_event(self, event: pygame.event.Event, box: Box) -> None:
        """Handle events for text editing and interaction."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                if box.rect.collidepoint(event.pos):
                    self.active = True
                    self.cursor_pos = self._get_char_index_from_pos(event.pos, box)
                    self.selection_start = self.cursor_pos
                    self.selection_end = self.cursor_pos
                else:
                    self.active = False
                    self.selection_start = None
                    self.selection_end = None

        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  # Left button held
                if self.active:
                    self.selection_end = self._get_char_index_from_pos(event.pos, box)
                    self.cursor_pos = self.selection_end

        elif event.type == pygame.KEYDOWN and self.active:
            ctrl_held = pygame.key.get_mods() & pygame.KMOD_CTRL
            shift_held = pygame.key.get_mods() & pygame.KMOD_SHIFT

            # Handle copy operations regardless of editable status
            if ctrl_held:
                if event.key == pygame.K_a:  # Select all
                    self.selection_start = 0
                    self.selection_end = len(self.text)
                    self.cursor_pos = self.selection_end
                elif event.key == pygame.K_c:  # Copy
                    if self.selection_start is not None:
                        pyperclip.copy(self._get_selected_text())
                        return

            # If not editable, only handle navigation keys
            if not self.editable:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_HOME, pygame.K_END):
                    if event.key == pygame.K_LEFT:
                        self._move_cursor_left(shift_held)
                    elif event.key == pygame.K_RIGHT:
                        self._move_cursor_right(shift_held)
                    elif event.key == pygame.K_HOME:
                        self._move_cursor_to_line_start(shift_held)
                    elif event.key == pygame.K_END:
                        self._move_cursor_to_line_end(shift_held)
                return

            # Handle all other editing operations only if editable
            if ctrl_held:
                if event.key == pygame.K_x:  # Cut
                    if self.selection_start is not None:
                        pyperclip.copy(self._get_selected_text())
                        self._delete_selected_text()
                elif event.key == pygame.K_v:  # Paste
                    self._paste_text(pyperclip.paste())
                elif event.key == pygame.K_z:  # Undo
                    self._undo()
                elif event.key == pygame.K_y:  # Redo
                    self._redo()
            else:
                if event.key == pygame.K_LEFT:
                    self._move_cursor_left(shift_held)
                elif event.key == pygame.K_RIGHT:
                    self._move_cursor_right(shift_held)
                elif event.key == pygame.K_HOME:
                    self._move_cursor_to_line_start(shift_held)
                elif event.key == pygame.K_END:
                    self._move_cursor_to_line_end(shift_held)
                elif event.key == pygame.K_BACKSPACE:
                    if self.selection_start != self.selection_end:
                        self._delete_selected_text()
                    elif self.cursor_pos > 0:
                        self._save_undo_state()
                        self.text = self.text[:self.cursor_pos - 1] + self.text[self.cursor_pos:]
                        self.cursor_pos -= 1
                        self.selection_start = self.selection_end = self.cursor_pos
                elif event.key == pygame.K_DELETE:
                    if self.selection_start != self.selection_end:
                        self._delete_selected_text()
                    elif self.cursor_pos < len(self.text):
                        self._save_undo_state()
                        self.text = self.text[:self.cursor_pos] + self.text[self.cursor_pos + 1:]
                        self.selection_start = self.selection_end = self.cursor_pos
                elif event.key == pygame.K_RETURN:
                    if len(self.lines) < self.max_lines:
                        self._save_undo_state()
                        self.text = self.text[:self.cursor_pos] + "\n" + self.text[self.cursor_pos:]
                        self.cursor_pos += 1
                        self.selection_start = self.selection_end = self.cursor_pos
                elif event.unicode and not ctrl_held:
                    self._save_undo_state()
                    if self.selection_start != self.selection_end:
                        self._delete_selected_text()
                    self.text = self.text[:self.cursor_pos] + event.unicode + self.text[self.cursor_pos:]
                    self.cursor_pos += 1
                    self.selection_start = self.selection_end = self.cursor_pos

            self.lines = self._wrap_text(self.text)

    def _get_char_index_from_pos(self, pos: tuple[int, int], box: Box) -> int:
        """Convert mouse position to character index."""
        relative_x = pos[0] - box.rect.x
        relative_y = pos[1] - box.rect.y

        line_index = min(relative_y // self.font.get_linesize(), len(self.lines) - 1)
        if line_index < 0:
            return 0

        line = self.lines[line_index]
        char_index = 0

        # Add characters from previous lines
        for i in range(line_index):
            char_index += len(self.lines[i]) + 1

        # Find position within current line
        accumulated_width = 0
        for i, char in enumerate(line):
            char_width = self.font.size(char)[0]
            if accumulated_width + char_width // 2 >= relative_x:
                return char_index + i
            accumulated_width += char_width

        return char_index + len(line)

    def _move_cursor_left(self, maintain_selection: bool = False) -> None:
        """Move cursor left one character."""
        if self.cursor_pos > 0:
            self.cursor_pos -= 1
            if not maintain_selection:
                self.selection_start = self.selection_end = self.cursor_pos
            else:
                self.selection_end = self.cursor_pos

    def _move_cursor_right(self, maintain_selection: bool = False) -> None:
        """Move cursor right one character."""
        if self.cursor_pos < len(self.text):
            self.cursor_pos += 1
            if not maintain_selection:
                self.selection_start = self.selection_end = self.cursor_pos
            else:
                self.selection_end = self.cursor_pos

    def _move_cursor_to_line_start(self, maintain_selection: bool = False) -> None:
        """Move cursor to start of current line."""
        current_line = 0
        chars_counted = 0

        for i, line in enumerate(self.lines):
            if chars_counted + len(line) >= self.cursor_pos:
                current_line = i
                break
            chars_counted += len(line) + 1

        self.cursor_pos = chars_counted
        if not maintain_selection:
            self.selection_start = self.selection_end = self.cursor_pos
        else:
            self.selection_end = self.cursor_pos

    def _move_cursor_to_line_end(self, maintain_selection: bool =
False) -> None:
        """Move cursor to end of current line."""
        current_line = 0
        chars_counted = 0

        for i, line in enumerate(self.lines):
            if chars_counted + len(line) >= self.cursor_pos:
                current_line = i
                break
            chars_counted += len(line) + 1

        self.cursor_pos = chars_counted + len(self.lines[current_line])
        if not maintain_selection:
            self.selection_start = self.selection_end = self.cursor_pos
        else:
            self.selection_end = self.cursor_pos

    def _delete_selected_text(self) -> None:
        """Delete currently selected text."""
        if self.selection_start is None or self.selection_end is None:
            return

        self._save_undo_state()
        start = min(self.selection_start, self.selection_end)
        end = max(self.selection_start, self.selection_end)
        self.text = self.text[:start] + self.text[end:]
        self.cursor_pos = start
        self.selection_start = self.selection_end = start

    def _paste_text(self, text: str) -> None:
        """Paste text at current cursor position."""
        if not text:
            return

        self._save_undo_state()
        if self.selection_start != self.selection_end:
            self._delete_selected_text()

        self.text = self.text[:self.cursor_pos] + text + self.text[self.cursor_pos:]
        self.cursor_pos += len(text)
        self.selection_start = self.selection_end = self.cursor_pos

    def _save_undo_state(self) -> None:
        """Save current state to undo stack."""
        self.undo_stack.append((self.text, self.cursor_pos, self.selection_start, self.selection_end))
        self.redo_stack.clear()

    def _undo(self) -> None:
        """Undo last text change."""
        if self.undo_stack:
            self.redo_stack.append((self.text, self.cursor_pos, self.selection_start, self.selection_end))
            self.text, self.cursor_pos, self.selection_start, self.selection_end = self.undo_stack.pop()
            self.lines = self._wrap_text(self.text)

    def _redo(self) -> None:
        """Redo last undone text change."""
        if self.redo_stack:
            self.undo_stack.append((self.text, self.cursor_pos, self.selection_start, self.selection_end))
            self.text, self.cursor_pos, self.selection_start, self.selection_end = self.redo_stack.pop()
            self.lines = self._wrap_text(self.text)

class Button(Object):
    """
    An interactive button component with hover, click, and toggle functionality.

    Features:
    - Hover effects with cursor changes
    - Click animations with size changes
    - Optional toggle state
    - Smooth size transitions
    - Customizable appearance

    Attributes:
        callback (Callable[[], Any]): Function called when button is clicked
        hover (bool): Current hover state
        pressed (bool): Current pressed state
        toggled (bool): Current toggle state (if switch=True)
        switch (bool): Whether button acts as a toggle
        border_radius (int): Corner rounding radius
        border_width (int): Border thickness
        smoothing (float): Animation smoothing factor (0-1)
        snapping (float): Size snapping threshold

    Args:
        text (str): Button label text
        box (Box): Position and size
        color (ColorData): Color scheme
        font (FontSet): Font configuration
        border_radius (int): Corner rounding radius
        border_width (int): Border thickness
        switch (bool): Enable toggle functionality
        callback (Callable[[], Any]): Click handler function
    """
    def __init__(self, text: str, box: Box, color: ColorData, font: FontSet, border_radius: int, border_width: int, switch: bool, callback: Callable[[], Any]):
        Object.__init__(self, box, color, font, [pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])
        self.callback: Callable[[], Any] = callback

        self.background_box: Box = self.box.copy()

        self.hover: bool = False
        self.pressed: bool = False
        self.toggled: bool = False

        self.switch: bool = switch

        self.border_radius: int = border_radius
        self.border_width: int = border_width

        self.smoothing: float = 0.35
        self.snapping: float = 0.5

        self.text_surface = font.medium.render(text, True, color.foreground)

    def on_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.box.rect.collidepoint(*event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hover:
            self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.pressed = False
            if self.hover and self.drawn:
                if self.switch: self.toggled = not self.toggled
                self.callback()
    
    def update(self) -> None:
        Object.update(self)
        if self.drawn and self.hover:
            self.window.cursor_handler.set_cursor(self, pygame.SYSTEM_CURSOR_HAND)
        else: self.window.cursor_handler.reset(self)

        scale_offset = 0
        if self.toggled: scale_offset -= 12.5
        elif self.pressed: scale_offset -= 15
        elif self.hover: scale_offset -= 10
        derivative_width, derivative_height = calculate_derivative_size(
            *tuple(self.background_box.size), 
            *tuple(self.box.size), 
            scale_offset, self.smoothing, self.snapping
        )
        self.background_box.x -= derivative_width / 2
        self.background_box.y -= derivative_height / 2
        self.background_box.width += derivative_width
        self.background_box.height += derivative_height

    def draw(self, offset: tuple[int, int] = (0, 0)) -> None:
        pygame.draw.rect(self.window.screen, self.color.background, self.background_box.get_rect(offset), 0, self.border_radius)
        pygame.draw.rect(self.window.screen, self.color.border, self.background_box.get_rect(offset), self.border_width, self.border_radius)
        self.window.screen.blit(self.text_surface, self.text_surface.get_rect(center = self.background_box.rect.center))
        Object.draw(self, (offset[0] + self.background_box.pos.x, offset[1] + self.background_box.pos.y))

class InputBox(Object):
    """
    A text input component with advanced editing capabilities.

    Features:
    - Multi-line text input
    - Text selection and cursor management
    - Copy/paste functionality
    - Undo/redo system
    - Word wrapping
    - Customizable appearance

    Attributes:
        text_handler (Text): Handles text rendering and editing
        hover (bool): Current hover state
        border_radius (int): Corner rounding radius
        border_width (int): Border thickness
        smoothing (float): Animation smoothing factor (0-1)
        snapping (float): Size snapping threshold

    Args:
        text (str): Text content
        box (Box): Position and size
        color (ColorData): Color scheme
        font (FontSet): Font configuration
        border_radius (int): Corner rounding radius
        border_width (int): Border thickness
    """
    def __init__(self, text: str, box: Box, color: ColorData, font: FontSet, border_radius: int, border_width: int):
        Object.__init__(self, box, color, font.small, [pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.KEYDOWN, pygame.KEYUP])
        self.text_handler: Text = Text(text, font.small, box.size, max_lines=1)
        self.background_box: Box = self.box.copy()

        self.hover: bool = False

        self.border_radius: int = border_radius
        self.border_width: int = border_width

        self.smoothing: float = 0.35
        self.snapping: float = 0.5
    
    @property
    def text(self):
        return self.text_handler.text
    
    def on_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.box.rect.collidepoint(*event.pos)
        if self.drawn: self.text_handler.parse_event(event, self.background_box)
    
    def update(self) -> None:
        Object.update(self)
        if self.drawn and self.hover:
            self.window.cursor_handler.set_cursor(self, pygame.SYSTEM_CURSOR_IBEAM)
        else: self.window.cursor_handler.reset(self)

        scale_offset = 0
        if self.text_handler.active: scale_offset -= 0
        elif self.hover: scale_offset -= 10
        derivative_width, derivative_height = calculate_derivative_size(
            *tuple(self.background_box.size), 
            *tuple(self.box.size), 
            scale_offset, self.smoothing, self.snapping
        )
        self.background_box.x -= derivative_width / 2
        self.background_box.y -= derivative_height / 2
        self.background_box.width += derivative_width
        self.background_box.height += derivative_height

        self.text_handler.max_width = self.background_box.width - 10

    def draw(self, offset: tuple[int, int] = (0, 0)) -> None:
        pygame.draw.rect(self.window.screen, self.color.background, self.background_box.get_rect(offset), 0, self.border_radius)
        pygame.draw.rect(self.window.screen, self.color.border, self.background_box.get_rect(offset), self.border_width, self.border_radius)
        self.text_handler.draw(self.window.screen, tuple(self.background_box.pos))
        Object.draw(self, (offset[0] + self.background_box.pos.x, offset[1] + self.background_box.pos.y))

# This is mainly just an extention
from pygame.constants import *