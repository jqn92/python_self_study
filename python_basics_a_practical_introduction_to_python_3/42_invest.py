def invest(amount, rate, years):
    """Print amount of investment at the end of each year for a number of years."""
    for year in range(1, years+1):
        print(f"Year {year}: ${amount + (amount * rate):,.2f}.-")
        year = year + 1
        amount = amount + (amount * rate)

initial_amount = float(input("Enter an initial amount: "))
annual_rate = float(input("Enter an annual percentage rate: ")) / 100
num_years = int(input("Enter a number of years: "))

invest(initial_amount,annual_rate,num_years)
