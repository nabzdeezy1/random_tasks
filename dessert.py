bananaORapple = input("Pick up the banana or the apple?")

if bananaORapple == "banana":
    milkORpancake = input("Pick up the milk or the pancake? ")
    if (milkORpancake == "milk"):
      print("You have made banana milkshake!")
    else:
      print("You have made banana pancakes!")
else:
    pastryORtoffee = input("Pick up the pastry or the toffee? ")
    if (pastryORtoffee == "pastry"):
      print("You have made apple pie!")
    else:
      print("You have made a toffee apple!")