fr = open("glider-gun.txt", "r")
height = int(fr.readline().strip())
width = int(fr.readline().strip())

dish1 = []
dish2 = []

def create_dishes(height, width):
    global dish1, dish2
    #idem spraviť ten prázdny
    for i in range (height):
        dish2.append([0] * width)

create_dishes(height, width)
print(dish2)