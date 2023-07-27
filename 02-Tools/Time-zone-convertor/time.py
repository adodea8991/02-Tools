import tkinter as tk
from datetime import datetime
import pytz

# Function to convert time between time zones
def convert_time():
    time_format = "%Y-%m-%d %H:%M:%S"
    selected_timezone = timezone_var.get()
    selected_timezone = pytz.timezone(selected_timezone)
    
    current_time = datetime.now()
    converted_time = current_time.astimezone(selected_timezone).strftime(time_format)
    
    converted_time_label.config(text="Converted Time: " + converted_time)

# Create the main window
window = tk.Tk()
window.title("Time Zone Converter")

# Timezone options
timezones = [
    'UTC',
    'US/Eastern',
    'US/Central',
    'US/Mountain',
    'US/Pacific',
    'Asia/Kolkata',
    'Europe/London',
    'Australia/Sydney'
]

# Create the GUI elements
timezone_label = tk.Label(window, text="Select Timezone:")
timezone_label.pack()

timezone_var = tk.StringVar(window)
timezone_var.set(timezones[0])  # Set the default timezone

timezone_combobox = tk.OptionMenu(window, timezone_var, *timezones)
timezone_combobox.pack()

convert_button = tk.Button(window, text="Convert", command=convert_time)
convert_button.pack()

converted_time_label = tk.Label(window, text="Converted Time: ")
converted_time_label.pack()

# Start the main event loop
window.mainloop()
