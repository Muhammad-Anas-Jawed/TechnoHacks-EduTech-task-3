import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        unit = temperature_unit.get()

        if unit == "Fahrenheit":
            converted_temperature = (temperature - 32) * 5/9
            result.set(f"{temperature}°F is equal to {converted_temperature:.2f}°C")
        elif unit == "Celsius":
            converted_temperature = (temperature * 9/5) + 32
            result.set(f"{temperature}°C is equal to {converted_temperature:.2f}°F")
    except Exception as e:
        result.set("Invalid input")

root = tk.Tk()
root.title("Temperature Converter")

temperature_label = tk.Label(root, text="Enter Temperature:")
temperature_label.grid(row=0, column=0)
entry_temperature = tk.Entry(root)
entry_temperature.grid(row=0, column=1)

temperature_unit_label = tk.Label(root, text="Select Unit:")
temperature_unit_label.grid(row=1, column=0)
temperature_unit = tk.StringVar()
temperature_unit.set("Fahrenheit")
unit_menu = tk.OptionMenu(root, temperature_unit, "Fahrenheit", "Celsius")
unit_menu.grid(row=1, column=1)

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
