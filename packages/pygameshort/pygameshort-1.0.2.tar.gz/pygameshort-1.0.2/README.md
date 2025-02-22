# pygameshort
A user interface extension library for Pygame with built-in networking capabilities.

## Features

- **Enhanced UI Components**
    - Button system with hover and click effects
    - Input boxes with full text editing capabilities
    - Smooth animations and transitions
    - Customizable color schemes and themes

- **Advanced Text Handling**
    - Multi-line text support
    - Text selection and manipulation
    - Copy/paste functionality
    - Undo/redo system


- **Integrated Networking**
    - Seamless integration with secure_network library
    - Easy-to-use connection management
    - Event-based network communication
    - Built-in security features


- **Flexible Layout System**
    - Box-based positioning
    - Size and position matrices
    - Automatic text wrapping
    - Responsive design capabilities

## Installation
```bash
pip install pygameshort
```

## Dependencies

- pygame
- secure_network
- pyperclip

## Roadmap

- ✔️ Uses secure networking package by me
- ✔️ Window, plus managers
    - ✔️ Event manager / distrebutor (Tickets)
- ✔️ All events are gathered into one event flow
- ✔️ Cooldown class
- ✔️ Cursor system
- ✔️ Systems for metrical values
- ✔️ Systems for fonts and color values
- ✔️ Object system(s)
    - ✔️ Fully functional text (input) system
    - ✔️ Easily made custom objects
    - ✔️ Buttons
    - ✔️ Input Box
    - ❌ Sliders
    - ❌ Loading bars
    - ❌ Movable, resizeable, closable ..etc.. windows
    - ❌ Drag and drop
    - ❌ Tab system
    - ❌ Layout manager
    - More to be added!

## Quick Start
```python
import pygameplus as pgp

# Create a window with networking
key = pgp.Key(b'I\xebi\xc3U\xa47\x85I%I@9\xf9b\ry\x807Fq\x1aj\x15585\xf8P\xc45\xb7H\xccg\x0fs\x92s\xd70\xd2o\x9fw\x83J/lt-\x03R\xb1Q^H\xf1O\xadQ 0\xe1') # Leave empty to generate a new
fernet_key, hmac_key = key.extract()
conn = pgp.Connection(fernet_key, hmac_key, "localhost", 8000, pgp.secure_network.CLIENT)

# Initialize window
window = pgp.Window("My App", conn, on_render=lambda: None)

# Create a button
button = pgp.Button(
    text="Click Me!",
    box=pgp.Box(100, 100, 200, 50),
    color=pgp.ColorData.create_light_theme(),
    font=pgp.FontSet().load_system_font("Arial", (12, 16, 24)),
    border_radius=5,
    border_width=2,
    switch=False,
    callback=lambda: print("Button clicked!")
)

# Create an input box
input_box = pgp.InputBox(
    text="Enter text...",
    box=pgp.Box(100, 200, 200, 50),
    color=pgp.ColorData.create_light_theme(),
    font=pgp.FontSet().load_system_font("Arial", (12, 16, 24)),
    border_radius=5,
    border_width=2
)

# Create a scene
scene = pgp.Scene([button, input_box])

# Set up render function
def render():
    window.screen.fill((255, 255, 255))
    scene.draw()

window.on_render.append(render)

# Start the application
# Use "window.connect()" whenever you want to connect using the connection
# Remember to set the address correctly first
# Also remember to then auth with a username and a correlating password
window.run()
```


## UI Components
### Button
*The Button class provides a customizable button with:*

- Hover effects
- Click animations
- Toggle functionality
- Smooth size transitions

### InputBox
*The InputBox class offers a full-featured text input with:*

- Text selection
- Copy/paste support
- Cursor management
- Multi-line support
- Word wrapping

### Window
*The Window class serves as the main container and provides:*

- Event management
- Scene rendering
- Network integration
- Frame rate control

### Networking
*The library integrates with the secure_network package for encrypted communication:*

```python
# Create a secure connection
key = pgp.Key()
fernet_key, hmac_key = key.extract()
conn = pgp.Connection(
    fernet_key,
    hmac_key,
    "localhost",
    8000,
    pgp.secure_network.CLIENT
)

# Send data
conn.send("Hello, server!")
```


### Themes
***pygameshort** includes built-in theme support:*
```python
# Light theme
light_theme = pgp.ColorData.create_light_theme()

# Dark theme
dark_theme = pgp.ColorData.create_dark_theme()
```


## Contributing
*-- To be added --*

Contributions are welcome! Please feel free to submit a Pull Request.

### **License**
[Add your chosen license here]

### **Author**
*Neo Zetterberg*

- Email: 20091103neo@gmail.com

### Acknowledgments

Built on top of the excellent **Pygame** library |
Uses secure_network for encrypted communication