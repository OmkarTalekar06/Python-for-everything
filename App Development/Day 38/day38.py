import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import datetime
import threading
import time
import asyncio


class AlarmClock(toga.App):

    def startup(self):

        self.main_window = toga.MainWindow(title=self.formal_name)

        self.current_time_label = toga.Label(
            "Current Time: ",
            style=Pack(padding=10, font_size=16)
        )

        self.hour_input = toga.TextInput(
            placeholder="Hour (0-23)",
            style=Pack(flex=1, padding=5)
        )

        self.minute_input = toga.TextInput(
            placeholder="Minute (0-59)",
            style=Pack(flex=1, padding=5)
        )

        self.status_label = toga.Label(
            "Alarm Status: Not Set",
            style=Pack(padding=10, font_size=14)
        )

        self.set_button = toga.Button(
            "Set Alarm",
            on_press=self.set_alarm,
            style=Pack(padding=5)
        )

        input_box = toga.Box(
            children=[self.hour_input, self.minute_input],
            style=Pack(direction=ROW, padding=5)
        )

        main_box = toga.Box(
            children=[
                self.current_time_label,
                input_box,
                self.set_button,
                self.status_label
            ],
            style=Pack(direction=COLUMN, padding=20)
        )

        self.main_window.content = main_box
        self.main_window.show()

        self.add_background_task(self.refresh_clock)

    async def refresh_clock(self, widget):

        while True:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            self.current_time_label.text = f"Current Time: {now}"
            await asyncio.sleep(1)

    def set_alarm(self, widget):

        try:
            self.alarm_hour = int(self.hour_input.value)
            self.alarm_minute = int(self.minute_input.value)
            self.status_label.text = "Alarm Status: Active"

            thread = threading.Thread(target=self.check_alarm)
            thread.daemon = True
            thread.start()

        except:
            self.status_label.text = "Invalid Time Input"

    def check_alarm(self):

        while True:
            now = datetime.datetime.now()

            if now.hour == self.alarm_hour and now.minute == self.alarm_minute:
                self.status_label.text = "Alarm Triggered!"
                break

            time.sleep(1)


def main():
    return AlarmClock("AlarmClock", "org.example.alarmclock")
