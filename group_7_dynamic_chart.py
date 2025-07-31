# Group 7 Team Members:
# Mohit Sharma
# Kuldeepsinh Zala
# Amanpreet Kaur
import tkinter as tk
from tkinter import Canvas, ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time

# Temperature Sensor Class
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

# Chart Display App Class
class ChartDisplayApp(tk.Tk):
    def __init__(self, sensor):
        super().__init__()
        self.sensor = sensor
        self.title("Dynamic Temperature Sensor Display Chart")
        self.geometry("600x550")  # Increased height for better spacing
        self.values = [self.sensor.generate_temperature() for _ in range(20)]  # Initial data
        self.initUI()

        # Setting the custom close protocol
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def initUI(self):
        tk.Label(self, text="Temperature Sensor Data (Dynamic)", font=("Arial", 12)).pack(pady=10)
        
        # Removed the Entry widget
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(pady=10)
        
        # Set up matplotlib figure and axes
        self.fig, self.axs = plt.subplots(2, 1, figsize=(6, 5), gridspec_kw={'hspace': 0.5})  # Added spacing
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack()
        
        # Draw initial charts
        self.draw_charts()

        # Start the background thread to update data
        self.update_thread = threading.Thread(target=self.update_data)
        self.update_thread.daemon = True  # Daemon thread will terminate with the GUI
        self.update_thread.start()

    # Method to update data dynamically in a thread
    def update_data(self):
        while True:
            time.sleep(0.5)  # Sleep for 0.5 second
            # Remove the first item and add a new random value
            self.values.pop(0)
            self.values.append(self.sensor.generate_temperature())
            self.draw_charts()

    # Method to draw the charts
    def draw_charts(self):
        self.axs[0].clear()
        self.axs[1].clear()

        # Line chart
        self.axs[0].plot(range(20), self.values, marker='o', linestyle='-', color='b', label="Temperature")
        self.axs[0].set_title("Line Chart")
        self.axs[0].legend()

        # Bar chart
        self.axs[1].bar(range(20), self.values, color='g', label="Temperature")
        self.axs[1].set_title("Bar Chart")
        self.axs[1].legend()

        # Update the canvas to reflect the changes
        self.canvas.draw()

    # Method to handle window close event
    def on_close(self):
        print("Closing the application...")
        self.quit()  # Terminate the Tkinter event loop

# Main function to run the app
if __name__ == "__main__":
    sensor = TemperatureSensor()  # Create sensor instance
    app = ChartDisplayApp(sensor)  # Initialize the app
    app.mainloop()  # Start the Tkinter main loop
