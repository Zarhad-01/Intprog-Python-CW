#Python Assignment
#Student ID: 895059

from graphics import *

def main():
    print("________START________")
    selectedColours, size = getInput()
    drawPatches(*selectedColours, size)
    #The "*selectedColours" allows the array to be input as 3 arguments
    print("________END________")

def getInput():
    isInvalid = True
    
    #Input validation for size of patchwork
    while isInvalid:
        size = input("What sized window would you like(5, 7, 9): ")
        
        if size.isdigit():
            #Ensure input is a digit 
            size = int(size)
            
            if size == 5 or size == 7 or size == 9:
                #Ensure size is valid
                isInvalid = False
            else:
                print("You didn't input one of the valid numbers.")
                
        else:
            print("You didn't input a number.")

    #Setting up for next while loop, with a list of allowed colours
    isInvalid = True
    validColours = ["red","green","blue","magenta","orange","pink"]
    selectedColours = []
    
    
    while isInvalid:
        colour = input("Pick your colour: ").lower()
             
        if colour in validColours:
            #Colour is a valid choice
            if colour not in selectedColours:
                #Colour has not been previously picked
                selectedColours.append(colour)
            else:
                print("You picked two of the same colour!")
        else:
            print("Your colour isn't one of the valid colours.")
            print("The valid colours are "+ ", ".join(validColours))
            
        if len(selectedColours) == 3:
            isInvalid = False
    
    return selectedColours, size

def drawPatches(c1,c2,c3,size):
    win = GraphWin("Patchwork: 895059",size*100, size*100)
    win.setBackground("white")
    
    colourLocation = size-1 
    
    #squarePatchStack is the  height of each 'stack' of square patchs
    squarePatchStack = size-1 
    
    for x in range(size):
        for y in range(size):
            
            if x+y< colourLocation:
                #Top left sectors colour
                colour = c1
            elif x+y==colourLocation or x==colourLocation or y==colourLocation:
                #Colour going along middle diagonally, bottom and left side
                colour = c2
            else:
                #Colour of the bit inside the above colour sector
                colour = c3
                
            if x%2==0 and y>=squarePatchStack:
                drawSquarePatch(win,x*100,y*100,colour)
            else:
                drawArrowPatch(win,x*100,y*100,colour)
        
        if x%2==0:
            #Increases the square patch stack height by 2 each time
            squarePatchStack-=2

def drawSquarePatch(win,x1,y1,colour):
    p2 = Point(x1,y1+100)
    
    for i in range(10):
        square = Rectangle(p2,Point(x1+100,y1))
        square.draw(win)
        
        #every other square must be white
        if  i%2 == 0:
            square.setOutline("white")
            square.setFill("white")
        else:
            square.setOutline(colour)
            square.setFill(colour)
        
        x1 -= 10
        y1 += 10
    
def drawArrowPatch(win,patchLocX,patchLocY,colour):
    for y in range(0,100,20):
        for x in range(0,100,20):
            
            shape = \
                [Point(x+patchLocX,y+patchLocY),
                Point(x+patchLocX+10,y+patchLocY+10),
                Point(x+patchLocX+20,y+patchLocY),
                Point(x+patchLocX+20,y+patchLocY+10),
                Point(x+patchLocX+10,y+patchLocY+20),
                Point(x+patchLocX,y+patchLocY+10)]
            
            shape = Polygon(shape)
            shape.draw(win)
            shape.setOutline(colour)
            
            if not((x==20 or x==60) and (y==20 or y==60)):
                shape.setFill(colour)
main()