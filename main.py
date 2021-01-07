import time
ports = 4
bins = [Food_Bin(0), Food_Bin(1), Food_Bin(2), Food_Bin(3)]

class Food_Bin:
    def __init__(self,  ledport):
        self.experationtime = 0
        self.ledport = ledport
        self.inuse = False

    def getTimeRemaining():
        ticks = experationtime - time.time()
        return ticks/86400

    def getNewColor(timeremaining):
        red = ((.264039 * timeremaining ** 6) + (-4.962 * timeremaining ** 5)+ (32.0903 * timeremaining ** 4) + (-74.065 * timeremaining ** 3) + (158.718 * timeremaining))
        return [red, 255 - red, 0]

    def stasis():
        #turn off the LEDS
        self.inuse = False

    def setColor(color):
        print("set the LED color to a [r, g, b]")

    def activate(experationtime):
        self.experationtime = experationtime
        self.inuse = True

def foodbinTime():
    lengthoftimer = 0
    timeofpress = time.time()
    while(time.time() > timeofpress - 4):
         if(buttonday):
             lengthoftimer ++
             timerofpress = time.time()
        if(buttonthreeday):
            lengthoftimer + 3
            timerofpress = time.time()
        if(buttonweak):
            lengthoftimer = lengthoftimer + 7
            timerofpress = time.time()
    return (lengthoftimer * 86400 + timeofpress)

def selectBin():
    binNotSelected = True
    currentbin = 0
    while(binNotSe1lected):
        enterpressed = False
        bins[currentbin].setColor([100, 200, 200])
        print ("wait 1 seconds")
        while(enterpressed):
            if("enter held"):
                return currentbin
            if("enter pressed"):
                enterpressed = True

def clearBin(porttoclear):
    for x in bins:
        if(x.ledport = porttoclear):
            x.inuse = False

def newBin():
    binport = selectBin()
    time = foodbinTime()
    bins[binort].activate(time)

while(True):
    while("light detected"):
        for x in bins:
            x.setColor(x.getNewColor(x.timeRemaining()))
    
