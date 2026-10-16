# Calculating a shopping cart
prices = [5.95, 3.00, 12.50]
total_price = 0
total_price = sum(prices)
print(total_price)
tax_rate = 1.08    # 8% tax 
total_tax = 0
for price in prices:
    total_tax = price * tax_rate
    total_price = total_tax + total_price

print(f"Total price (with tax): ${total_price}")
