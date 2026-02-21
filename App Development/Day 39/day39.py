import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import os


class FileManager(toga.App):

    def startup(self):

        self.current_path = os.getcwd()

        self.main_window = toga.MainWindow(title=self.formal_name)

        self.path_label = toga.Label(
            f"Path: {self.current_path}",
            style=Pack(padding=10)
        )

        self.file_input = toga.TextInput(
            placeholder="Enter file name",
            style=Pack(flex=1, padding=5)
        )

        self.content_input = toga.MultilineTextInput(
            placeholder="Enter file content",
            style=Pack(flex=1, padding=5, height=100)
        )

        self.output_area = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=1, padding=5)
        )

        self.create_button = toga.Button(
            "Create File",
            on_press=self.create_file,
            style=Pack(flex=1, padding=5)
        )

        self.read_button = toga.Button(
            "Read File",
            on_press=self.read_file,
            style=Pack(flex=1, padding=5)
        )

        self.delete_button = toga.Button(
            "Delete File",
            on_press=self.delete_file,
            style=Pack(flex=1, padding=5)
        )

        self.list_button = toga.Button(
            "List Files",
            on_press=self.list_files,
            style=Pack(flex=1, padding=5)
        )

        button_row1 = toga.Box(
            children=[self.create_button, self.read_button],
            style=Pack(direction=ROW, padding=5)
        )

        button_row2 = toga.Box(
            children=[self.delete_button, self.list_button],
            style=Pack(direction=ROW, padding=5)
        )

        main_box = toga.Box(
            children=[
                self.path_label,
                self.file_input,
                self.content_input,
                button_row1,
                button_row2,
                self.output_area
            ],
            style=Pack(direction=COLUMN, padding=10)
        )

        self.main_window.content = main_box
        self.main_window.show()

    def create_file(self, widget):

        filename = self.file_input.value

        if filename:
            try:
                with open(filename, "w") as f:
                    f.write(self.content_input.value)
                self.output_area.value = "File Created Successfully"
            except:
                self.output_area.value = "Error Creating File"
        else:
            self.output_area.value = "Enter File Name"

    def read_file(self, widget):

        filename = self.file_input.value

        if filename:
            try:
                with open(filename, "r") as f:
                    data = f.read()
                self.output_area.value = data
            except:
                self.output_area.value = "File Not Found"
        else:
            self.output_area.value = "Enter File Name"

    def delete_file(self, widget):

        filename = self.file_input.value

        if filename:
            try:
                os.remove(filename)
                self.output_area.value = "File Deleted Successfully"
            except:
                self.output_area.value = "File Not Found"
        else:
            self.output_area.value = "Enter File Name"

    def list_files(self, widget):

        try:
            files = os.listdir(self.current_path)
            self.output_area.value = "\n".join(files)
        except:
            self.output_area.value = "Error Listing Files"


def main():
    return FileManager("FileManager", "org.example.filemanager")
