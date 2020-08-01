class tamagochi():
    hunger=0
    thirst=0
    sleepiness=0
    walk=0
    health=100
    def takeawalk(self):
        self.walk-=50
        if self.walk<0:
            self.walk=0
        self.hunger+=20
        self.thirst+=30
    def sleep(self):
        self.sleepiness-=50
        if self.sleepiness<0:
            self.sleepiness=0
        self.thirst+=60
        self.hunger+=10
        self.walk+=30
    def feed(self):
        self.hunger-=50
        if self.hunger<0:
            self.hunger=0
        self.thirst+=20
        self.walk+=10
    def drink(self):
        self.thirst-=50
        if self.thirst<0:
            self.thirst=0
        self.walk+=10
    def healthc(self):
        if self.hunger>100 or self.thirst>100:
            self.health-=15
            if self.hunger>100:
                self.hunger=100
            else:
                self.thirst=100
        elif self.hunger<30 and self.thirst<30:
            self.health+=25
            self.hunger+=30
            self.thirst+=20
    def walkc(self):
        if self.walk>150:
            return 'run'
    def update(self):
        self.healthc()
        if self.walkc()=='run':
            return 'run'
        if self.health<0:
            return 'dead'
        if self.hunger>60:
            return 'hungry'
        if self.thirst>80:
            return 'thirsty'
        if self.walk>60:
            return 'walk'
        if self.sleepiness>70:
            return 'sleepy'
        self.hunger+=1
        self.thirst+=1
        self.walk+=1
        self.sleepiness+=1
        return 'happy'
    def getstats(self):
        return self.hunger,self.thirst,self.walk,self.sleepiness
