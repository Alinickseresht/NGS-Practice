
import tkinter as tk
from tkinter import messagebox


def calculate_fold_change():
    try:
        sample_target = float(entry_sample_target.get())
        sample_reference = float(entry_sample_reference.get())

        control_target = float(entry_control_target.get())
        control_reference = float(entry_control_reference.get())

        # ΔCt calculations
        sample_delta_ct = sample_target - sample_reference
        control_delta_ct = control_target - control_reference

        # ΔΔCt
        delta_delta_ct = sample_delta_ct - control_delta_ct

        # Fold Change
        fold_change = 2 ** (-delta_delta_ct)

        result_text.set(
            f"Sample ΔCt: {round(sample_delta_ct, 3)}\n"
            f"Control ΔCt: {round(control_delta_ct, 3)}\n"
            f"ΔΔCt: {round(delta_delta_ct, 3)}\n"
            f"Fold Change: {round(fold_change, 3)}"
        )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numeric Ct values."
        )


# Main Window
root = tk.Tk()
root.title("qPCR ΔΔCt Calculator")
root.geometry("420x400")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="qPCR Fold Change Calculator",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

# Labels and Entries
labels = [
    "Sample Target Ct",
    "Sample Reference Ct",
    "Control Target Ct",
    "Control Reference Ct"
]

entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(frame, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

    entry = tk.Entry(frame, width=20)
    entry.grid(row=i, column=1, padx=10, pady=5)

    entries.append(entry)

(
    entry_sample_target,
    entry_sample_reference,
    entry_control_target,
    entry_control_reference
) = entries

# Calculate Button
calculate_button = tk.Button(
    root,
    text="Calculate Fold Change",
    command=calculate_fold_change,
    width=25,
    height=2
)
calculate_button.pack(pady=15)

# Result
result_text = tk.StringVar()

result_label = tk.Label(
    root,
    textvariable=result_text,
    font=("Arial", 11),
    justify="left"
)
result_label.pack(pady=10)

# Run App
root.mainloop()
