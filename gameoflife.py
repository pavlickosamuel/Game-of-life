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

create_dishes(height, width)
print(dish2)