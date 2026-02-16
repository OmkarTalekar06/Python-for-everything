import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class QuizApp(toga.App):

    def startup(self):

        self.questions = [
            ("Capital of France?", ["Berlin", "Paris", "Rome", "Madrid"], 1),
            ("2 + 2 = ?", ["3", "4", "5", "6"], 1),
            ("Python is a ?", ["Snake", "Language", "Car", "Game"], 1),
            ("CPU stands for?", ["Central Process Unit", "Central Processing Unit", "Control Unit", "Main Unit"], 1),
            ("HTML is used for?", ["Styling", "Structure", "Database", "AI"], 1),
            ("Android is based on?", ["Linux", "Windows", "iOS", "DOS"], 0),
            ("Which is a loop?", ["if", "for", "def", "class"], 1),
            ("RAM is?", ["Storage", "Memory", "CPU", "GPU"], 1),
            ("1 Byte = ?", ["4 bits", "8 bits", "16 bits", "32 bits"], 1),
            ("Which is OOP concept?", ["Loop", "Function", "Encapsulation", "Variable"], 2),
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = toga.Label(
            "",
            style=Pack(margin=20, font_size=16)
        )

        self.options_box = toga.Box(
            style=Pack(direction=COLUMN, margin=10)
        )

        self.option_buttons = []

        for i in range(4):
            btn = toga.Button(
                "",
                on_press=self.check_answer,
                style=Pack(margin=5)
            )
            self.option_buttons.append(btn)
            self.options_box.add(btn)

        self.score_label = toga.Label(
            "Score: 0 / 10",
            style=Pack(margin=10)
        )

        main_box = toga.Box(
            children=[self.question_label, self.options_box, self.score_label],
            style=Pack(direction=COLUMN, margin=10)
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        self.load_question()

    # -------------------
    def load_question(self):

        if self.current_question < len(self.questions):

            question, options, _ = self.questions[self.current_question]
            self.question_label.text = question

            for i in range(4):
                self.option_buttons[i].text = options[i]

                # Proper reset
                try:
                    del self.option_buttons[i].style.background_color
                except:
                    pass

                self.option_buttons[i].enabled = True

        else:
            self.show_result()

    # -------------------
    def check_answer(self, widget):

        _, _, correct_index = self.questions[self.current_question]
        selected_index = self.option_buttons.index(widget)

        for btn in self.option_buttons:
            btn.enabled = False

        if selected_index == correct_index:
            widget.style.background_color = "green"
            self.score += 1
        else:
            widget.style.background_color = "red"
            self.option_buttons[correct_index].style.background_color = "green"

        self.score_label.text = f"Score: {self.score} / 10"

        self.current_question += 1

        self.loop.call_later(1.5, self.load_question)

    # -------------------
    def show_result(self):

        self.question_label.text = f"Quiz Finished! Final Score: {self.score} / 10"
        self.options_box.clear()


def main():
    return QuizApp("Quiz App", "org.example.quizapp")
