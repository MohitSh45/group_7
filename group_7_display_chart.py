# Group 7 Team Members:
# Mohit Sharma
# Kuldeepsinh Zala
# Amanpreet Kaur

import tkinter as tk
from tkinter import Canvas, ttk
import random
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

class ChartDisplayApp(tk.Tk):
    def __init__(self, sensor):
        super().__init__()
        self.sensor = sensor
        self.title("Temperature Sensor Display Chart")
        self.geometry("600x550")  # Increased height for better spacing
        self.values = [self.sensor.generate_temperature() for _ in range(20)]
        
        self.initUI()
    
    def initUI(self):
        tk.Label(self, text="Temperature Sensor Data", font=("Arial", 12)).pack(pady=10)
        
        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)
        self.button = tk.Button(self, text="Update Chart", command=self.update_chart)
        self.button.pack(pady=10)
        
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(pady=10)
        
        self.fig, self.axs = plt.subplots(2, 1, figsize=(6, 5), gridspec_kw={'hspace': 0.5})  # Added spacing
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack()
        
        self.draw_charts()
    
    def update_chart(self):
        try:
            val = float(self.entry.get())
            if 0 <= val <= 100:
                self.values.pop(0)
                self.values.append(val)
                self.draw_charts()
            else:
                print("Enter a value between 0-100")
        except ValueError:
            print("Invalid input! Enter a number.")
    
    def draw_charts(self):
        self.axs[0].clear()
        self.axs[1].clear()
        
        self.axs[0].plot(range(20), self.values, marker='o', linestyle='-', color='b', label="Temperature")
        self.axs[0].set_title("Line Chart")
        self.axs[0].legend()
        
        self.axs[1].bar(range(20), self.values, color='g', label="Temperature")
        self.axs[1].set_title("Bar Chart")
        self.axs[1].legend()
        
        self.canvas.draw()

if __name__ == "__main__":
    sensor = TemperatureSensor()
    app = ChartDisplayApp(sensor)
    app.mainloop()
