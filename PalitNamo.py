class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})
        print(f"{quantity}x {name} added to cart.")

    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]
        print(f"{name} removed from cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            for item in self.items:
                print(f"  {item['quantity']}x {item['name']} - ₱{item['price']} each")

    def checkout(self):
        if self.items:
            total = sum(item['price'] * item['quantity'] for item in self.items)
            print(f"Total: ₱{total}")
            self.items.clear()
            print("Thank you for purchasing!")
        else:
            print("Your cart is empty.")


def main():
    cart = ShoppingCart()

    while True:
        print("\n===== SHOPPING CART MENU =====\n")
        cart.view_cart()
        print("\nA. Add Items | B. Remove Items | C. Checkout | D. Exit\n")
        choice = input("My Choice: ").strip().upper()
        
        if choice == 'A':
            num_items = int(input("\nHow many items?: "))
            for i in range(num_items):
                name = input(f"\nItem {i+1} Name: ")
                price = float(input("\nPrice: "))
                quantity = int(input("\nQuantity: "))
                cart.add_item(name, price, quantity)
        elif choice == 'B':
            cart.remove_item(input("\nItem to Remove: "))
        elif choice == 'C':
            cart.checkout()
        elif choice == 'D':
            print("Done Shopping!")
            break
        else:
            print("Invalid choice")

main()
