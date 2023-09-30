import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry.get())
        if var.get() == 1:  # Fahrenheit to Celsius
            result.set((temperature - 32) * 5/9)
        elif var.get() == 2:  # Celsius to Fahrenheit
            result.set((temperature * 9/5) + 32)
    except ValueError:
        result.set("Invalid input")

def on_validate_input(P):
    if P == "" or P.isdigit() or P[0] == "-":
        return True
    else:
        return False
    

root = tk.Tk()
root.title("Temperature Converter")

var = tk.IntVar()

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Enter Temperature:")
label.grid(row=0, column=0)

validate_input = root.register(on_validate_input)
entry = tk.Entry(frame, validate="key", validatecommand=(validate_input, "%P"))
entry.grid(row=0, column=1)


radio_fahrenheit = tk.Radiobutton(frame, text="Fahrenheit to Celsius", variable=var, value=1)
radio_fahrenheit.grid(row=1, column=0, padx=10)

radio_celsius = tk.Radiobutton(frame, text="Celsius to Fahrenheit", variable=var, value=2)
radio_celsius.grid(row=1, column=1, padx=10)

convert_button = tk.Button(frame, text="Convert", command=convert_temperature)
convert_button.grid(row=2, columnspan=2, pady=10)

result = tk.StringVar()
result.set("")
output_label = tk.Label(frame, textvariable=result)
output_label.grid(row=3, columnspan=2)

root.mainloop()
