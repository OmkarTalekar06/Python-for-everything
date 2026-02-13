import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class CalculatorApp(toga.App):

    def startup(self):

        self.expression = ""

        main_box = toga.Box(style=Pack(direction=COLUMN, margin=15))

        # Display Screen
        self.display = toga.Label(
            "0",
            style=Pack(font_size=32, margin_bottom=20)
        )

        main_box.add(self.display)

        # Button Layout (Rows)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for row in buttons:
            row_box = toga.Box(style=Pack(direction=ROW, margin_bottom=10))

            for item in row:
                btn = toga.Button(
                    item,
                    on_press=self.on_button_press,
                    style=Pack(flex=1, margin_right=5)
                )
                row_box.add(btn)

            main_box.add(row_box)

        self.main_window = toga.MainWindow(title="Simple Calculator")
        self.main_window.content = main_box
        self.main_window.show()

    def on_button_press(self, widget):

        value = widget.text

        if value == "C":
            self.expression = ""
            self.display.text = "0"

        elif value == "=":
            try:
                result = str(eval(self.expression))
                self.display.text = result
                self.expression = result
            except:
                self.display.text = "Error"
                self.expression = ""

        else:
            self.expression += value
            self.display.text = self.expression


def main():
    return CalculatorApp("Simple Calculator", "org.omkar.calculator")
