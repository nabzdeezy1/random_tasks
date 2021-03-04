class Restaurant:
    def __init__(self, name, website, cuisine):
        self.name = name
        self.website = website
        self.cuisine = cuisine
        
dominoes = Restaurant("Dominoes", "www.dominoes.co.uk", "pizza")
yosushi = Restaurant("Yo Sushi!", "www.yosushi.co.uk", "sushi")
fiveguys = Restaurant("Five Guys", "www.fiveguys.co.uk" ,"burger")

restaurants = [dominoes, yosushi, fiveguys]

exit = False
while exit == False:
    print("CS1822 Restaurant DB")
    print("1. Display restaurant list")
    print("2. Add a restaurant")
    print("3. Exit")
    choice = input("Please enter your choice: ")
    
    if choice == "1":
        for i in range(0, len(restaurants)):
            print(restaurants[i].name + " - " + restaurants[i].website + " - " + restaurants[i].cuisine)
            
    if choice == "2":
        rest_n = input("Enter restaurant name: ")
        rest_w = input("Enter website: ")
        rest_c = input("Enter cuisine: ")
        new = Restaurant(rest_n, rest_w, rest_c)
        restaurants.append(new)
    
    if choice == "3":
        print("Goodbye!")
        exit = True