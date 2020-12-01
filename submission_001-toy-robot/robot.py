
# TODO: Decompose into functions
"""This function moves the square with different degrees and has a single parameter - size """
def move_square(size):
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")
"""This is our rectangle function which moves the triangle shape using its length and width """
def move_rectangle():
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

"""This function moves the circle in different degrees """
def move_circle():
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        
"""This function calls the argument size from square function """
def square_dancing():
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        degrees = 90
        size = 20
        print("* Move Forward "+str(length))
        #print("Moving in a square of size 10")
        move_square(size)
        # for j in range(4):
        #     print("* Move Forward " + str(size))
        #     print("* Turn Right " + str(degrees) + " degrees")
        #     degrees = 90
  
def crop_circle():
    print("Crop circles - 4 circles")
    length = 20
    degrees = 1
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle()
        # print("Moving in a circle")
        # for k in range(360):
        #     print("* Move Forward " + str(length))
        #     print("* Turn Right " + str(degrees) + " degrees")
   


    '''The function should be named move_shapes.
        It doesnt just move but it moves several shapes in different directions. 
    '''
    def move(): 
    move_square(10)
    move_rectangle()
    move_circle()
    square_dancing()
    crop_circle()
    #size = 10
    # print("Moving in a square of size "+str(size))
    # for i in range(4):
    #     degrees = 90
    #  print("* Move Forward "+str(size))
    #  print("* Turn Right "+str(degrees)+" degrees")

    #length = 20
    #width = 10              
    
    # print("Moving in a rectangle of "+str(length)+" by "+str(width))
    # for i in range(2):
    #     degrees = 90
    #     print("* Move Forward "+str(length))
    #     print("* Turn Right "+str(degrees)+" degrees")
    #     print("* Move Forward "+str(width))
    #     print("* Turn Right "+str(degrees)+" degrees")

    # print("Moving in a circle")
    # degrees = 1
    # for i in range(360):
    #     length = 1
    #     print("* Move Forward "+str(length))
    #     print("* Turn Right "+str(degrees)+" degrees")

    # print("Square dancing - 3 squares of size 20")
    # for i in range(3):
    #     length = 20
    #     print("* Move Forward "+str(length))
    #     print("Moving in a square of size 10")
    #     for j in range(4):
    #         print("* Move Forward " + str(size))
    #         print("* Turn Right " + str(degrees) + " degrees")
    #         degrees = 90

    # print("Crop circles - 4 circles")
    # for i in range(4):
    #     print("* Move Forward "+str(length))
    #     print("Moving in a circle")
    #     for k in range(360):
    #         print("* Move Forward " + str(length))
    #         print("* Turn Right " + str(degrees) + " degrees")
   
    
    
def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
