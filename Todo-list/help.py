import os
import tkinter as tk
from tkinter import messagebox
from datetime import date

# Custom dialog box for entering priority
class PriorityDialog(tk.Toplevel):
    def __init__(self, parent, items):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        self.title("Priority")
        self.geometry("200x100")
        self.transient(parent)
        self.grab_set()

        self.items = items
        self.priority_label = tk.Label(self, text="Enter the priority number:")
        self.priority_label.pack(pady=5)

        self.priority_entry = tk.Entry(self, width=10)
        self.priority_entry.pack(pady=5)

        self.ok_button = tk.Button(self, text="OK", command=self.ok)
        self.ok_button.pack(pady=5)
        
        self.priority = None
        
        self.protocol("WM_DELETE_WINDOW", self.cancel)

    def ok(self):
        priority = self.priority_entry.get()
        if priority.isdigit() and int(priority) > 0 and int(priority) <= len(self.items):
            self.priority = self.items[int(priority)-1]
            self.destroy()
        else:
            messagebox.showwarning("Priority", "Invalid priority number. Please try again.")

    def cancel(self):
        self.priority = None
        self.destroy()

# Function to handle "Finish" button click
def finish():
    # Open the priority dialog
    priority_dialog = PriorityDialog(root, action_items)
    root.wait_window(priority_dialog)
    
    # Get the priority from the dialog
    priority = priority_dialog.priority
    
    # If the user entered a priority, create a text file and write the action items with their priorities
    if priority is not None:
        desktop_path = os.path.expanduser("~/Desktop")  # Get the path to the desktop
        file_path = os.path.join(desktop_path, "todo_list.txt")  # Set the file path on the desktop
        
        today = date.today().strftime("%B %d, %Y")  # Get the current date
        
        with open(file_path, "w") as file:
            file.write(f"Today's to-do list - {today}\n")
            file.write(f"Priority - {priority}\n")
            file.write("-----\n")
            file.write("Important items:\n")
            for i, item in enumerate(action_items):
                file.write(f"{i+1}. {item}\n")
        
        messagebox.showinfo("Finish", "To-do list saved successfully!")
    else:
        messagebox.showwarning("Priority", "Priority not entered. Please try again.")

# Function to handle "Add" button click or pressing ENTER key
def add(event=None):
    # Get the entered action item from the text box
    action = entry.get()

    # If the user pressed ENTER or typed "finish", prompt for the priority and end the program
    if event is None or event.keysym == "Escape":
        finish()
        root.destroy()
        return

    # Add the action item to the list
    action_items.append(action)

    # Clear the text box
    entry.delete(0, tk.END)

    # Update the display box
    display_box.insert(tk.END, f"Action: {action}\n")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an empty list to store the action items
action_items = []

# Create a label to display instructions
label = tk.Label(root, text="Enter your daily action items.\nPress Enter to add an item.\nPress Escape to finish.")
label.pack(pady=10)

# Create a text box for entering action items
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.focus_set()

# Bind the Enter key press event to the add function
root.bind("<Return>", add)

# Bind the Escape key press event to the add function
root.bind("<Escape>", add)

# Create a display box to show the added items
display_box = tk.Text(root, height=10, width=40)
display_box.pack(pady=5)

# Start the main loop
root.mainloop()
