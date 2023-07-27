import tkinter as tk
import vlc

# Define the radio stations
radio_stations = [
    {
        'name': 'New York Hott Radio',
        'url': 'http://stream.zeno.fm/5nqmkhb8dd0uv',
    },
    {
        'name': 'Radio Romania Actualitati',
        'url': 'https://stream.streamgenial.stream/595fmmy86p8uv',
    },
    {
        'name': 'JAZZ RADIO JAZZY FRENCH',
        'url': 'http://jazz-wr18.ice.infomaniak.ch/jazz-wr18-128.mp3',
    },
    {
        'name': 'Rock radio',
        'url': 'https://cast2.my-control-panel.com/proxy/vladas/stream',
    },
    {
        'name': 'Jazz24 - KNKX-HD2',
        'url': 'http://live.wostreaming.net/direct/ppm-jazz24mp3-ibc1',
    },
    {
        'name': 'Peaceful Radio',
        'url': 'http://samcloud.spacial.com/api/listen?sid=72935&amp;m=sc',
    }
]

# Global variable for storing the player instances
players = []

# Function to handle station selection
def select_station():
    selected_station = station_var.get()
    stream_url = get_stream_url(selected_station)
    
    if stream_url:
        play_stream(stream_url)

# Function to retrieve the stream URL for a selected station
def get_stream_url(station_name):
    for station in radio_stations:
        if station['name'] == station_name:
            return station['url']
    return None

# Function to play the stream
def play_stream(stream_url):
    player = vlc.MediaPlayer(stream_url)
    player.play()
    players.append(player)

# Function to stop playing all streams
def stop_all_streams():
    for player in players:
        player.stop()
    players.clear()

# Create the main window
window = tk.Tk()
window.title("Radio Player")

# Create the GUI elements
station_label = tk.Label(window, text="Select a radio station:")
station_label.pack()

station_names = [station['name'] for station in radio_stations]
station_var = tk.StringVar(window)
station_var.set(station_names[0])  # Set the default station

station_dropdown = tk.OptionMenu(window, station_var, *station_names)
station_dropdown.pack()

play_button = tk.Button(window, text="Play", command=select_station)
play_button.pack()

stop_button = tk.Button(window, text="Stop All", command=stop_all_streams)
stop_button.pack()

# Start the main event loop
window.mainloop()
