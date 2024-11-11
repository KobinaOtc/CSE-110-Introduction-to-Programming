shopping_cart = []
new_item = ''
prices = []
new_price = ""

total = 0

while new_item != "quit":
    new_item = input ("What item would you like to add? ")
    if new_item != 'quit':
        new_price = input(f"What is the price of '{new_item}'? ")
        shopping_cart.append(new_item)
        prices.append (new_price)
        print()
        print (f"'{new_item}' has been added to the cart. ")

print()
print("The contents of the shopping cart are: ")

for i in range (len (shopping_cart)):
    new_item = shopping_cart [i]
    new_price = prices [i]
    total += float(prices[i])

    print (f" {i+1} - {new_item} - ${new_price}")

print(f"The total is: ${total:.2f}")

