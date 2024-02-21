from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    conversion_rate = c.convert(from_currency, to_currency, amount)
    return conversion_rate

if __name__ == "__main__":
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (3-letter code): ").upper()
    to_currency = input("Enter the currency to convert to (3-letter code): ").upper()

    result = currency_converter(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {result} {to_currency}")
