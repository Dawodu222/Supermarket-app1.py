import re


class Supermarket:
    sections = {
        "Beverage": [("Milk", 2.5), ("Honey", 4.0), ("Bread", 1.8), ("Juice", 3.5), ("Tea", 2.0)],
        "Liquor": [("American Honey", 40.0), ("Martel", 60.0), ("Hennessy", 100.0), ("Whiskey", 30.0), ("Vodka", 25.0)],
        "Clothing": [("Jeans", 35.0), ("Shirts", 25.0), ("Socks", 5.0), ("Jacket", 45.0), ("T-shirt", 15.0)],
        "Cars": [("Benz", 45000.0), ("Chevrolet", 25000.0), ("Toyota", 30000.0), ("BMW", 55000.0), ("Ford", 22000.0)],
        "Kitchen Utensil": [("Pan", 15.0), ("Knife Set", 30.0), ("Cutting Board", 8.0), ("Blender", 40.0),
                            ("Microwave", 60.0)],
    }
    cart = []

    def display_categories(self):
        print("\n--- Welcome to Danieliz Supermarket ---")
        print("\n--- Categories ---")
        for idx, section in enumerate(self.sections, 1):
            print(f"{idx}. {section}")
        print("0. Exit")

    def display_items(self, category):
        print(f"\nItems in {category}:")
        for idx, item in enumerate(self.sections[category], 1):
            print(f"{idx}. {item[0]} ${item[1]:.2f}")
        print("0. Go back")

    def add_to_cart(self, category, item_idx):
        item = self.sections[category][item_idx - 1]
        self.cart.append(item)
        print(f"{item[0]} added to your cart.")

    def display_cart(self):
        if not self.cart:
            print("\nYour cart is empty.")
        else:
            print("\nYour Cart:")
            total = 0
            for item in self.cart:
                print(f"{item[0]} ${item[1]:.2f}")
                total += item[1]
            print(f"Total: ${total:.2f}")
        print("0. Go back")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty, can't proceed to checkout.")
            return

        # Show cart before proceeding to checkout
        self.display_cart()

        email = input("Enter your email: ")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format.")
            return

        # Collect credit card details
        credit_card = input("Enter your credit card number (16 digits): ")
        if not credit_card.isdigit() or len(credit_card) != 16:
            print("Invalid credit card number.")
            return

        # Collect CVV
        cvv = input("Enter your CVV (3 digits): ")
        if not cvv.isdigit() or len(cvv) != 3:
            print("Invalid CVV.")
            return

        # Collect expiration date (MM/YY)
        exp_date = input("Enter expiration date (MM/YY): ")
        if not re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", exp_date):
            print("Invalid expiration date format. Please use MM/YY.")
            return

        # Final message after successful checkout
        print(f"Thank you for your purchase! A receipt has been sent to {email}.")
        self.cart.clear()


def main():
    supermarket = Supermarket()

    while True:
        supermarket.display_categories()
        try:
            choice = int(input("Select a category by number, press 0 to exit: "))
            if choice == 0:
                break
            category = list(supermarket.sections.keys())[choice - 1]
            while True:
                supermarket.display_items(category)
                item_choice = int(input(f"Select an item from {category} or press 0 to go back: "))
                if item_choice == 0:
                    break
                supermarket.add_to_cart(category, item_choice)

                while True:
                    action = input(
                        "Would you like to (c)ontinue shopping, (v)iew cart, (p)roceed to checkout, or (0) to go back? ").lower()
                    if action == 'c':
                        break
                    elif action == 'v':
                        supermarket.display_cart()
                    elif action == 'p':
                        supermarket.checkout()
                        break
                    elif action == '0':
                        break
                    else:
                        print("Invalid input. Please choose again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()





