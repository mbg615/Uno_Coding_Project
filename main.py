from pyglet.window import Window, key, mouse
from pyglet import app, shapes, graphics, image, sprite

winWidth = 800
winHeight = 600
fus = 1
logoImage = image.load("C:/Users/Michael/Desktop/Uno_Negativo-master/UnoNegativo.png")
Red = (255, 0, 0)
Blue = (0, 0 ,255)
window = Window(winWidth, winHeight, resizable = True)
batch = graphics.Batch()

menuBackground = graphics.OrderedGroup(0)
menuForeground = graphics.OrderedGroup(1)

def backgroundUpdate():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    mainBackground.width = winWidth
    mainBackground.height = winHeight

def menuUpdate():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    logo.x = logo.x + (winWidth  // 4)
    logo.y = logo.y + (winHeight // 3)

def menuReturn():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    logo.x = 250
    logo.y = 350

def on_key_press(symbol, modifiers):
    if symbol == key.F:
        global fus
        fus += 1
 
def on_key_release(symbol, modifiers):
    if symbol == key.F and fus % 2 == 0:
        window.set_fullscreen(True) 
        backgroundUpdate()
        menuUpdate()

    if symbol == key.F and fus % 2 == 1:
        window.set_fullscreen(False)
        backgroundUpdate()
        menuReturn()

def hola():
    print("hola")
    return

def adios():
    print("adios")
    return

class buttonRect(object):

    def __init__(self, x, y, width, height, color, action):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.name = shapes.Rectangle(self.x, self.y, self.width, self.height, self.color, batch=batch, group=menuForeground)
        self.action = action

        self.minX = x
        self.maxX = x + width
        self.minY = y
        self.maxY = y + height

    def boundary(self, mousePos):

        mouseX, mouseY = mousePos

        if mouseX > self.minX and mouseX < self.maxX and mouseY > self.minY and mouseY < self.maxY:
            eval(self.action + "()")

#holaButton = buttonRect(250, 100, 50, 50, Blue, "hola")
#adiosButton = buttonRect(400, 200, 100, 100, Blue, "adios")

def loadButtons(mouseX, mouseY):

    mousePos = mouseX, mouseY

    #holaButton.boundary(mousePos)
    #adiosButton.boundary(mousePos)



def on_mouse_press(mouseX, mouseY, button, modifiers):

    loadButtons(mouseX, mouseY)

mainBackground = shapes.Rectangle(0, 0, winWidth, winHeight, Red, batch=batch, group=menuBackground)
mainBackground.opacity = 220


#testButton = shapes.Rectangle(250, 100, 50, 50, Blue, batch=batch, group=menuForeground)

def on_draw():
    window.clear()
    batch.draw()
    logo.draw()

logo = sprite.Sprite(logoImage, 250, 350, group=menuForeground)

window.push_handlers(on_draw, on_key_press, on_key_release, on_mouse_press)
        
app.run()
