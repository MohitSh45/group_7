import tkinter as tk
import threading
import paho.mqtt.client as mqtt
import time

from group_7_utils import Utils

class SubscriberApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Group 7 Subscriber")

        self.topic = "group7/data"
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.connect("localhost", 1883, 60)
        self.client.subscribe(self.topic)

        self.data_log = []

        self.setup_ui()
        self.listen_thread = threading.Thread(target=self.client.loop_forever)
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def setup_ui(self):
        self.display = tk.Text(self.window, height=20, width=60)
        self.display.pack()

    def on_message(self, client, userdata, msg):
        try:
            packet = Utils.parse_packet(msg.payload.decode())
            value = packet["value"]
            packet_id = packet["packet_id"]
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(packet["timestamp"]))

            # Check for "wild" or "missing" data
            warning = ""
            if value > 40 or value < 10:
                warning = " [OUT OF RANGE]"

            log = f"[{timestamp}] Packet ID: {packet_id} | Value: {value}{warning}\n"
            self.display.insert(tk.END, log)
            self.display.see(tk.END)
            self.data_log.append(packet_id)

        except Exception as e:
            print("Error parsing message:", e)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = SubscriberApp()
    app.run()
