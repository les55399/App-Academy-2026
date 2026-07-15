import random
import string


ARTISTS = [
    "Cassper Nyovest",
    "Tyla",
    "Kabza De Small",
    "Focalistic",
    "Uncle Waffles",
    "Black Coffee",
    "Major League DJz",
    "Ami Faku"
]


class Person:
    def __init__(self, name, age, email, favorite_artist):
        self.name = name
        self.age = age
        self.email = email
        self.favorite_artist = favorite_artist
        self.ticket_id = self.generate_ticket_id()

    @staticmethod
    def generate_ticket_id(length=8):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def __str__(self):
        return (
            f"---Ticket Holder Information---\n"
            f"Name            : {self.name}\n"
            f"Age             : {self.age}\n"
            f"Email           : {self.email}\n"
            f"Favorite Artist : {self.favorite_artist}\n"
            f"Ticket Number   : {self.ticket_id}\n"
        )


def menu():
    print("\n==============================\n"
         "      FNB MEGA FEST 2026\n"
        "==============================\n"
        "1. Book Tickets\n"
        "2. View All Bookings\n"
        "3. View Available Artists\n"
        "4. Exit\n"
    )


def choice():
    while True:
        user_input = input("Enter your option (1-4): ").strip()

        if not user_input:
            print("Input cannot be empty.")
            continue

        try:
            option = int(user_input)

            if 1 <= option <= 4:
                return option

            print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def value(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def book_ticket(attendees, artist_list):

    while True:
        num_of_tickets = value("How many tickets would you like to purchase? ")

        if num_of_tickets > 0:
            break

        print("You must purchase at least one ticket.")

    for ticket in range(1, num_of_tickets + 1):

        print(f"\n------ Ticket {ticket} of {num_of_tickets} ------")

        name = input("Enter your name: ").title().strip()

        while True:
            age = value("Enter your age: ")

            if age > 0:
                break

            print("Age must be greater than zero.")

        email = input("Enter your email: ").strip()

        print("\nAvailable Artists")

        for index, artist in enumerate(artist_list, start=1):
            print(f"{index}. {artist}")

        while True:
            artist_choice = value("\nSelect your favorite artist: ")

            if 1 <= artist_choice <= len(artist_list):
                favorite_artist = artist_list[artist_choice - 1]
                break

            print(f"Choose a number between 1 and {len(artist_list)}.")

        print(f"\nYou selected: {favorite_artist}")

        new_person = Person(
            name,
            age,
            email,
            favorite_artist
        )

        
        while new_person.ticket_id in attendees:
            new_person.ticket_id = Person.generate_ticket_id()

        attendees[new_person.ticket_id] = new_person

        print("\nBooking Successful!")
        print(f"Ticket Number : {new_person.ticket_id}")
        print(f"Booked For    : {new_person.name}")
        print(f"Artist        : {favorite_artist}")


def view_bookings(attendees):

    print("\n========== CURRENT BOOKINGS ==========")

    if not attendees:
        print("No bookings have been made.")
        return

    for person in attendees.values():
        print(person)


def view_artists(artist_list):

    print("\n========== AVAILABLE ARTISTS ==========")

    for index, artist in enumerate(artist_list, start=1):
        print(f"{index}. {artist}")


def main():

    attendees = {}

    while True:

        menu()

        user_choice = choice()

        match user_choice:

            case 1:
                book_ticket(attendees, ARTISTS)

            case 2:
                view_bookings(attendees)

            case 3:
                view_artists(ARTISTS)

            case 4:
                print("\nThank you for using the FNB Mega Fest Booking System.")
                print("Goodbye!")
                break


if __name__ == "__main__":
    main()