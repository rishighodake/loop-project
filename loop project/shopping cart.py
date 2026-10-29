
products = int(input("Enter number of products: "))

subtotal = 0

for i in range(1, products + 1):
    print("\nProduct", i)

    price = float(input("Enter product price: ₹"))
    quantity = int(input("Enter quantity: "))

    while price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        price = float(input("Enter product price again: ₹"))
        quantity = int(input("Enter quantity again: "))

    item_total = price * quantity
    subtotal += item_total

discount = 0

if subtotal >= 3000:
    discount = subtotal * 0.10

amount = subtotal - discount

if amount < 1500:
    delivery = 100
else:
    delivery = 0

final_amount = amount + delivery

print("\n--- Shopping Bill ---")
print("Subtotal: ₹", subtotal)
print("Discount: ₹", discount)
print("Delivery Charge: ₹", delivery)
print("Final Payable Amount: ₹", final_amount)
