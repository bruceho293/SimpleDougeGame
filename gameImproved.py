from tkinter import *
import random
import time

game = Tk()
game.title("Game")
game.resizable(0,0)
game.geometry("800x800+50+50")

# Specify the frames in the game
top = Frame(game, height = 200)
mid = Frame(game, height = 400)
top.pack(side = TOP)
mid.pack()

# End of the frames


# Top frame
name = Label(top, text = "Try to douge if you can")
name.config(font=('times', 40, 'bold'))
name.pack()
# End of top frames

# Middle frame
game_layout = Canvas(mid, width = 400, height = 400)
game_layout.config(highlightbackground = "black", highlightthickness = 1)
game_layout.pack()

class Player:
    def __init__(self, canvas, oval, rec, line, color):
        self.canvas = canvas
        self.oval = oval
        self.rec = rec
        self.line = line

        # pos_oval = self.canvas.coords(self.oval.id)
        # pos_rec = self.canvas.coords(self.rec.id)
        # pos_line = self.canvas.coords(self.line.id)
        # dx = int((pos_oval[0] + pos_rec[0] + pos_line[0]) / 3)
        # dy = int((pos_oval[1] + pos_rec[1] + pos_line[1]) / 3)

        self.id = self.canvas.create_rectangle(0, 0, 20, 20, fill = color)
        self.canvas.move(self.id, 250, 380)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.x, self.y = 0, 0
        self.vx, self.vy = 1, 1
        self.game_over = 0

    def Game_over(self):
        pos_oval = self.canvas.coords(self.oval.id)
        pos_rec = self.canvas.coords(self.rec.id)
        pos_line = self.canvas.coords(self.line.id)
        pos = self.canvas.coords(self.id)


        if (pos[0] >= pos_oval[0] and pos[0] <= pos_oval[2]) or (pos[2] >= pos_oval[0] and pos[2] <= pos_oval[2]) :
            if (pos[1] >= pos_oval[1] and pos[1] <= pos_oval[3]) or (pos[3] >= pos_oval[1] and pos[3] <= pos_oval[3]):
                self.game_over = 1


        if (pos[0] >= pos_rec[0] and pos[0] <= pos_rec[2]) or (pos[2] >= pos_rec[0] and pos[2] <= pos_rec[2]) :
            if (pos[1] >= pos_rec[1] and pos[1] <= pos_rec[3]) or (pos[3] >= pos_rec[1] and pos[3] <= pos_rec[3]):
                self.game_over = 1

        if pos_line[0] >= pos[0] and pos_line[0] <= pos[2]:
            if (pos_line[1] >= pos[1] and pos_line[1] <= pos[3]) or (pos_line[3] >= pos[1] and pos_line[3] <= pos[3]) or (pos[1] > pos_line[1] and pos[3] < pos_line[3] ):
                self.game_over = 1
    # def Score(self):
    #     self.score += 1
    #
    # def get_score(self):
    #     return str(self.score)

    # def turn_left(self, event):
    #     pos = self.canvas.coords(self.id)
    #     if pos[0] > 10:
    #         self.x = -10
    #         self.canvas.move(self.id, self.x, 0)
    #
    # def turn_right(self, event):
    #     pos = self.canvas.coords(self.id)
    #     if pos[2] < 400:
    #         self.x = 10
    #         self.canvas.move(self.id, self.x, 0)
    #
    # def go_up(self, event):
    #     pos = self.canvas.coords(self.id)
    #     if pos[1] > 10:
    #         self.y = -10
    #         self.canvas.move(self.id, 0, self.y)
    #
    # def go_down(self, event):
    #     pos = self.canvas.coords(self.id)
    #     if pos[3] < 400:
    #         self.y = 10
    #         self.canvas.move(self.id, 0, self.y)
    def move(self, event):
        pos = self.canvas.coords(self.id)
        if event.keysym == "Up":
                if pos[1] > 0:
                    self.x = 0
                    self.y = -10
                else:
                    self.x, self.y = 0, 0
        elif event.keysym == "Down":
                if pos[3] < 400:
                    self.x = 0
                    self.y = 10
                else:
                    self.x, self.y = 0, 0
        elif event.keysym == "Left":
                if pos[0] > 0:
                    self.x = -10
                    self.y = 0
                else:
                    self.x, self.y = 0, 0
        elif event.keysym == "Right":
                if pos[2] < 400:
                    self.x = 10
                    self.y = 0
                else:
                    self.x, self.y = 0, 0
        self.canvas.move(self.id, self.x, self.y)
        print (self.canvas.coords(self.id))

class Oval:
    def __init__(self, canvas, color):
        self.canvas = canvas
        x1 = random.randint(0, 360)
        x2 = x1 + 40
        y1 = 0
        y2 = 50
        self.id = self.canvas.create_oval(x1, y1, x2, y2, fill = color)
        self.y = 30

    def flying(self):
        self.canvas.move(self.id, 0, self.y)


class Rectangle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        x1 = random.randint(0, 360)
        x2 = x1 + 40
        y1 = random.randint(0, 360)
        y2 = y1 + 40
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill = color)
        self.x = 20
        self.y = 20

    def flying(self):
        number = random.randint (0, 1)
        if number == 0:
            self.canvas.move(self.id, 0, self.y)
        else:
            self.canvas.move(self.id, self.x, 0)

class Line:
    def __init__(self, canvas):
        self.canvas = canvas
        x1 = 0
        x2 = x1
        y1 = random.randint(0, 200)
        y2 = y1 + 200
        color = ["red", "blue", "green"]
        random.shuffle(color)
        self.id = self.canvas.create_line(x1, y1, x2, y2, fill = color[0])
        self.x = 30
    def flying(self):
        self.canvas.move(self.id, self.x, 0)

Score = Label(mid)
Score.pack(side = BOTTOM)




def start_game():
    oval = Oval(game_layout, "blue")
    rectangle = Rectangle(game_layout, "yellow")
    line = Line(game_layout)
    player = Player(game_layout, oval, rectangle, line, "red")


    game.bind_all("<Left>", player.move)
    game.bind_all("<Right>", player.move)
    game.bind_all("<Up>", player.move)
    game.bind_all("<Down>", player.move)

    score = 0
    t1 = 0.1
    while 1:
        oval.flying()
        pos1 = game_layout.coords(oval.id)
        if pos1[3] >= 400:
            game_layout.delete(oval.id)
            score += 1
            color = ["red", "blue", "yellow", "orange", "purple"]
            random.shuffle(color)
            oval = Oval(game_layout, color[0])
            player.oval = oval
        game.update_idletasks()
        game.update()
        time.sleep(t1)


        rectangle.flying()
        pos2 = game_layout.coords(rectangle.id)
        if pos2[3] >= 400 or pos2[2] >= 400:
            game_layout.delete(rectangle.id)
            score += 1
            color = ["red", "blue", "yellow", "orange", "purple"]
            random.shuffle(color)
            rectangle = Rectangle(game_layout, color[0])
            player.rec = rectangle
        game.update_idletasks()
        game.update()
        time.sleep(t1 - 0.05)

        line.flying()
        pos3 = game_layout.coords(line.id)
        if pos3[2] >= 400:
            game_layout.delete(line.id)
            score += 1
            line = Line(game_layout)
            player.line = line
        game.update_idletasks()
        game.update()
        time.sleep(t1 + 0.05)

        Score.config(text = "Score: " + str(score), font =("times", 30, "bold"))
        player.Game_over()
        gameOver = player.game_over
        if gameOver:
            player.score = score
            break
    Score.config(text = "Game over. Your score is " + str(player.score))

start_button = Button(mid, text = "Start the game", command = start_game)
start_button.pack(side = TOP)
exit_button = Button(mid, text = "Close the game", command = game.destroy)
exit_button.pack(side = TOP)

game.mainloop()
# End of the Middle Frame
