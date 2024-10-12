from tkinter import *

window = Tk()
window.geometry('800x100')
window.title('Currency converter')


def from_kg():
    pound = float(input_value.get()) * 0.76
    peso = float(input_value.get()) * 19.30
    euro = float(input_value.get()) * 0.91

    poundconversion.delete('1.0', END)
    poundconversion.insert(END, pound)

    pesoconversion.delete('1.0', END)
    pesoconversion.insert(END, peso)

    euroconversion.delete('1.0', END)
    euroconversion.insert(END, euro)

dollarstring = Label(window, text = 'Dollars: ')
input_value = StringVar()
dollarinputstring = Entry(window, textvariable = input_value)
poundreturn = Label(window, text = 'Pounds:')
pesoreturn = Label(window, text = 'Pesos: ')
euroreturn = Label(window, text = 'Euros: ')

poundconversion = Text(window, height = 2, width = 25, fg = 'blue')
pesoconversion = Text(window, height = 2, width = 25)
euroconversion = Text(window, height = 2, width = 25)

conversionbutton = Button(window, text = 'Convert', command = from_kg)

dollarstring.grid(row=0,column=0)
dollarinputstring.grid(row=0,column=1)
conversionbutton.grid(row=0,column=3)
poundreturn.grid(row=1,column=0)
pesoreturn.grid(row=1,column=2)
euroreturn.grid(row=1,column=4)
poundconversion.grid(row=2,column=0)
pesoconversion.grid(row=2,column=2)
euroconversion.grid(row=2,column=4)

window.mainloop()
