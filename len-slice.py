# Topping list
toppings = ["pepperoni", "pineapple", "cheese", "sasuage", "olives", "anchovies", "mushrooms"]
#price list
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

num_pizza = len(toppings)

print('we sell',  num_pizza,  'diferent kind of pizza')

#creating two-dimensional list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"],[3, "sasuage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"] ]

print(pizza_and_prices)
pizza_and_prices.sort()

print (pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop(-1)
print(pizza_and_prices)
pizza_and_prices.insert(4, [2.5, "peper"])
print(pizza_and_prices)

#Three cheapest pizza
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
