import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class ExpenseTracker(toga.App):

    def startup(self):
        self.expenses = []

        self.main_box = toga.Box(
            style=Pack(direction=COLUMN, padding=30)
        )

        self.header = toga.Label(
            "💰 Expense Tracker",
            style=Pack(padding_bottom=10, font_size=22)
        )

        self.sub_header = toga.Label(
            "Track your daily spending easily",
            style=Pack(padding_bottom=20, font_size=12)
        )

        self.main_box.add(self.header)
        self.main_box.add(self.sub_header)

        self.card = toga.Box(
            style=Pack(direction=COLUMN, padding=20)
        )

        self.amount_label = toga.Label("Amount", style=Pack(padding_bottom=5))
        self.amount_input = toga.TextInput(
            placeholder="Enter amount",
            style=Pack(padding_bottom=15)
        )

        self.category_label = toga.Label("Category", style=Pack(padding_bottom=5))
        self.category_input = toga.TextInput(
            placeholder="Enter category",
            style=Pack(padding_bottom=15)
        )

        self.desc_label = toga.Label("Description", style=Pack(padding_bottom=5))
        self.desc_input = toga.TextInput(
            placeholder="Enter description",
            style=Pack(padding_bottom=20)
        )

        self.card.add(self.amount_label)
        self.card.add(self.amount_input)
        self.card.add(self.category_label)
        self.card.add(self.category_input)
        self.card.add(self.desc_label)
        self.card.add(self.desc_input)

        self.main_box.add(self.card)

        self.button_box = toga.Box(
            style=Pack(direction=ROW, padding_bottom=20)
        )

        self.add_button = toga.Button(
            "Add",
            on_press=self.add_expense,
            style=Pack(flex=1, padding=10)
        )

        self.total_button = toga.Button(
            "Total",
            on_press=self.show_total,
            style=Pack(flex=1, padding=10)
        )

        self.clear_button = toga.Button(
            "Clear",
            on_press=self.clear_expenses,
            style=Pack(flex=1, padding=10)
        )

        self.button_box.add(self.add_button)
        self.button_box.add(self.total_button)
        self.button_box.add(self.clear_button)

        self.main_box.add(self.button_box)

        self.history_label = toga.Label(
            "📋 Expense History",
            style=Pack(padding_bottom=10, font_size=14)
        )

        self.output = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=1, padding=10)
        )

        self.main_box.add(self.history_label)
        self.main_box.add(self.output)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def add_expense(self, widget):
        amount = self.amount_input.value
        category = self.category_input.value
        description = self.desc_input.value

        if not amount or not category:
            self.main_window.info_dialog("Error", "Amount and Category required")
            return

        try:
            amount = float(amount)
        except:
            self.main_window.info_dialog("Error", "Enter valid amount")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        self.expenses.append(expense)

        self.output.value += f"{category}  |  ₹{amount}  |  {description}\n"

        self.amount_input.value = ""
        self.category_input.value = ""
        self.desc_input.value = ""

    def show_total(self, widget):
        total = sum(exp["amount"] for exp in self.expenses)
        self.main_window.info_dialog("Total Expense", f"Total Spent: ₹{total}")

    def clear_expenses(self, widget):
        self.expenses.clear()
        self.output.value = ""

def main():
    return ExpenseTracker()
