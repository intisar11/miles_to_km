from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_results.config(text=f"{km}")

window = Tk()

window.title("Miles to Kilometer converter")
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=2, row=1)


miles = Label(text="Miles")
miles.grid(column= 3, row=1)

km = Label(text="Km")
km.grid(column=3, row=2)

kilometer_results = Label(text="0")
kilometer_results.grid(column=2, row=2)

converter = Label(text="is equal to")
converter.grid(column=1, row=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)





window.mainloop()
