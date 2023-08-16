import tkinter as tk

def convert_temperature():
    try:
        input_temp = float(entry.get())
        if from_unit.get() == "Celsius":
            if to_unit.get() == "Fahrenheit":
                result.set(f"{input_temp * 9/5 + 32:.2f} °F")
            elif to_unit.get() == "Kelvin":
                result.set(f"{input_temp + 273.15:.2f} K")
            else:
                result.set("Invalid conversion")
        elif from_unit.get() == "Fahrenheit":
            if to_unit.get() == "Celsius":
                result.set(f"{(input_temp - 32) * 5/9:.2f} °C")
            elif to_unit.get() == "Kelvin":
                result.set(f"{(input_temp - 32) * 5/9 + 273.15:.2f} K")
            else:
                result.set("Invalid conversion")
        elif from_unit.get() == "Kelvin":
            if to_unit.get() == "Celsius":
                result.set(f"{input_temp - 273.15:.2f} °C")
            elif to_unit.get() == "Fahrenheit":
                result.set(f"{(input_temp - 273.15) * 9/5 + 32:.2f} °F")
            else:
                result.set("Invalid conversion")
        else:
            result.set("Invalid unit")
    except ValueError:
        result.set("Invalid input")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry('300x300')
input_label = tk.Label(root, text="Enter Temperature:")
input_label.pack()

entry = tk.Entry(root)
entry.pack()

from_unit = tk.StringVar()
from_unit.set("Celsius")

from_dropdown = tk.OptionMenu(root, from_unit, "Celsius", "Fahrenheit", "Kelvin")
from_dropdown.pack()

to_unit = tk.StringVar()
to_unit.set("Celsius")

to_dropdown = tk.OptionMenu(root, to_unit, "Celsius", "Fahrenheit", "Kelvin")
to_dropdown.pack()

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()
