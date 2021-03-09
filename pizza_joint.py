# Make Some Pizzas

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
num_pizzas = len(toppings)

prices = [2, 6, 1, 3, 2, 7, 2]

print("We sell",str(num_pizzas),"different kinds of pizza!")

pizzas = list(zip(prices, toppings))

print(pizzas)

# Sorting and Slicing Pizzas

pizzas.sort()

cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:-3]

print(three_cheapest)

num_two_dollar_slices = prices.count(2)



