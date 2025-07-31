# Group 7 Team Members:
# Mohit Sharma
# Kuldeepsinh Zala
# Amanpreet Kaur
import random
import matplotlib.pyplot as plt

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
        
        return (self.current_temp - (self.base_temp - self.variation)) / (2 * self.variation)

# Generate 500 temperature readings
temp_sensor = TemperatureSensor()
temperatures = [temp_sensor.generate_temperature() for _ in range(500)]

time_steps = list(range(500))

# Plot the temperature variations
plt.figure(figsize=(10, 5))
plt.plot(time_steps, temperatures, label="Normalized Temperature Readings", color='b')
plt.xlabel("Time Steps")
plt.ylabel("Normalized Temperature (0 to 1)")
plt.title("Humidity Sensor at Progress Campus")
plt.legend()
plt.grid()
plt.show()
