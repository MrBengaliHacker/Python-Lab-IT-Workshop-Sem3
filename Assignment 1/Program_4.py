cost = float(input("Enter the cost of the electronic item: ₹"))

if cost >= 50000:
    discount = 0.15
elif 30000 <= cost < 50000:
    discount = 0.10
elif 20000 <= cost < 30000:
    discount = 0.05
else:
    discount = 0.0

discount_amount = cost * discount
net_amount = cost - discount_amount

print("Discount Applied: ₹", discount_amount)
print("Net Amount Payable: ₹", net_amount)