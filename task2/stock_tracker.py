
# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input(
        "\nEnter stock symbol (or 'done' to finish): "
    ).upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose an available stock.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid whole number.")

print("\n----- Your Portfolio -----")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value

    print(
        f"{stock}: {quantity} shares x "
        f"${stock_prices[stock]} = ${value}"
    )

print("--------------------------")
print(f"Total Investment Value: ${total_investment:.2f}")

# Save portfolio to a CSV file
with open("portfolio.csv", "w") as file:
    file.write("Stock,Quantity,Price,Total Value\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        file.write(f"{stock},{quantity},{price},{value}\n")

print("Portfolio saved to portfolio.csv")
