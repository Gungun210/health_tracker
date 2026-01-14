import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
from datetime import datetime

CSV_FILE = "health_data.csv"

def calculate_bmi(weight, height):
    try:
        height_m = float(height) / 100
        weight_kg = float(weight)
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 2)
    except (ZeroDivisionError, ValueError):
        return None

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Name", "Age", "Gender", "Height", "Weight", "BMI", "Symptoms"])
        writer.writerow(data)

def submit_info():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    height = entry_height.get()
    weight = entry_weight.get()
    symptoms = entry_symptoms.get()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    if not (name and age and gender and height and weight):
        messagebox.showerror("Input Error", "Please fill out all required fields.")
        return

    bmi = calculate_bmi(weight, height)
    if bmi is None:
        messagebox.showerror("Calculation Error", "Invalid height or weight.")
        return

    data = [date, name, age, gender, height, weight, bmi, symptoms]
    save_to_csv(data)

    output = f"Data saved!\nName: {name}\nAge: {age}\nGender: {gender}\nBMI: {bmi}"
    output_label.config(text=output)

# GUI Setup
root = tk.Tk()
root.title("Health Tracker")
root.geometry("400x600")

tab_control = ttk.Notebook(root)

# Tab 1: Data Entry
entry_tab = ttk.Frame(tab_control)
tab_control.add(entry_tab, text="Enter Health Info")

tk.Label(entry_tab, text="Name:").pack()
entry_name = tk.Entry(entry_tab)
entry_name.pack()

tk.Label(entry_tab, text="Age:").pack()
entry_age = tk.Entry(entry_tab)
entry_age.pack()

tk.Label(entry_tab, text="Gender:").pack()
gender_var = tk.StringVar()
gender_menu = tk.OptionMenu(entry_tab, gender_var, "Male", "Female", "Other")
gender_menu.pack()

tk.Label(entry_tab, text="Height (cm):").pack()
entry_height = tk.Entry(entry_tab)
entry_height.pack()

tk.Label(entry_tab, text="Weight (kg):").pack()
entry_weight = tk.Entry(entry_tab)
entry_weight.pack()

tk.Label(entry_tab, text="Symptoms:").pack()
entry_symptoms = tk.Entry(entry_tab)
entry_symptoms.pack()

tk.Button(entry_tab, text="Submit", command=submit_info, bg="green", fg="white").pack(pady=10)
output_label = tk.Label(entry_tab, text="", justify="left")
output_label.pack(pady=10)

# Tab 2: Graph - Coming next
graph_tab = ttk.Frame(tab_control)
tab_control.add(graph_tab, text="View BMI Chart")

tab_control.pack(expand=1, fill="both")


root.mainloop()
