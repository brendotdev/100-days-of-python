from tkinter import *

# ---------------------------- WINDOW SETUP ------------------------------- #
window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=30, pady=30, bg="#f2f2f2")  # Light gray background
window.resizable(False, False)

# ---------------------------- FONT SETUP -------------------------------- #
LABEL_FONT = ("Arial", 12, "bold")
OUTPUT_FONT = ("Arial", 14, "normal")
BUTTON_FONT = ("Arial", 12)

# ---------------------------- CONVERSION FUNCTION ------------------------ #
def convert_miles_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.60934, 2)
        km_output_label.config(text=f"{km}")
    except ValueError:
        km_output_label.config(text="Invalid input")

# ---------------------------- WIDGETS ------------------------------------ #

# Entry for miles
miles_input = Entry(width=10, font=OUTPUT_FONT, justify="center")
miles_input.grid(column=1, row=0)
miles_input.focus()

# Miles label
miles_label = Label(text="Miles", font=LABEL_FONT, bg="#f2f2f2", fg="#333")
miles_label.grid(column=2, row=0)

# "is equal to" label
equal_label = Label(text="is equal to", font=LABEL_FONT, bg="#f2f2f2", fg="#333")
equal_label.grid(column=0, row=1)

# Output label (km result)
km_output_label = Label(text="0", font=OUTPUT_FONT, bg="#f2f2f2", fg="#007acc")
km_output_label.grid(column=1, row=1)

# Km label
km_label = Label(text="Km", font=LABEL_FONT, bg="#f2f2f2", fg="#333")
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", font=BUTTON_FONT, command=convert_miles_to_km)
calculate_button.grid(column=1, row=2, pady=10)

# Optional: set window icon (must be .ico on Windows)
# window.iconbitmap("miles_to_km.ico")

# Keep window open
window.mainloop()
