import random
import tkinter as tk

class Game:
    def __init__(self, master):
        self.master = master
        master.title("سنگ کاغذ قیچی")

        self.score = 0

        self.options = ["سنگ", "کاغذ", "قیچی"]
        self.outcomes = {
            "سنگ-قیچی": "بردی",
            "کاغذ-سنگ": "بردی",
            "قیچی-کاغذ": "بردی",
            "سنگ-کاغذ": "باختی",
            "کاغذ-قیچی": "باختی",
            "قیچی-سنگ": "باختی",
            "سنگ-سنگ": "مساوی",
            "کاغذ-کاغذ": "مساوی",
            "قیچی-قیچی": "مساوی"
        }

        self.player_choice = None
        self.computer_choice = None

        self.label = tk.Label(master, text="سنگ کاغذ قیچی", font=("Arial", 24))
        self.label.pack()

        self.options_frame = tk.Frame(master)
        self.options_frame.pack()

        for i, option in enumerate(self.options):
            button = tk.Button(self.options_frame, text=option, command=lambda i=i: self.set_player_choice(i))
            button.pack(side="left", padx=5, pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 16))
        self.result_label.pack()

        self.score_label = tk.Label(master, text=f"امتیاز: {self.score}", font=("Arial", 16))
        self.score_label.pack()

        self.play_again_button = tk.Button(master, text="بازی مجدد", command=self.play_again)
        self.play_again_button.pack(pady=10)

    def set_player_choice(self, choice):
        self.player_choice = choice
        self.play()

    def play(self):
        self.computer_choice = random.choice(self.options)
        outcome_key = self.options[self.player_choice] + "-" + self.computer_choice
        result = self.outcomes[outcome_key]

        if result == "بردی":
            self.score += 1
        elif result == "باختی":
            self.score -= 1

        self.result_label.config(text=result)
        self.score_label.config(text=f"امتیاز: {self.score}")

    def play_again(self):
        self.player_choice = None
        self.computer_choice = None
        self.result_label.config(text="")
        self.score = 0
        self.score_label.config(text=f"امتیاز: {self.score}")

root = tk.Tk()
game = Game(root)
root.mainloop()
