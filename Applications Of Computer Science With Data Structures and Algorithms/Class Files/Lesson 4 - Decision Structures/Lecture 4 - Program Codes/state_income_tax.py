def main():
    netIncome = float(input("Enter net income.\nDo not include a dollar sign or any commas. "))

    if netIncome <= 15000:
        tax = 0
    elif netIncome <= 30000:
        tax = (netIncome - 15000) * 0.05
    else:
        fivePercentTax = 0.05 * 15000
        tenPercentTax = 0.1 * (netIncome - 30000)
        tax = fivePercentTax + tenPercentTax

    print("Tax due = $", tax)

if __name__ == "__main__":
    main()