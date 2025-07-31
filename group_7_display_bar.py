# Group 7 Team Members:
# Mohit Sharma
# Kuldeepsinh Zala
# Amanpreet Kaur

import tkinter as tk
from tkinter import ttk
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TemperatureSensor:
    def __init__(self, base_temp=20, variation=5, peak_chance=0.1, noise_level=0.5):
        self.base_temp = base_temp
        self.variation = variation
        self.peak_chance = peak_chance
        self.noise_level = noise_level
        self.current_temp = base_temp

    def generate_temperature(self) -> float:
        self.current_temp += random.gauss(0, self.noise_level)
        if random.random() < self.peak_chance:
            self.current_temp += random.uniform(self.variation / 2, self.variation)
        self.current_temp = max(self.base_temp - self.variation, min(self.current_temp, self.base_temp + self.variation))
        return (self.current_temp - (self.base_temp - self.variation)) / (2 * self.variation) * 100

class LineChartDisplay(tk.Tk):
    def __init__(self, sensor):
        super().__init__()
        self.sensor = sensor
        self.title("Temperature Sensor Line Chart Display")
        self.geometry("500x400")
        
        self.values = []
        self.time_steps = []
        self.time_counter = 0
        self.update_task = None  # Store the task ID for auto-update
        
        tk.Label(self, text="Temperature Line Chart", font=("Arial", 12)).pack(pady=10)
        self.fig, self.ax = plt.subplots(figsize=(5, 3))
        self.ax.set_xlabel("Time Steps")
        self.ax.set_ylabel("Temperature (%)")
        self.ax.set_title("Live Temperature Data")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack()
        
        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)
        self.button = tk.Button(self, text="Update Chart", command=self.update_chart)
        self.button.pack(pady=5)
        
        self.description = tk.Label(self, text="Current Temperature: 0%", font=("Arial", 10))
        self.description.pack(pady=5)
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window close event
        self.auto_update()  # Start auto update

    def update_chart(self):
        try:
            val = float(self.entry.get())
            if 0 <= val <= 100:
                self.values.append(val)
                self.time_steps.append(self.time_counter)
                self.time_counter += 1
                self.redraw_chart()
                self.description.config(text=f"Current Temperature: {val}%")
            else:
                self.description.config(text="Enter a value between 0-100")
        except ValueError:
            self.description.config(text="Invalid input! Enter a number.")

    def auto_update(self):
        new_value = self.sensor.generate_temperature()
        self.values.append(new_value)
        self.time_steps.append(self.time_counter)
        self.time_counter += 1
        self.redraw_chart()
        self.description.config(text=f"Current Temperature: {new_value:.2f}%")
        self.update_task = self.after(1000, self.auto_update)  # Schedule next update in 1 second

    def redraw_chart(self):
        try:
            self.ax.clear()
            self.ax.plot(self.time_steps, self.values, marker='o', linestyle='-', color='b', label="Temperature")
            self.ax.set_xlabel("Time Steps")
            self.ax.set_ylabel("Temperature (%)")
            self.ax.set_title("Live Temperature Data")
            self.ax.legend()
            self.canvas.draw()  # Safely update the canvas
        except Exception as e:
            print(f"Error during chart redraw: {e}")

    def on_closing(self):
        if self.update_task is not None:
            self.after_cancel(self.update_task)  # Cancel scheduled update if exists
        self.destroy()

if __name__ == "__main__":
    sensor = TemperatureSensor()
    app = LineChartDisplay(sensor)
    app.mainloop()
