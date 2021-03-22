class Rectangle:

    # Construct a rectangle object

    def __init__(self, width = 1, height = 2):

        self.width = width

        self.height = height



    def getArea(self):

        return self.width * self.height



    def getPerimeter(self):

        return 2 * (self.width + self.height)



def main():

    # Create a rectangle with width 4 and height 40

    r1 = Rectangle(4, 40)

    print("The width of the rectangle is", r1.width)

    print("The height of the rectangle is", r1.height)

    print("The area of the rectangle is", r1.getArea())

    print("The perimeter of the rectangle is", r1.getPerimeter())



    # Create a rectangle with width 3.5 and height 35.9

    r1 = Rectangle(3.5, 35.9)

    print("The width of the rectangle is", r1.width)

    print("The height of the rectangle is", r1.height)

    print("The area of the rectangle is", r1.getArea())

    print("The perimeter of the rectangle is", r1.getPerimeter())



main()

