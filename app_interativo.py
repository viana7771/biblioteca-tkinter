import tkinter as tk

name = str(input('Write your name: '))

window = tk.Tk()
window.title('My First Interactive App')
window.geometry('400x200')

tk.Label(
    window,
    text=f'Bem Vindo, {name}!',
    font=('Arial', 12)
).pack()

window.mainloop()