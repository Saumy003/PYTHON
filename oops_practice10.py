class Movie:
    def __init__(self, movie_name, total_seats, tickets_price):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.tickets_price = tickets_price
        self.booked_seats = 0

    def book_tickets(self , num_of_tickets:int):
        if num_of_tickets > self.total_seats - self.booked_seats:
            print("Sorry, not enough seats available")
        else:
            self.booked_seats += num_of_tickets
            self.total_seats -= num_of_tickets
            print(f"YOUR TICKETS ARE BOOKED! THANK YOU *_*")
            print(f"Total price = {self.tickets_price * num_of_tickets}\n")
    

    def show_status(self) -> None:
        print(f"Movie name = {self.movie_name}")
        print(f"Seats avaliable = {self.total_seats}")
        print(f"Total booked = {self.booked_seats}\n")


obj1 = Movie("Hera Pheri" , 100 , 499 )
obj1.show_status()
obj1.book_tickets(70)

obj1.show_status()
