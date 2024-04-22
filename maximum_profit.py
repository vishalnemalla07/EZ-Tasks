def max_profit(stock_prices):
    if len(stock_prices) < 2:
        return 0
    
    min_price = stock_prices[0]
    max_profit = 0
    
    for price in stock_prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

input_prices = [10, 7, 5, 8, 11, 9]
print(max_profit(input_prices))
