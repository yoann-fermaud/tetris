import sys, json
from src.game import App
from src.button import Button
from src.settings import *


class Menu: # It is the first page of the game
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
                    Score(self.screen).run()
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


class Score:
    def __init__(self, screen):
        self.screen = screen

        self.menu = Menu()

        self.button_back = Button(image=None, pos=(WIN_RES[0] / 2, 600), text_input="BACK",
                                  font=70, base_color="white", hovering_color=(233, 135, 193))

    def events(self):
        self.mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.button_back.checkForInput(self.mouse_pos):
                    self.menu.run()

    def sort_score(self):
        try:
            with open("data/score.json", "r") as file:
                data = json.load(file)
        except ValueError:
            data = {
                "Current score": "",
                "Users and Scores": {}
            }

        # In the json files, we sort all the value in the descending order. We want to display only the highest scores.
        # We have to use "reverse=True" to put the value in descending order, "item[1]"" indicates the ascending order
        sorted_scores = dict(sorted(data["Users and Scores"].items(), key=lambda item: item[1], reverse=True))
        data["Users and Scores"] = sorted_scores

        with open("data/score.json", "w") as file:
            json.dump(data, file, indent=4)

    def draw_score(self):
        try:
            with open("data/score.json", "r") as file:
                data = json.load(file)
        except ValueError:
            data = {
                "Current score": "",
                "Users and Scores": {}
            }

        increment_blit = 0
        dict_value = 0

        for key, value in data["Users and Scores"].items():
            if dict_value < 4:
                # Display key and value on separate lines
                text = f"{key}: {value}"
                self.label = pg.font.Font(FONT_PATH, 40)
                self.label_rect = self.label.render(text, True, "white")
                self.screen.blit(self.label_rect, (WIN_RES[0] / 2 - self.label_rect.get_width() / 2, 325 + increment_blit))
                increment_blit += 50
                dict_value += 1
            else:
                break

    def draw(self):
        background = pg.image.load("assets/background/background_menu.png")
        self.screen.blit(background, (0, 0))

        self.text = pg.font.Font(FONT_PATH, 80)
        self.text_rect = self.text.render("SCORES", True, (233, 175, 135))
        self.screen.blit(self.text_rect, (WIN_RES[0] / 2 - self.text_rect.get_width() / 2, 200))

        self.draw_score()
        self.button_back.update(self.screen)

        pg.display.flip()

    def update(self):
        self.sort_score()
        self.button_back.changeColor(self.mouse_pos)

    def run(self):
        while True:
            self.events()
            self.draw()
            self.update()


if __name__ == '__main__':
    menu = Menu()
    menu.run()
