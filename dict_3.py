def circle_calc():
    r=int(input("Enter the radius of a circle"))
    pi=3.1415926535897932384626433832795

    area = pi*r*r
    dia = 2*r
    circum = pi*dia

    circle={"Area":area, "Diameter":dia, "Circumference":circum}

    print(circle)

if __name__=='__main__':
    circle_calc()

'''Solution

import math

def circle_calc(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    diameter=2*radius
    return area, circumference,diameter

if __name__=="__main__":
    r=input("Enter a radius:")
    r=float(r)
    area, c, d = circle_calc(r)
    print(f"area {area}, circumference {c}, diameter {d}")'''