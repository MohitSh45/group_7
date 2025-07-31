# Group 7 Team Members:
# Mohit Sharma
# Kuldeepsinh Zala
# Amanpreet Kaur

import tkinter as tk
from tkinter import ttk
import random
import threading
import time

class TemperatureSensor:
    def __init__(self, base_temp=20, variation=5, peak_chance=0.1, noise_level=0.5):
        """
        Initializes the temperature sensor simulator.
        :param base_temp: The average temperature value.
        :param variation: The range of fluctuation around the base.
        :param peak_chance: Probability of a sudden peak.
        :param noise_level: Small random variations.
        """
        self.base_temp = base_temp
        self.variation = variation
        self.peak_chance = peak_chance
        self.noise_level = noise_level
        self.current_temp = base_temp

    def generate_temperature(self) -> float:
        """Simulates temperature readings with realistic variations."""
        self.current_temp += random.gauss(0, self.noise_level)
        
        if random.random() < self.peak_chance:
            self.current_temp += random.uniform(self.variation / 2, self.variation)
        
        self.current_temp = max(self.base_temp - self.variation, min(self.current_temp, self.base_temp + self.variation))
        
        return (self.current_temp - (self.base_temp - self.variation)) / (2 * self.variation) * 100  # Convert to percentage

class GaugeDisplay(tk.Tk):
    def __init__(self, sensor):
        super().__init__()
        self.sensor = sensor
        self.title("Temperature Sensor Gauge Display")
        self.geometry("300x300")
        
        self.value = tk.DoubleVar(value=50)  # Default value in percentage
        
        tk.Label(self, text="Temperature Reading (0-100%)", font=("Arial", 12)).pack(pady=10)
        self.gauge = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", variable=self.value)
        self.gauge.pack(pady=10)
        
        self.entry = tk.Entry(self, textvariable=self.value)
        self.entry.pack(pady=5)
        self.button = tk.Button(self, text="Update Value", command=self.update_gauge)
        self.button.pack(pady=5)
        
        self.description = tk.Label(self, text="Current Temperature: 50%", font=("Arial", 10))
        self.description.pack(pady=5)
        
        self.start_auto_update()

    def update_gauge(self):
        try:
            val = float(self.entry.get())
            if 0 <= val <= 100:
                self.value.set(val)
                self.description.config(text=f"Current Temperature: {val}%")
            else:
                self.description.config(text="Enter a value between 0-100")
        except ValueError:
            self.description.config(text="Invalid input! Enter a number.")

    def auto_update(self):
        while True:
            new_value = self.sensor.generate_temperature()
            self.value.set(new_value)
            self.description.config(text=f"Current Temperature: {new_value:.2f}%")
            time.sleep(1)

    def start_auto_update(self):
        threading.Thread(target=self.auto_update, daemon=True).start()

if __name__ == "__main__":
    sensor = TemperatureSensor()
    app = GaugeDisplay(sensor)
    app.mainloop()