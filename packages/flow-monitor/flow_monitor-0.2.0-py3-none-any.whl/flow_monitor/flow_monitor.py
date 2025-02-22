import tkinter as tk
from tkinter import ttk
import time
import threading
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import serial
import struct
import numpy as np
import signal
import sys

# ------------------------------
# Serial Configuration
COM_PORT = "COM6"  # Replace with your serial port
BAUD = 9600
METROLOGY_FRAME_LENGTH = 29
HEADER = b'\x0C\x0C'

incomingData = {
    'calibratedFlowrate': 0,
    'avgFlowRate': 0,
    'forwardTotalVolume': 0,
    'reverseTotalVolume': 0,
    'forwardFlowTime': 0,
    'reverseFlowTime': 0,
}

# ------------------------------
# Global Data Lists (Full History)
timestamps = []         # Formatted time strings for x-axis labels
calibrated_flow = []    # Calibrated flow rate (L/s)
avg_flow = []           # Average flow rate (L/s)
forward_volume = []     # Forward volume (converted to liters)

# Global variable to control the number of points shown in the graph.
window_size = 100  # Default value

# Global index tracker for table updates
table_last_index = 0

# Global variable to store the "after" callback ID for the table update.
table_update_after_id = None

# Create a stop event for the serial thread.
stop_event = threading.Event()

# Global variable to store the serial thread.
serial_thread = None

# ------------------------------
def parse_frame(meas_data):
    """Parse a single frame and return a timestamp and a copy of the parsed data."""
    i = 0
    for key in incomingData:
        data_in_bytes = meas_data[i + 2: i + 6]
        incomingData[key] = struct.unpack('<f', data_in_bytes)[0]
        i += 4
    timestamp = round(time.time() * 1000)  # Milliseconds timestamp
    return timestamp, incomingData.copy()

def synchronize_stream(port):
    """Wait until the header is found."""
    while not stop_event.is_set():
        byte = port.read(1)
        if byte == HEADER[0:1]:
            second_byte = port.read(1)
            if second_byte == HEADER[1:2]:
                return
    # Return if stop_event was set.
    return

def read_serial_data():
    """Continuously read serial data and update global lists."""
    try:
        with serial.Serial(COM_PORT, baudrate=BAUD, timeout=0.1) as port:
            print(f"Listening on {COM_PORT} at {BAUD} baud...")
            while not stop_event.is_set():
                synchronize_stream(port)
                if stop_event.is_set():
                    break
                meas_data = port.read(METROLOGY_FRAME_LENGTH - 2)  # Exclude header bytes
                if len(meas_data) == METROLOGY_FRAME_LENGTH - 2:
                    full_frame = HEADER + meas_data  # Reattach header
                    timestamp, parsed_data = parse_frame(full_frame)
                    # For debugging:
                    print(timestamp, parsed_data)
                    update_plot(parsed_data, timestamp)
                time.sleep(0.1)
    except serial.SerialException as e:
        print(f"Serial port error: {e}")
    except struct.error as e:
        print(f"Data parsing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def update_plot(data, timestamp):
    """Append new data to the history lists and log the raw JSON (dictionary)
    along with the timestamp to a file."""
    # Format the time for the graph
    formatted_time = datetime.datetime.fromtimestamp(timestamp / 1000).strftime('%H:%M:%S')
    timestamps.append(formatted_time)
    calibrated_flow.append(data["calibratedFlowrate"])
    avg_flow.append(data["avgFlowRate"])
    forward_volume.append(data["forwardTotalVolume"] * 1000)  # Convert m³ to liters

    # Log the raw data as received (timestamp and dictionary) to a text file.
    # This will create (or append to) a file called "data_log.txt"
    year_datetime = datetime.datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
    with open("data_log_raw.txt", "a") as log_file:
        # Write exactly as received; for example:
        log_file.write(f"{year_datetime} {data}\n")


def calculate_statistics():
    """Calculate statistics for forward_volume."""
    if not forward_volume:
        return 0, 0, 0, 0
    arr = np.array(forward_volume)
    return np.min(arr), np.max(arr), np.mean(arr), np.std(arr)

# ------------------------------
# Persistent line objects for the graph
line1 = None
line2 = None
line3 = None

def animate(i):
    """Update the graph without clearing the axes."""
    global line1, line2, line3, window_size
    if len(timestamps) < 2:
        return  # Not enough data

    x = list(range(len(timestamps)))  # Numeric x-axis (data point indices)

    if line1 is None:
        # Create persistent step plots with markers and picker enabled.
        line1, = ax1.step(x, calibrated_flow, label="Calibrated Flowrate (L/s)",
                          where='post', marker='o', color='b', picker=5)
        line2, = ax1.step(x, avg_flow, label="Avg Flow Rate (L/s)",
                          where='post', marker='o', color='r', linestyle='dashed', picker=5)
        line3, = ax2.step(x, forward_volume, label="Forward Volume (L)",
                          where='post', marker='o', color='g', picker=5)
        ax1.set_ylabel("Flowrate (L/s)")
        ax2.set_ylabel("Volume (L)")
        ax2.set_xlabel("Time (HH:MM:SS)")
        ax1.set_title("Real-Time Flow Data (Graph)")
        ax1.legend()
        ax2.legend()
    else:
        # Update the line data.
        line1.set_data(x, calibrated_flow)
        line2.set_data(x, avg_flow)
        line3.set_data(x, forward_volume)

    # Update x-ticks with time labels.
    tick_step = max(1, len(x) // 10)
    tick_positions = list(range(0, len(x), tick_step))
    ax1.set_xticks(tick_positions)
    ax1.set_xticklabels([timestamps[i] for i in tick_positions], rotation=45)
    ax2.set_xticks(tick_positions)
    ax2.set_xticklabels([timestamps[i] for i in tick_positions], rotation=45)

    # Auto-scroll: show last `window_size` points.
    new_right = len(x) - 1
    new_left = max(0, new_right - window_size + 1)
    ax1.set_xlim(new_left, new_right)
    ax2.set_xlim(new_left, new_right)

    # Adjust y-limits based on visible data.
    if calibrated_flow and avg_flow:
        y1min = min(min(calibrated_flow[new_left:new_right+1]), min(avg_flow[new_left:new_right+1]))
        y1max = max(max(calibrated_flow[new_left:new_right+1]), max(avg_flow[new_left:new_right+1]))
        margin1 = (y1max - y1min) * 0.1 if y1max != y1min else 1
        ax1.set_ylim(y1min - margin1, y1max + margin1)
    if forward_volume:
        y2min = min(forward_volume[new_left:new_right+1])
        y2max = max(forward_volume[new_left:new_right+1])
        margin2 = (y2max - y2min) * 0.1 if y2max != y2min else 1
        ax2.set_ylim(y2min - margin2, y2max + margin2)

    canvas.draw_idle()

    # Update statistics label.
    min_v, max_v, avg_v, std_v = calculate_statistics()
    stats_label.config(text=f"📊 Min: {min_v:.2f} L | Max: {max_v:.2f} L | Avg: {avg_v:.2f} L | Std Dev: {std_v:.2f} L")

# ------------------------------
# Hover functionality.
def on_hover(event):
    """Display an annotation for the nearest data point when hovering."""
    if event.inaxes == ax1:
        if event.xdata is None:
            annot1.set_visible(False)
            canvas.draw_idle()
            return
        index = int(round(event.xdata))
        if index < 0 or index >= len(timestamps):
            annot1.set_visible(False)
            canvas.draw_idle()
            return
        time_str = timestamps[index]
        val1 = calibrated_flow[index]
        val2 = avg_flow[index]
        annot1.xy = (index, max(val1, val2))
        annot1.set_text(f"Time: {time_str}\nCalib: {val1:.2f}\nAvg: {val2:.2f}")
        annot1.set_visible(True)
        canvas.draw_idle()
    elif event.inaxes == ax2:
        if event.xdata is None:
            annot2.set_visible(False)
            canvas.draw_idle()
            return
        index = int(round(event.xdata))
        if index < 0 or index >= len(timestamps):
            annot2.set_visible(False)
            canvas.draw_idle()
            return
        time_str = timestamps[index]
        val = forward_volume[index]
        annot2.xy = (index, val)
        annot2.set_text(f"Time: {time_str}\nVolume: {val:.2f}")
        annot2.set_visible(True)
        canvas.draw_idle()
    else:
        if annot1.get_visible() or annot2.get_visible():
            annot1.set_visible(False)
            annot2.set_visible(False)
            canvas.draw_idle()

# ------------------------------
def update_table():
    """Update the data table in the 'Data Table' tab with new rows,
       write all new rows to a text file, and keep only the latest 100 rows in the table."""
    global table_last_index, table_update_after_id

    new_rows = []  # To collect new rows for writing to file
    # Insert new rows into the table and collect them for logging.
    for i in range(table_last_index, len(timestamps)):
        row_values = (
            timestamps[i],
            f"{calibrated_flow[i]:.2f}",
            f"{avg_flow[i]:.2f}",
            f"{forward_volume[i]:.2f}"
        )
        tree.insert("", "end", values=row_values)
        new_rows.append(row_values)
    
    # Append the new rows to the text file.
    if new_rows:
        with open("data_log.txt", "a") as f:
            for row in new_rows:
                # Join the row values with commas (CSV format) and add a newline.
                f.write(",".join(row) + "\n")
    
    # Update the global index so we don't insert duplicate rows.
    table_last_index = len(timestamps)
    
    # Keep only the latest 100 rows in the treeview.
    children = tree.get_children()
    if len(children) > 100:
        # Delete extra rows from the beginning.
        for child in children[:-100]:
            tree.delete(child)
    
    # Schedule the next update.
    table_update_after_id = root.after(1000, update_table)


# ------------------------------
def start_serial_reading():
    """Start serial data reading in a background thread."""
    global serial_thread
    serial_thread = threading.Thread(target=read_serial_data, daemon=True)
    serial_thread.start()

# ------------------------------
# GUI Setup using Notebook for tabs.
root = tk.Tk()
root.title("Real-Time Flow Data Monitor")
root.geometry("1100x700")

def on_closing():
    """Cleanup and exit the application."""
    print("Closing application...")
    stop_event.set()                  # Signal the serial thread to stop
    try:
        ani.event_source.stop()       # Stop the animation event source
    except Exception as e:
        print("Error stopping animation:", e)
    if table_update_after_id is not None:
        try:
            root.after_cancel(table_update_after_id)  # Cancel table update callback
        except Exception as e:
            print("Error cancelling table update:", e)
    root.destroy()
    sys.exit(0)

# Bind Ctrl+C (SIGINT) to call on_closing.
signal.signal(signal.SIGINT, lambda s, f: on_closing())

root.protocol("WM_DELETE_WINDOW", on_closing)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Tab 1: Graph Tab
tab_graph = ttk.Frame(notebook)
notebook.add(tab_graph, text="Flow Rate Graph")

# Tab 2: Data Table Tab
tab_table = ttk.Frame(notebook)
notebook.add(tab_table, text="Data Table")

# ------------------------------
# --- Graph Tab Setup ---
graph_frame = ttk.Frame(tab_graph)
graph_frame.pack(fill="both", expand=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), dpi=100)
fig.tight_layout(pad=3.0)

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

toolbar_frame = ttk.Frame(tab_graph)
toolbar_frame.pack(fill="x")
toolbar_label = ttk.Label(toolbar_frame, text="🔍 Use mouse scroll & drag to pan/zoom", font=("Arial", 10))
toolbar_label.pack(side="left", padx=5, pady=5)

# --- Configurable Window Size ---
config_frame = ttk.Frame(tab_graph)
config_frame.pack(fill="x", padx=5, pady=5)
points_label = ttk.Label(config_frame, text="Points Shown:")
points_label.pack(side="left", padx=(0, 5))

window_size_spinbox = tk.Spinbox(config_frame, from_=10, to=1000, increment=10, width=5)
window_size_spinbox.pack(side="left")

def update_window_size(event=None):
    global window_size
    try:
        window_size = int(window_size_spinbox.get())
    except ValueError:
        pass

window_size_spinbox.config(command=update_window_size)
window_size_spinbox.bind("<Return>", update_window_size)

stats_label = ttk.Label(tab_graph, text="📊 Min: -- L | Max: -- L | Avg: -- L | Std Dev: -- L", font=("Arial", 12))
stats_label.pack(side=tk.BOTTOM, pady=10)

annot1 = ax1.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                      bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
annot1.set_visible(False)
annot2 = ax2.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                      bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
annot2.set_visible(False)

canvas.mpl_connect("motion_notify_event", on_hover)

# ------------------------------
# --- Data Table Tab Setup ---
tree = ttk.Treeview(tab_table, columns=("Time", "Calibrated", "Avg", "Volume"), show="headings", height=25)
tree.heading("Time", text="Time")
tree.heading("Calibrated", text="Calibrated Flowrate (L/s)")
tree.heading("Avg", text="Avg Flow Rate (L/s)")
tree.heading("Volume", text="Forward Volume (L)")
tree.column("Time", width=100, anchor="center")
tree.column("Calibrated", width=150, anchor="center")
tree.column("Avg", width=150, anchor="center")
tree.column("Volume", width=150, anchor="center")
tree.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(tab_table, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# ------------------------------
ani = animation.FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
update_table()          # Start periodic table updates.
start_serial_reading()  # Start reading serial data.

root.mainloop()
