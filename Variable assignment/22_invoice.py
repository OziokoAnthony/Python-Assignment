# Exercise 22 — Format an Invoice
# Objective: Properly align items and prices in an invoice using string formatting.
# 
# Question:
# Format an invoice for items purchased and their prices.
# 
# Expected output:
# Item        Price
# -------------------
# Laptop      $1200.99
# Mouse       $25.50

items = [
    ("Laptop", 1200.99),
    ("Mouse", 25.50),
]

print(f'{"Item":<12}{"Price":>10}')
print("-" * 22)

for item, price in items:
    print(f"{item:<12}${price:>9.2f}")
