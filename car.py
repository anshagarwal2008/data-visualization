class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.model = model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit


    def start(self):
        print("car started")

    def stop(self):
        print("car stoped ")

    def accelarator(self):
        print("car is accelarating")                

    def gear_change(self,gear_type):
        print("gear changed")
        """ gear changed functionality"""



ansh= Car("A6","red","audi",80)
ansh.accelarator()