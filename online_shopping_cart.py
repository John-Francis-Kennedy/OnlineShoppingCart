class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")
        return total_cost   # return value so main program can add it
        

# Main program
cart = []  # list to hold all items

# Ask how many items user wants
num_items = int(input("How many items would you like to add to your cart? "))

for i in range(1, num_items + 1):
    print(f"\nItem {i}")
    name = input("Enter the item name:\n")
    price = float(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))

    # Create object and add to cart
    item = ItemToPurchase(name, price, quantity)
    cart.append(item)


# Print results
print("\nTOTAL COST")
grand_total = 0
for item in cart:
    grand_total += item.print_item_cost()

print(f"\nTotal: ${grand_total:.0f}")
