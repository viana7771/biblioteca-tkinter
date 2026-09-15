import tkinter as tk

window = tk.Tk()
window.title('Doubling Calculator')
window.geometry('700x400')

tk.Label(
    window,
    text='Write a number: '
).pack()

def to_execute():
    execute_number = float(number.get())
    response['text'] = execute_number * 2

def to_clean():
    response['text'] = ''
    
number = tk.Entry(window)
number.pack()

calculator_number = tk.Button(
    window,
    text='Duble the Number',
    command=to_execute
)
calculator_number.pack()

response = tk.Label(
    window,
    text=''
)
response.pack()

clean_number = tk.Button(
    window,
    text='Clean Number',
    command=to_clean
)
clean_number.pack()

window.mainloop()