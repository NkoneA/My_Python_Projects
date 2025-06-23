
# Order processing program

discount_10 = 0.1
discount_20 = 0.2
highest_quantity = 0
highest_business = ""

print('Welcome to the Tech Inventory Bulk Order System!')

business = input('What is your business name?(X to quit): ').upper()

while business != 'X':
    product = input('What product are you ordering?: ').lower()

    # Input validation
    valid_quantity = False
    while not valid_quantity:
        quantity = int(input("How many units?: "))
        if quantity > 0 and quantity != 0:
            valid_quantity = True
        else:
            print("Please enter a valid positive numeric quantity.")

    print('**************************************')

    # Set prices 
    if product == 'keyboard':
        unit_price = 200
    elif product == 'monitor':
        unit_price = 1800
    elif product == 'mouse':
        unit_price = 150
    else:
        unit_price = 100

    # Cost calculation
    total_cost = unit_price * quantity

    # Determine discount rate
    if quantity > 10:
        discount_rate = discount_20
    elif quantity > 5:
        discount_rate = discount_10
    else:
        discount_rate = 0

    discount = total_cost * discount_rate
    final_cost = total_cost - discount

    # Display summary
    print(f'Business: {business}')
    print(f'Product: {product}')
    print(f'Quantity: {quantity}')
    if discount_rate == discount_20:
        print(f'Discount applied: 20% (R{discount:.2f})')
    elif discount_rate == discount_10:
        print(f'Discount applied: 10% (R{discount:.2f})')
    else:
        print('No discount applied.')
    print(f'Total cost: R{final_cost:.2f}')
    print('**************************************')

    # Track highest quantity
    if quantity > highest_quantity:
        highest_quantity = quantity
        highest_business = business

    # Prompt the user again
    business = input('What is your business name?(X to quit): ').upper()

# After exiting
if highest_business:
    print(f'Congratulations, {highest_business}! You have earned '
          f'a free delivery voucher for your order')






    
                 
 
                

 
               
               
