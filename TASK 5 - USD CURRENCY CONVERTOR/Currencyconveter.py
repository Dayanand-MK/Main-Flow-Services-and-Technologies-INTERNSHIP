import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
from PIL import ImageTk, Image

def convert_currency():
    amount = float(entry.get())
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()

    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
    data = response.json()

    conversion_rate = data['rates'][target_currency]
    converted_amount = amount * conversion_rate

    result_label.config(text=str(converted_amount))

window = tk.Tk()
window.geometry("600x270")
window.title("Currency Converter")
window.iconbitmap("E:\\internship\Main flow - python\\TASKS\\TASK 5 - USD CURRENCY CONVERTER APPLICATION\\icon.ico")
window.maxsize(300,270)
window.minsize(400,270)

image = Image.open('E:\\internship\\Main flow - python\\TASKS\\TASK 5 - USD CURRENCY CONVERTER APPLICATION\\currency.png')
zoom = 0.5

pix,piy = tuple([int(zoom * x) for x in image.size])

img = ImageTk.PhotoImage(image.resize((pix,piy)))
panel = Label(window, image = img)
panel.place(x = 190, y = 35)

l1 = Label(window,text = "USD Currency Convertrt", font= ('times','10','bold'))
l1.place(x=150,y=15)

label1 = tk.Label(window, text="Amount:", font = ('roboto',10,'bold'))
label1.place(x=20,y=15)

entry = tk.Entry(window,width = 20,borderwidth = 1,font = ('roboto',10,"bold"))
entry.place(x=20,y=60)


label2 = tk.Label(window, text="Base Currency:")
label2.place(x=300,y=40)

base_currency_var = tk.StringVar(window)
base_currency_var.set("USD")  # Default base currency

base_currency_dropdown = tk.OptionMenu(window, base_currency_var, "USD", "EUR", "GBP", "INR")
base_currency_dropdown.place(x=300,y=70)

label3 = tk.Label(window, text="Target Currency:")
label3.place(x=300,y=120)

target_currency_var = tk.StringVar(window)
target_currency_var.set("EUR")  # Default target currency

target_currency_dropdown = tk.OptionMenu(window, target_currency_var, "USD", "EUR", "GBP", "INR")
target_currency_dropdown.place(x=300,y=150)

label4 = tk.Label(window, text="Converted Amount:")
label4.place(x=100,y=120)

result_label = tk.Label(window, text="")
result_label.place(x=150,y=160)

button = tk.Button(window, text="Convert", command=convert_currency)
button.place(x=150,y=200)

window.mainloop()