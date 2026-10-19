# Calculating a shopping cart
prices = [5.95, 3.00, 12.50]
total_price = 0
total_price = sum(prices)
tax_rate = 0.08    # 8% tax 
total_tax = 0
for price in prices:
    total_tax = total_price * tax_rate
    total_bill = total_tax + total_price

print(f"Total price (with tax): ${total_bill:.2f}")
