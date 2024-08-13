# Name: Georgia Vrana
# Date Submitted: Tuesday, April 23rd, 2024
# Assignment-13: Temperature
# Description: This Python program features a graphical user interface for converting temperatures between 
#              Fahrenheit and Celsius, providing separate input fields and buttons for each conversion direction,
#              and displaying the results immediately below the respective inputs.

import tkinter as tk

def convert_to_celsius():
    # Retrieve value from the Fahrenheit entry box and convert to float
    fahrenheit = float(fahrenheit_entry.get())
    # Convert the Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5/9
    # Update the Celsius result label to show the result rounded to two decimal places
    celsius_result_label.config(text=f"The temperature is {celsius:.2f} Celsius")

def convert_to_fahrenheit():
    # Retrieve value from the Celsius entry box and convert to float
    celsius = float(celsius_entry.get())
    # Convert the Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    # Update the Fahrenheit result label to show the result rounded to two decimal places
    fahrenheit_result_label.config(text=f"The temperature is {fahrenheit:.2f} Fahrenheit")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create the entry and button for Fahrenheit to Celsius conversion
fahrenheit_entry = tk.Entry(root, width=10)
fahrenheit_entry.pack(pady=5)
fahrenheit_to_c_button = tk.Button(root, text="Convert to Celsius", command=convert_to_celsius)
fahrenheit_to_c_button.pack()

# Label to display the Celsius result
celsius_result_label = tk.Label(root, text="Enter a temperature in Fahrenheit and convert.")
celsius_result_label.pack(pady=5)

# Separator line
separator = tk.Label(root, text="------------------------------------------")
separator.pack()

# Create the entry and button for Celsius to Fahrenheit conversion
celsius_entry = tk.Entry(root, width=10)
celsius_entry.pack(pady=5)
celsius_to_f_button = tk.Button(root, text="Convert to Fahrenheit", command=convert_to_fahrenheit)
celsius_to_f_button.pack()

# Label to display the Fahrenheit result
fahrenheit_result_label = tk.Label(root, text="Enter a temperature in Celsius and convert.")
fahrenheit_result_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()

