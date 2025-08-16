class Engine:
    def __init__(self):
        print("Engine defined")
        
    def start(self):
        print("engine starting")
        
#constructor based dependency injection is the standard practice used across orgs

class Car:
    def __init__(self, engine):
        self.engine = engine
        print("engine type", self.engine)
        print("car defined")
        
    def drive(self):
        self.engine.start()
        print("car moving")
        
engine = Engine()

car = Car(engine)

car.engine.start()


