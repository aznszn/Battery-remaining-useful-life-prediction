import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import joblib

def calculate_RUL():
    try:
        F1 = float(entry_discharge_time.get())
        F2 = float(entry_decrement_36_34V.get())
        F3 = float(entry_max_voltage_discharge.get())
        F4 = float(entry_min_voltage_charge.get())
        F5 = float(entry_time_at_415V.get())
        F6 = float(entry_time_constant_current.get())
        F7 = float(entry_charging_time.get())

        model = joblib.load("model.sav")
        scaler = joblib.load("scaler.pkl")

        input_data = [[F1, F2, F3, F4, F5, F6, F7]]
        scaler.transform(input_data)
        prediction = model.predict(input_data)

        label_RUL.config(text=f"Remaining Useful Life: {prediction[0]:.2f} hours")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for all fields.")

root = ThemedTk(theme='arc')
root.title("Battery RUL Estimation")
root.geometry("500x500")  # Set a reasonable size for the window

style = ttk.Style()
style.configure("TLabel", padding=10, font=("Helvetica", 12))
style.configure("TEntry", padding=10, font=("Helvetica", 12))
style.configure("TButton", padding=10, font=("Helvetica", 12))

frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

label_discharge_time = ttk.Label(frame, text="Discharge Time (s)")
label_discharge_time.grid(row=0, column=0, sticky="w")
entry_discharge_time = ttk.Entry(frame)
entry_discharge_time.grid(row=0, column=1)

label_decrement_36_34V = ttk.Label(frame, text="Decrement 3.6-3.4V (s)")
label_decrement_36_34V.grid(row=1, column=0, sticky="w")
entry_decrement_36_34V = ttk.Entry(frame)
entry_decrement_36_34V.grid(row=1, column=1)

label_max_voltage_discharge = ttk.Label(frame, text="Max. Voltage Discharge (V)")
label_max_voltage_discharge.grid(row=2, column=0, sticky="w")
entry_max_voltage_discharge = ttk.Entry(frame)
entry_max_voltage_discharge.grid(row=2, column=1)

label_min_voltage_charge = ttk.Label(frame, text="Min. Voltage Charge (V)")
label_min_voltage_charge.grid(row=3, column=0, sticky="w")
entry_min_voltage_charge = ttk.Entry(frame)
entry_min_voltage_charge.grid(row=3, column=1)

label_time_at_415V = ttk.Label(frame, text="Time at 4.15V (s)")
label_time_at_415V.grid(row=4, column=0, sticky="w")
entry_time_at_415V = ttk.Entry(frame)
entry_time_at_415V.grid(row=4, column=1)

label_time_constant_current = ttk.Label(frame, text="Time Constant Current (s)")
label_time_constant_current.grid(row=5, column=0, sticky="w")
entry_time_constant_current = ttk.Entry(frame)
entry_time_constant_current.grid(row=5, column=1)

label_charging_time = ttk.Label(frame, text="Charging Time (s)")
label_charging_time.grid(row=6, column=0, sticky="w")
entry_charging_time = ttk.Entry(frame)
entry_charging_time.grid(row=6, column=1)

calculate_button = ttk.Button(frame, text="Calculate RUL", command=calculate_RUL)
calculate_button.grid(row=7, column=0, columnspan=2, pady=20)

label_RUL = ttk.Label(frame, text="Remaining Useful Life: N/A", font=("Helvetica", 14))
label_RUL.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
