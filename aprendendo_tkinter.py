import tkinter as tk

window = tk.Tk()
window.title('Futuro programa')
window.geometry('700x400')

tk.Label(
    window,
    text='Sistema',
    font=('Arial', 12),
    fg='black'
).pack()

window.mainloop()