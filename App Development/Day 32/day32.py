import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class TodoApp(toga.App):

    def startup(self):

        # Main container (Full screen, high contrast)
        main_box = toga.Box(
            style=Pack(
                direction=COLUMN,
                flex=1,
                padding=20,
                background_color="#ffffff"
            )
        )

        # Title
        title = toga.Label(
            "MY TO-DO LIST",
            style=Pack(
                padding_bottom=20,
                font_size=26,
                font_weight="bold",
                color="#000000"
            )
        )

        # Input field
        self.task_input = toga.TextInput(
            placeholder="Enter your task...",
            style=Pack(
                flex=1,
                padding=12
            )
        )

        # Add button (high contrast blue)
        add_button = toga.Button(
            "ADD",
            on_press=self.add_task,
            style=Pack(
                padding=12,
                font_size=16,
                background_color="#0fef47",
                color="#ffffff"
            )
        )

        # Top row
        top_row = toga.Box(
            style=Pack(
                direction=ROW,
                padding_bottom=15
            )
        )

        top_row.add(self.task_input)
        top_row.add(add_button)

        # Task container (large scrollable list)
        self.task_container = toga.Box(
            style=Pack(
                direction=COLUMN,
                flex=1,
                padding=10
            )
        )

        scroll = toga.ScrollContainer(
            content=self.task_container,
            style=Pack(flex=1)
        )

        main_box.add(title)
        main_box.add(top_row)
        main_box.add(scroll)

        # Main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def add_task(self, widget):

        task_text = self.task_input.value

        if task_text != "":

            # Task row (light gray card)
            task_row = toga.Box(
                style=Pack(
                    direction=ROW,
                    padding=15,
                    padding_bottom=10,
                    background_color="#ffffff"
                )
            )

            # Task label (big font)
            task_label = toga.Label(
                task_text,
                style=Pack(
                    flex=1,
                    font_size=18,
                    color="#000000"
                )
            )

            # Delete button (red contrast)
            delete_button = toga.Button(
                "DELETE",
                on_press=lambda w, row=task_row: self.delete_task(row),
                style=Pack(
                    width=80,
                    background_color="#ff3b30",
                    color="#ffffff"
                )
            )

            task_row.add(task_label)
            task_row.add(delete_button)

            self.task_container.add(task_row)

            self.task_input.value = ""

    def delete_task(self, row):
        self.task_container.remove(row)


def main():
    return TodoApp("ToDo App", "org.example.todo")
