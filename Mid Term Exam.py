class Star_Cinema:
    hall_list = []

    def __init__(self):
        pass

    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        seats = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seats

    def book_seats(self, id, seat_list):
        if id in self.__seats:
            for (row, col) in seat_list:
                if self.__seats[id][row][col] == 0:
                    self.__seats[id][row][col] = 1
                else:
                    print(f"Seat at row {row}, col {col} is already booked.")
        else:
            print(f"Show ID {id} not found.")

    def view_show_list(self):
        print("\nNow running shows are:")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Name: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id in self.__seats:
            print(f"\nAvailable seats for show ID {id}:")
            for row in self.__seats[id]:
                print(' \t'.join(['O' if seat == 0 else 'X' for seat in row]))
        else:
            print(f"Show ID {id} not found.")


cinema = Star_Cinema()
hall1 = Hall(8, 8, 1)
cinema.entry_hall(hall1)

hall1.entry_show(2, "Kalki", "12:00 pm")
hall1.entry_show(3, "Yodha", "05:00 pm")
hall1.entry_show(4, "Maidaan", "03:00 pm")
hall1.entry_show(5, "Article 370", "11:00 pm")
hall1.entry_show(6, "Fighter", "07:00 pm")

while True:
    print("\nPress 1. to view all running shows.")
    print("Press 2. to view available seats.")
    print("Press 3. to book tickets.")
    print("Press 4. to exit.")

    choice = int(input("\nPlease enter your Choice: "))

    if choice == 1:
        for hall in Star_Cinema.hall_list:
            hall.view_show_list()
    elif choice == 2:
        movie_id = int(input("\nEnter Movie ID: "))
        for hall in Star_Cinema.hall_list:
            hall.view_available_seats(movie_id)
    elif choice == 3:
        movie_id = int(input("\nEnter Movie ID: "))
        seats_to_book = []
        while True:
            row = int(input("Enter row No: "))
            col = int(input("Enter col No: "))
            seats_to_book.append((row, col))
            more = input("Do you want to book more seats? (y/n): ")
            if more.lower() != 'y':
                break
        for hall in Star_Cinema.hall_list:
            hall.book_seats(movie_id, seats_to_book)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")