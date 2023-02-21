import sys
import pathlib
from src.tetris import Tetris, Text
from src.settings import *

from src.button import Button


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption("TETRIS")
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = Tetris(self)
        self.text = Text(self)

    def load_images(self):
        images = []
        for i in range(7):
            image = pg.image.load(SPRITE_DIR_PATH + str(i) + ".png")
            images.append(image)
        return images

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def update(self):
        self.clock.tick(FPS)
        self.tetris.update()

    def draw(self):
        self.screen.fill(color=BG_COLOR)
        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))
        self.tetris.draw()
        self.text.draw()
        pg.display.flip()

    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True

    def run(self):
        while True:
            if self.tetris.game_over_flag:
                Endgame().run()
                self.tetris.game_over_flag = False
            else:
                self.check_events()
                self.update()
                self.draw()


class Endgame:
    def __init__(self):
        pg.init()
        pg.display.set_caption("TETRIS")
        self.screen = pg.display.set_mode(WIN_RES)
        self.app = App()

        self.button_play = Button(image=None, pos=(WIN_RES[0] / 2, 500), text_input="PLAY AGAIN",
                                  font=60, base_color="white", hovering_color=(233, 135, 193))
        self.button_quit = Button(image=None, pos=(WIN_RES[0] / 2, 600), text_input="QUIT",
                                  font=60, base_color="white", hovering_color=(233, 135, 144))

    def events(self):
        self.mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.button_play.checkForInput(self.mouse_pos):
                    self.app.run()
                elif self.button_quit.checkForInput(self.mouse_pos):
                    pg.quit()
                    sys.exit()

    def draw(self):
        background = pg.image.load("assets/background/background_menu.png")
        self.screen.blit(background, (0, 0))

        self.text = pg.font.Font(FONT_PATH, 80)
        self.text_rect = self.text.render("GAME OVER", True, (233, 175, 135))
        self.screen.blit(self.text_rect, (WIN_RES[0] / 2 - self.text_rect.get_width() / 2, 225))

        self.button_play.update(self.screen)
        self.button_quit.update(self.screen)
        pg.display.flip()

    def update(self):
        self.button_play.changeColor(self.mouse_pos)
        self.button_quit.changeColor(self.mouse_pos)

    def run(self):
        while True:
            self.events()
            self.draw()
            self.update()
