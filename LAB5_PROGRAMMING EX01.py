print("Anas Ahmed(18b-116-cs),CS-A")
print('Lab No.5')
print('Programming Ex#1')
def area():
    import math
    radius = eval(input('enter value of radius= ' ))
    height = eval(input('enter value for height= '))
    area = (2*math.pi*radius*height) + (2*math.pi*radius**2)
    print('The area of the cylinder is {0:{1}f}cm\u00b2'.format(area,height))
def volume():
    import math
    radius2= eval(input('enter value of radius for calculating volume= '))
    height2= eval(input('enter value of height for calculating volume= '))
    volume = (math.pi*radius2**2*height2)
    print("The volume of the cylinder is {0:{1}f}cm\u00b3".format(volume,height2))
