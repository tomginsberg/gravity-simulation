

class Mover():
    def __init__(self): 
        self.position = PVector(random(width),random(height))
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        

    def update (self):
        mouse = PVector(mouseX, mouseY)
        dir = PVector.sub(mouse, self.position)
        dir.normalize()
        dir.mult(0.4)
        self.acceleration = dir
        self.velocity.add(self.acceleration)
        self.velocity.limit(15)
        self.position.add(self.velocity)


    def draw(self):  
        noStroke()
        fill(255)
        ellipse(self.position.x, self.position.y, 5,5)
        
    

movers = []

def setup():
    global movers
    size(3000,1500)
    for i in range (0,500):
        movers.append(Mover()) 
    

def draw():
    fill(0)
    rect(0,0,width,height)
    for i in range (0,len(movers)):
        movers[i].update()
        movers[i].draw()
        fill(255)
        textSize(24)
        text("Particles: "+str(len(movers)),100,100)
    
def keyPressed():
    global movers
    if keyCode==38:
        movers.append(Mover())
    if keyCode==40:
        for i in range(0,5):
            del(movers[i])
            break



