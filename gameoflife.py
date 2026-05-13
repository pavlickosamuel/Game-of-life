fr = open("glider-gun.txt", "r")
height = int(fr.readline().strip())
width = int(fr.readline().strip())

dish1 = []
dish2 = []

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
    if x > 0 and y > 0 and dish[y-1][x-1] == 1:
            neighbors += 1
    if y > 0 and x < width - 1 and dish[y-1][x+1] == 1:
            neighbors += 1
    if x > 0 and dish[y][x-1] == 1:
            neighbors += 1
    if x < width - 1 and dish[y][x+1] == 1:
            neighbors += 1
    if x > 0 and y < height - 1 and dish[y+1][x-1] == 1:
            neighbors += 1
    if y < height - 1 and dish[y+1][x] == 1:
            neighbors += 1
    if y < height - 1 and x < width - 1 and dish[y+1][x+1] == 1:
            neighbors += 1
    if x > 0 and y < height - 1 and dish[y+1][x-1] == 1:
            neighbors += 1
    print(neighbors)

#def copy_dishes(source, destination): kopirovat miskz medyi sebou kopirovanie sa musi striedat
        

create_dishes(height, width)
get_neighbors(dish1, 0, 0)
