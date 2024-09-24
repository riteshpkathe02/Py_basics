class Human:
    #Properties
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    #Mehods
    def do_work(self):
        if self.occupation == "Tennis Player":
            print(self.name,"plays tennis")
        elif self.occupation=="business":
            print(self.name, "Paissaa, Daasanga")

    def speaks(self):
        print(self.name,"bolta hai Aeee champlii")

Ambani = Human("Jethalal Champaklal Gada","business")
Ambani.do_work()
Ambani.speaks()

print(Ambani.occupation)