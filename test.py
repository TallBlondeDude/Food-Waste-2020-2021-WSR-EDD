import time

class Food_Bin:
    def __init__(self, experationtime, ledport):
        self.experationtime = experationtime
        self.ledport = ledport

    def getTimeRemaining():
        ticks = experationtime - time.time()
        return ticks/86400
        
    def getNewColor(timeremaining):
        red = ((.264039 * timeremaining ** 6) + (-4.962 * timeremaining ** 5)+ (32.0903 * timeremaining ** 4) + (-74.065 * timeremaining ** 3) + (158.718 * timeremaining))
        return [red, 255-red, 0]
