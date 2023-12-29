class train :
    def __init__(self, name, cost, seats) :  
        self.name = name
        self.cost = cost
        self.seats = seats

    def TrainInfo(self) :
        print(f"Name of the train is {self.name} \nThe ticket cost of train is {self.cost} \nSeats available in train is {self.seats} ")

    def bookTicket(self) :
        if (self.seats>0) :
            print(f"Your ticket is booked!!, Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else :
            print("sorry this tarin is full!!, kindly try in tatkal")
        
    def cancelTicket(self) :
        print("your ticket is cancel")
        self.seats = self.seats + 1

smith = train("Rajdhani express", 1700, 3)
smith.TrainInfo()
smith.bookTicket()
smith.bookTicket()
smith.bookTicket()
smith.bookTicket()
smith.cancelTicket()
smith.bookTicket()
smith.TrainInfo()
