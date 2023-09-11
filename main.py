from main_screen import MainScreen

running = True
while running:
    game = MainScreen(1280, 720, "Platform Game")
    running = game.update()
