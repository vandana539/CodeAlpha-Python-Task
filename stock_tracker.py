# CodeAlpha Internship - Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Stock:", stock_name)
        print("Price per share: $", stock_prices[stock_name])
        print("Investment value: $", investment)

    except ValueError:
        print("Please enter a valid whole number for quantity.")

print("\nTotal Investment Value: $", total_investment)

save = input("Save result to a text file? (yes/no): ").lower().strip()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write(f"Total Investment Value: ${total_investment}\n")

    print("Result saved in portfolio.txt")

print("Thank you for using Stock Portfolio Tracker!")