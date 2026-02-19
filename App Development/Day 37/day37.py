import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ContactManager(toga.App):

    def startup(self):
        self.contacts = []

        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=30))

        self.title = toga.Label(
            "📇 Contact Manager",
            style=Pack(font_size=20, padding_bottom=20)
        )
        self.main_box.add(self.title)

        self.name_input = toga.TextInput(
            placeholder="Enter Name",
            style=Pack(padding_bottom=10)
        )
        self.main_box.add(self.name_input)

        self.phone_input = toga.TextInput(
            placeholder="Enter Phone Number",
            style=Pack(padding_bottom=10)
        )
        self.main_box.add(self.phone_input)

        self.email_input = toga.TextInput(
            placeholder="Enter Email",
            style=Pack(padding_bottom=15)
        )
        self.main_box.add(self.email_input)

        self.button_box = toga.Box(style=Pack(direction=ROW, padding_bottom=15))

        self.add_button = toga.Button(
            "Add",
            on_press=self.add_contact,
            style=Pack(flex=1, padding=10)
        )

        self.delete_button = toga.Button(
            "Delete",
            on_press=self.delete_contact,
            style=Pack(flex=1, padding=10)
        )

        self.button_box.add(self.add_button)
        self.button_box.add(self.delete_button)

        self.main_box.add(self.button_box)

        self.search_input = toga.TextInput(
            placeholder="Search by Name",
            style=Pack(padding_bottom=10)
        )
        self.main_box.add(self.search_input)

        self.search_button = toga.Button(
            "Search",
            on_press=self.search_contact,
            style=Pack(padding_bottom=15)
        )
        self.main_box.add(self.search_button)

        self.output = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=1)
        )
        self.main_box.add(self.output)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def add_contact(self, widget):
        name = self.name_input.value
        phone = self.phone_input.value
        email = self.email_input.value

        if not name or not phone:
            self.main_window.info_dialog("Error", "Name and Phone required")
            return

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        self.contacts.append(contact)
        self.display_contacts()

        self.name_input.value = ""
        self.phone_input.value = ""
        self.email_input.value = ""

    def delete_contact(self, widget):
        name = self.name_input.value

        self.contacts = [c for c in self.contacts if c["name"] != name]
        self.display_contacts()

    def search_contact(self, widget):
        keyword = self.search_input.value.lower()
        self.output.value = ""

        for contact in self.contacts:
            if keyword in contact["name"].lower():
                self.output.value += f"{contact['name']} | {contact['phone']} | {contact['email']}\n"

    def display_contacts(self):
        self.output.value = ""
        for contact in self.contacts:
            self.output.value += f"{contact['name']} | {contact['phone']} | {contact['email']}\n"


def main():
    return ContactManager()
