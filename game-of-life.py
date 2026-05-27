import tkinter as tk

fr = open("glider-gun.txt", "r")
height = int(fr.readline().strip())
width = int(fr.readline().strip())
cell_size = 10

win = tk.Tk()
win.title("Game of Life")
canvas = tk.Canvas(win, width = width*cell_size, height = height*cell_size, bg = "white")
canvas.pack()

dish1 = []
dish2 = []
generation = 1

def create_dishes(height, width):
    global dish1, dish2
    for i in range (height):
        dish2.append([0] * width)
        dish1.append([0] * width)

    y = 0
    x = 0
    
    for line in fr:
        x = 0
        for char in line.strip():
            if char != "-":
                dish1[y][x] = 1
            x += 1
        y += 1

def get_neighbors(dish, x, y):
    neighbors = 0
    if y > 0:
        if x > 0 and dish[y-1][x-1] == 1: neighbors += 1
        if dish[y-1][x] == 1: neighbors += 1
        if x < width - 1 and dish[y-1][x+1] == 1: neighbors += 1
    
    if x > 0 and dish[y][x-1] == 1: neighbors += 1
    if x < width - 1 and dish[y][x+1] == 1: neighbors += 1
    
    if y < height - 1:
        if x > 0 and dish[y+1][x-1] == 1: neighbors += 1
        if dish[y+1][x] == 1: neighbors += 1
        if x < width - 1 and dish[y+1][x+1] == 1: neighbors += 1
    
    return neighbors

def copy_dishes(source, destination): 
    for y in range(height):
        for x in range(width):
            neighbours = get_neighbors(source, x, y)
            if source[y][x] == 1:
                if neighbours < 2:
                    destination[y][x] = 0
                if neighbours == 2 or neighbours == 3:
                    destination[y][x] = 1
                if neighbours > 3:
                    destination[y][x] = 0
            else:
                if neighbours == 3:
                    destination[y][x] = 1

def create_grid():
    for i in range(0, width*cell_size, cell_size):
        canvas.create_line(i, 0, i, height*cell_size, fill="lightgray")
    for i in range(0, height*cell_size, cell_size):
        canvas.create_line(0, i, width*cell_size, i, fill="lightgray")

def paint_dish(dish):
    for y in range(height):
        for x in range(width):
            if dish[y][x] == 1:
                canvas.create_rectangle(x*cell_size, y*cell_size, (x+1)*cell_size, (y+1)*cell_size, fill="wheat4")
            else:
                canvas.create_rectangle(x*cell_size, y*cell_size, (x+1)*cell_size, (y+1)*cell_size, fill="white")

def sterilize_dish(dish):
    for y in range(height):
        for x in range(width):
            dish[y][x] = 0

def life():
    global generation
    canvas.delete("all")
    create_grid()

    if generation % 2 == 1:
        sterilize_dish(dish2)
        copy_dishes(dish1, dish2)
        paint_dish(dish2)
        
    else:
        sterilize_dish(dish1)
        copy_dishes(dish2, dish1)
        paint_dish(dish1)

    generation += 1
    canvas.after(100, life)

create_dishes(height, width)
paint_dish(dish1)
life()

win.mainloop()
