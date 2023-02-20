import sys
from src.main import App
from src.button import Button
from src.settings import *


class Menu:
    def __init__(self):
        pg.init()
        pg.display.set_caption("TETRIS")
        self.screen = pg.display.set_mode(WIN_RES)
        self.app = App()

        self.button_play = Button(image=None, pos=(WIN_RES[0] / 2, 400), text_input="PLAY",
                                  font=70, base_color="white", hovering_color=(233, 135, 193))
        self.button_score = Button(image=None, pos=(WIN_RES[0] / 2, 500), text_input="SCORE",
                                   font=70, base_color="white", hovering_color=(151, 135, 233))
        self.button_quit = Button(image=None, pos=(WIN_RES[0] / 2, 600), text_input="QUIT",
                                  font=70, base_color="white", hovering_color=(233, 135, 144))

    def events(self):
        self.mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.button_play.checkForInput(self.mouse_pos):
                    self.app.run()
                elif self.button_score.checkForInput(self.mouse_pos):
                    pass
                elif self.button_quit.checkForInput(self.mouse_pos):
                    pg.quit()
                    sys.exit()

    def draw(self):
        background = pg.image.load("assets/background/background_menu.png")
        self.screen.blit(background, (0, 0))

        self.text = pg.font.Font(FONT_PATH, 80)
        self.text_rect = self.text.render("TETRIS", True, (233, 175, 135))
        self.screen.blit(self.text_rect, (WIN_RES[0] / 2 - self.text_rect.get_width() / 2, 200))

        self.button_play.update(self.screen)
        self.button_score.update(self.screen)
        self.button_quit.update(self.screen)
        pg.display.flip()

    def update(self):
        self.button_play.changeColor(self.mouse_pos)
        self.button_score.changeColor(self.mouse_pos)
        self.button_quit.changeColor(self.mouse_pos)

    def run(self):
        while True:
            self.events()
            self.draw()
            self.update()


if __name__ == '__main__':
    menu = Menu()
    menu.run()
