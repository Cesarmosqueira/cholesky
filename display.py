from cholesky import *
from decimal import Decimal
from tkinter import Tk, Label, StringVar, Button, Entry, END, messagebox, PhotoImage, RIGHT, simpledialog

window = Tk()
window.title("Cholesky Descomposition")
window.geometry("1150x660+120+120")
window.configure(bg='bisque2')
window.resizable(False, False)
# empty arrays for your Entrys and StringVars
input_boxes = []
input_entries = []

output_boxes = []
output_entries = []
# callback function to get your StringVars
storage = [[],[],[]]

def store_in_a():
    c = 0
    for i in range(rows):
        storage[c].append([0]*cols)
        for j in range(cols):
            storage[c][i][j] = float(input_boxes[i][j].get())
    
def store_in_b():
    c = 1
    for i in range(rows):
        storage[c].append([0]*cols)
        for j in range(cols):
            storage[c][-1][j] = float(input_boxes[i][j].get())
def store_in_c():
    c = 2
    for i in range(rows):
        storage[c].append([0]*cols)
        for j in range(cols):
            storage[c][-1][j] = float(input_boxes[i][j].get())

def load_from_a():
    if storage[0] == []: return
    for i in range(rows):
        for j in range(cols):
            input_boxes[i][j].set(str(storage[0][i][j]))
    matrix = storage[0]
    return 
def load_from_b():
    if storage[0] == []: return
    for i in range(rows):
        for j in range(cols):
            input_boxes[i][j].set(str(storage[1][i][j]))
    matrix = storage[1]
    return 
def load_from_c():
    if storage[0] == []: return
    for i in range(rows):
        for j in range(cols):
            input_boxes[i][j].set(str(storage[2][i][j]))
    matrix = storage[2]
    return 
def get_cholesky():
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = float(input_boxes[i][j].get())
    if not is_positive_definite(matrix) or len(matrix) != len(matrix[0]):
        messagebox.showerror("error", "Can't do cholesky descomposition here")
        return
    else: 
        print("getting:",matrix)
        a = fact_cholesky(matrix)
        send_to_output(a)
        print("outing", a)
    
def send_to_input():
    for i in range(rows):
        for j in range(cols):
            input_boxes[i][j].set(output_boxes[i][j].get())
    return 

def load_random_mat():
    matrix = get_random_matrix(rows)
    for i in range(rows):
        for j in range(cols):
            input_boxes[i][j].set(str(matrix[i][j]))
    return 
def send_to_output(matrix):
    for i in range(rows):
        for j in range(cols):
            output_boxes[i][j].set(matrix[i][j])
    return 

def mult_by_its_transpose():
    print("box in 0,0 =",input_boxes[0][0].get())
    print("box in 4,5 =",input_boxes[4][5].get())
    matrix = []
    for i in range(rows):
        matrix.append([0.0]*cols)
        for j in range(cols):
            matrix[i][j] = float(input_boxes[i][j].get())

    print(matrix)
    a = AXAT(matrix)
    print(a)
    send_to_output(a)

Label(window, text="Input matrix :", font=('arial', 10, 'bold'), 
      bg="bisque2").place(x=20, y=20)
Label(window, text="Output matrix :", font=('arial', 10, 'bold'), 
      bg="bisque2").place(x=560, y=20)
x2 = 0
y2 = 0
#rows, cols = [int(x) for x in input().split()]
size = 0
while size <= 0:
    size = simpledialog.askinteger("Setup", "Enter the matrix size", initialvalue=9)

cols, rows = size, size
matrix = get_random_matrix(rows)
for i in range(rows):
    input_boxes.append([])
    input_entries.append([])
    output_boxes.append([])
    output_entries.append([])
    for j in range(cols):
        input_boxes[i].append(StringVar())
        output_boxes[i].append(StringVar())
        input_entries[i].append(Entry(window, textvariable=input_boxes[i][j],width=4))
        input_entries[i][j].place(x=60 + x2, y=50 + y2)
        output_entries[i].append(Entry(window, textvariable=output_boxes[i][j],width=4))
        output_entries[i][j].place(x=600+ x2, y=50 + y2)
        x2 += 40
    y2 += 35
    x2 = 0

cholesky_btn= Button(window,text="Cholesky", bg='bisque3', width=15, command=get_cholesky)
cholesky_btn.place(x=285,y=570)

random_gen = Button(window,text="Random PosDef", bg='bisque3', width=15, command=load_random_mat)
random_gen.place(x=100,y=570)

storeA = Button(window,text="Store A", bg='bisque3', width=7, command=store_in_a)
storeA.place(x=230,y=600)
storeB = Button(window,text="Store B", bg='bisque3', width=7, command=store_in_b)
storeB.place(x=310,y=600)
storeC = Button(window,text="Store C", bg='bisque3', width=7, command=store_in_c)
storeC.place(x=390,y=600)

readA = Button(window,text="Load A", bg='bisque3', width=7, command=load_from_a)
readA.place(x=230,y=630)
readB = Button(window,text="Load B", bg='bisque3', width=7, command=load_from_a)
readB.place(x=310,y=630)
readC = Button(window,text="Load C", bg='bisque3', width=7, command=load_from_a)
readC.place(x=390,y=630)


out_to_in = Button(window,text="Send to input field", bg='bisque3', width=15, command=send_to_input)
out_to_in.place(x=640,y=570)

photo = PhotoImage(file = r"formulapng.png") 
AxAt = Button(window,text="$AxA'$", bg='bisque3', width=80, command=mult_by_its_transpose)
AxAt.config(image=photo)
AxAt.place(x=100,y=605)

window.mainloop()