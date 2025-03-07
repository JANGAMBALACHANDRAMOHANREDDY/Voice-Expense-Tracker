import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Initialize the main window
root = tk.Tk()
root.title("Voice-Based Expense Tracker")
root.geometry("400x300")

# Dictionary to store expenses
expenses = {}

# Function to add expenses
def add_expense(command):
    try:
        parts = command.split()
        amount = int(parts[1])
        category = parts[2].lower()
        
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        
        output_label.config(text=f"Added expense: ₹{amount} for {category}")
    except (IndexError, ValueError):
        output_label.config(text="Invalid format! Use: Add 500 food")

# Function to show the expense report
def show_report():
    if not expenses:
        messagebox.showinfo("Report", "No expenses to show.")
        return
    
    report = "\n".join([f"{cat}: ₹{amt}" for cat, amt in expenses.items()])
    total = sum(expenses.values())
    report += f"\nTotal: ₹{total}"
    
    output_label.config(text=f"Expense Report:\n{report}")
    
    # Pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Expense Report")
    plt.show()

# Function to process user input
def process_input():
    user_input = input_entry.get().lower()
    if user_input.startswith("add"):
        add_expense(user_input)
    elif user_input == "show report":
        show_report()
    elif user_input == "exit":
        root.quit()
    else:
        output_label.config(text="Command not recognized.")

# UI Components
input_label = tk.Label(root, text="Say something (e.g., 'Add 500 food' or 'Show report'):")
input_label.pack(pady=10)

input_entry = tk.Entry(root, width=30)
input_entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=process_input)
submit_button.pack(pady=5)

output_label = tk.Label(root, text="", wraplength=300)
output_label.pack(pady=10)

# Run the main loop
root.mainloop()
