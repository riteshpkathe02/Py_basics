# def calculate_area(base, height):
#     area = (1/2)*base*height
#     return area

# base = int(input("Enter base of traingle : "))
# height = int(input("Enter height of traingle : "))

# print(calculate_area(base, height))

def calculate_area(shape, base, height):

    if shape==3:
        area = (1/2)*base*height
    elif shape==4:
        area = base*height
    else:
        print("Given shape is invalid")

    return area        

shape = int(input("Rectangle=4 or Traingle=3 : "))
base = int(input("Enter base : "))
height = int(input("Enter height : "))

print(calculate_area(shape, base, height))