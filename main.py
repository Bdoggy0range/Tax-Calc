import pygame
import pygame_gui

# Initialize pygame
pygame.init()

# Set window title and size
pygame.display.set_caption('Tax Calculator')
window_surface = pygame.display.set_mode((800, 600))

# Create and fill background surface
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

# Create UI manager with theme
manager = pygame_gui.UIManager((800, 600), theme_path="buttons.json")
button_layout_rect = pygame.Rect(30, 20, 100, 20)

# Input field for entering the original price
calctxt = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((275, 225), (250, 50)),
    placeholder_text="Enter your original price eg. 699.99",
    manager=manager
)

# Button to trigger calculation
calcbtn = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 285), (100, 50)),
    text='Calculate',
    manager=manager
)

# Output field to display the result
outputtxt = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((275, 350), (250, 50)),
    placeholder_text="Output",
    manager=manager
)

# Set up clock for controlling frame rate
clock = pygame.time.Clock()
is_running = True

# Main event loop
while is_running:
    time_delta = clock.tick(60)/1000.0  # Time since last frame in seconds
    for event in pygame.event.get():
        # Print text when user finishes entering text
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            print(event.text)
        # Handle button press event
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == calcbtn:
                try:
                    # Calculate total with 10% tax and display result
                    total = float(calctxt.get_text()) * 0.10 + float(calctxt.get_text())
                    outputtxt.set_text(f"${total:.2f}")
                except ValueError:
                    # Handle invalid input
                    outputtxt.set_text("Invalid input")
        # Handle window close event
        if event.type == pygame.QUIT:
            is_running = False

        # Pass event to UI manager
        manager.process_events(event)

    # Update UI manager
    manager.update(time_delta)

    # Draw background and UI
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    # Update display
    pygame.display.update()
