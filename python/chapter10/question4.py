# write a class Train which has method to book a ticket, get status(no of sets) and get fare information of train running under inidan railways
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    # Method to book a ticket
    def book_ticket(self):
        if self.seats > 0:
            print(f"Ticket booked! Your seat number is {self.seats}")
            self.seats -= 1
        else:
            print("Sorry, no seats available!")

    # Method to get the status of seats
    def get_status(self):
        print(f"Train name: {self.name}")
        print(f"Seats available: {self.seats}")

    # Method to get fare information
    def get_fare_info(self):
        print(f"The fare for the train {self.name} is {self.fare} INR")

# Example usage
train1 = Train("Rajdhani Express", 1500, 2)

train1.get_status()
train1.get_fare_info()

train1.book_ticket()
train1.get_status()

train1.book_ticket()
train1.get_status()

train1.book_ticket()
