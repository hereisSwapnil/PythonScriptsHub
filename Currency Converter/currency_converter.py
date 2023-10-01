import tkinter as tk
from forex_python.converter import CurrencyRates

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()
    
    currency_converter = CurrencyRates()
    converted_amount = currency_converter.convert(from_currency, to_currency, amount)
    
    result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
root = tk.Tk()
root.title("Currency Converter")
currencies = [
    'USD',  # United States Dollar
    'EUR',  # Euro
    'GBP',  # British Pound Sterling
    'JPY',  # Japanese Yen
    'AUD',  # Australian Dollar
    'CAD',  # Canadian Dollar
    'CHF',  # Swiss Franc
    'CNY',  # Chinese Yuan
    'INR',  # Indian Rupee
    'SGD',  # Singapore Dollar
    'MYR',  # Malaysian Ringgit
    'NZD',  # New Zealand Dollar
    'ZAR',  # South African Rand
    'BRL',  # Brazilian Real
    'RUB',  # Russian Ruble
    'TRY',  # Turkish Lira
    'AED',  # United Arab Emirates Dirham
    'SAR',  # Saudi Riyal
    'MXN',  # Mexican Peso
    'IDR',  # Indonesian Rupiah
]
label_amount = tk.Label(root, text="Enter Amount:")
label_amount.grid(row=0, column=0, pady=10)

entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

label_from_currency = tk.Label(root, text="From Currency:")
label_from_currency.grid(row=1, column=0, pady=10)

combo_from_currency = tk.StringVar()
combo_from_currency.set(currencies[0])
from_currency_menu = tk.OptionMenu(root, combo_from_currency, *currencies)
from_currency_menu.grid(row=1, column=1, padx=10)

label_to_currency = tk.Label(root, text="To Currency:")
label_to_currency.grid(row=1, column=2)

combo_to_currency = tk.StringVar()
combo_to_currency.set(currencies[1])
to_currency_menu = tk.OptionMenu(root, combo_to_currency, *currencies)
to_currency_menu.grid(row=1, column=3, padx=10)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=2, column=0, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=3, column=0, columnspan=4, padx=10)

root.mainloop()
