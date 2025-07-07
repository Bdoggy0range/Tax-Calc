import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((800, 600), 'theme.json')
manager = pygame_gui.UIManager((800, 600), theme_path="buttons.json")
button_layout_rect = pygame.Rect(30, 20, 100, 20)


calctxt = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((275, 225), (250, 50)),
                                        placeholder_text="Enter your original price eg. 699.99",
                                        manager=manager
                                        )
calcbtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 285), (100, 50)),
                                             text='Calculate',
                                             manager=manager)
outputtxt = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((275, 350), (250, 50)),
                                        placeholder_text="Output",
                                        manager=manager
                                        )

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            print(event.text)
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == calcbtn:
                try:
                    total = float(calctxt.get_text()) * 0.10 + float(calctxt.get_text())
                    outputtxt.set_text(f"${total:.2f}")
                except ValueError:
                    outputtxt.set_text("Invalid input")
        if event.type == pygame.QUIT:
            is_running = False
        

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()