import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import paho.mqtt.client as mqtt

from group_7_data_generator import DataGenerator
from group_7_utils import Utils

class PublisherApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Group 7 Publisher")

        self.topic = "group7/data"
        self.generator = DataGenerator()
        self.client = mqtt.Client()
        self.client.connect("localhost", 1883, 60)

        self.running = False
        self.delay = 2

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.window, text="Publishing Delay (sec):").pack()
        self.delay_entry = tk.Entry(self.window)
        self.delay_entry.insert(0, str(self.delay))
        self.delay_entry.pack()

        tk.Button(self.window, text="Start Publishing", command=self.start_publishing).pack(pady=5)
        tk.Button(self.window, text="Stop Publishing", command=self.stop_publishing).pack()

    def start_publishing(self):
        try:
            self.delay = float(self.delay_entry.get())
            self.running = True
            threading.Thread(target=self.publish_loop, daemon=True).start()
        except ValueError:
            messagebox.showerror("Error", "Invalid delay value!")

    def stop_publishing(self):
        self.running = False

    def publish_loop(self):
        count = 0
        while self.running:
            count += 1

            if random.randint(1, 100) == 50:
                continue  # Randomly skip a transmission (~1 in 100)

            if count % 25 == 0 and random.choice([True, False]):
                value = self.generator.get_wild_value()
            else:
                value = self.generator.get_value()

            packet = Utils.generate_packet(value)
            self.client.publish(self.topic, packet)
            print(f"Published: {packet}")
            time.sleep(self.delay)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PublisherApp()
    app.run()
