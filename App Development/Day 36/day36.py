import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import random
import string


class PasswordGenerator(toga.App):

    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=30))

        self.title = toga.Label(
            "🔐 Password Generator",
            style=Pack(font_size=20, padding_bottom=20)
        )
        self.main_box.add(self.title)

        self.length_label = toga.Label("Password Length", style=Pack(padding_bottom=5))
        self.main_box.add(self.length_label)

        self.length_input = toga.TextInput(
            placeholder="Enter length (e.g. 12)",
            style=Pack(padding_bottom=15)
        )
        self.main_box.add(self.length_input)

        self.options_box = toga.Box(style=Pack(direction=COLUMN, padding_bottom=15))

        self.upper_switch = toga.Switch("Include Uppercase", value=True)
        self.lower_switch = toga.Switch("Include Lowercase", value=True)
        self.digits_switch = toga.Switch("Include Numbers", value=True)
        self.symbols_switch = toga.Switch("Include Symbols", value=True)

        self.options_box.add(self.upper_switch)
        self.options_box.add(self.lower_switch)
        self.options_box.add(self.digits_switch)
        self.options_box.add(self.symbols_switch)

        self.main_box.add(self.options_box)

        self.generate_button = toga.Button(
            "Generate Password",
            on_press=self.generate_password,
            style=Pack(padding=10)
        )
        self.main_box.add(self.generate_button)

        self.result_input = toga.TextInput(
            readonly=True,
            style=Pack(padding_top=20)
        )
        self.main_box.add(self.result_input)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def generate_password(self, widget):
        length = self.length_input.value

        if not length:
            self.main_window.info_dialog("Error", "Enter password length")
            return

        try:
            length = int(length)
        except:
            self.main_window.info_dialog("Error", "Length must be number")
            return

        characters = ""

        if self.upper_switch.value:
            characters += string.ascii_uppercase
        if self.lower_switch.value:
            characters += string.ascii_lowercase
        if self.digits_switch.value:
            characters += string.digits
        if self.symbols_switch.value:
            characters += string.punctuation

        if characters == "":
            self.main_window.info_dialog("Error", "Select at least one option")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        self.result_input.value = password


def main():
    return PasswordGenerator()
