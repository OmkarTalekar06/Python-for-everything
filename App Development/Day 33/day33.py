import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class NotesApp(toga.App):

    def startup(self):

        # Store notes in dictionary
        self.notes_data = {}

        # App Heading
        heading = toga.Label(
            "My Notes",
            style=Pack(
                padding=15,
                font_size=22,
                font_weight="bold",
                color="#FF8C42"
            )
        )

        # Title input
        self.title_input = toga.TextInput(
            placeholder="Enter note title",
            style=Pack(padding=10)
        )

        # Content input
        self.content_input = toga.MultilineTextInput(
            placeholder="Write your note here...",
            style=Pack(flex=1, padding=10)
        )

        # Notes list
        self.notes_list = toga.Selection(
            items=[],
            on_change=self.open_note,
            style=Pack(flex=1, padding=10)
        )

        # Save button
        save_button = toga.Button(
            "Save",
            on_press=self.save_note,
            style=Pack(flex=1, padding=5)
        )

        # Delete button
        delete_button = toga.Button(
            "Delete",
            on_press=self.delete_note,
            style=Pack(flex=1, padding=5)
        )

        # Button row
        button_box = toga.Box(
            children=[save_button, delete_button],
            style=Pack(direction=ROW)
        )

        # Editor side (right side)
        editor_box = toga.Box(
            children=[heading, self.title_input, self.content_input, button_box],
            style=Pack(direction=COLUMN, flex=2, padding=10)
        )

        # Main layout
        main_box = toga.Box(
            children=[self.notes_list, editor_box],
            style=Pack(direction=ROW, flex=1)
        )

        # Main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # -----------------------
    # Save Note
    # -----------------------
    def save_note(self, widget):

        title = self.title_input.value.strip()
        content = self.content_input.value.strip()

        if title == "" or content == "":
            return

        self.notes_data[title] = content
        self.notes_list.items = list(self.notes_data.keys())

        self.title_input.value = ""
        self.content_input.value = ""

    # -----------------------
    # Open Note
    # -----------------------
    def open_note(self, widget):

        selected = self.notes_list.value

        if selected:
            self.title_input.value = selected
            self.content_input.value = self.notes_data[selected]

    # -----------------------
    # Delete Note
    # -----------------------
    def delete_note(self, widget):

        selected = self.notes_list.value

        if selected:
            del self.notes_data[selected]
            self.notes_list.items = list(self.notes_data.keys())

            self.title_input.value = ""
            self.content_input.value = ""


def main():
    return NotesApp("Notes App", "org.example.notesapp")
