import sys, json
from src.tetris import Tetris, Text
from src.button import Button
from src.settings import *


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption("TETRIS")
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.images = self.load_images()

        self.set_timer()
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
                Endgame(self.screen).run()
                self.tetris.game_over_flag = False
            else:
                self.check_events()
                self.update()
                self.draw()


class Username:
    def __init__(self, screen):
        pg.init()
        self.screen = screen
        self.list_username = ""
        self.under_username = ""
        self.before_username = "Enter your name"

    def draw(self):
        self.name = pg.font.Font(FONT_PATH, 40)
        self.press = pg.font.Font(FONT_PATH, 20)

        self.name_rect = self.name.render(self.before_username or self.list_username, True, (233, 175, 135))
        self.press_rect = self.press.render(self.under_username, True, (233, 175, 135))

        self.screen.blit(self.name_rect, (WIN_RES[0] / 2 - self.name_rect.get_width() / 2, 325))
        self.screen.blit(self.press_rect, (WIN_RES[0] / 2 - self.press_rect.get_width() / 2, 375))


class Endgame:
    def __init__(self, screen):
        self.screen = screen

        self.app = App()
        self.username = Username(self.screen)

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
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    self.username.list_username = self.username.list_username[:-1]
                    self.username.under_username = "Press enter to validate"
                elif event.key == pg.K_RETURN and self.username.list_username != "":
                    self.username.under_username = "Username has been saved"
                    self.save_username(self.username.list_username)
                else:
                    self.username.before_username = ""
                    self.username.under_username = "Press enter to validate"
                    self.username.list_username += event.unicode

    def save_username(self, username):
        try:
            with open("data/score.json", "r") as file:
                data = json.load(file)

        except ValueError:
            data = {
                "Current score": "",
                "Users and Scores": {}
            }

        if username not in [i for i in data["Users and Scores"]]:
            data["Users and Scores"][username] = data["Current score"]

        elif data["Users and Scores"][username] < data["Current score"]:
            data["Users and Scores"][username] = data["Current score"]

        data["Current score"] = 0

        with open("data/score.json", "w") as file:
            json.dump(data, file, indent=4)

    def draw(self):
        background = pg.image.load("assets/background/background_menu.png")
        self.screen.blit(background, (0, 0))

        self.text = pg.font.Font(FONT_PATH, 80)
        self.text_rect = self.text.render("GAME OVER", True, (233, 175, 135))
        self.screen.blit(self.text_rect, (WIN_RES[0] / 2 - self.text_rect.get_width() / 2, 225))

        self.username.draw()

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
