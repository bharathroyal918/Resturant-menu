# creating a menu
menu = {
    'Chicken Biryani':299,
    'Veg Biryani': 199,
    'Gobi':129,
    'Mutton Biryani': 349,
    'Pasta':139,
    'Veg Pizza':159
}
print("Welcome to Friends Resturant")
print(" Chicken Biryani:299 \n Veg Biryani: 199 \n Gobi:129\n Mutton Biryani: 349\n Pasta:139\n Veg Pizza:159")

order_total=0
item_1=input("Enter the name of item that you want to order :")

if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} as been added in  your order")
else:
    print(f"order item {item_1} is not available ")

other_item= input("Do you want to other item (yes/no) :")
if other_item=="yes":
    item_2=input("Enter the name of second item : ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"item {item_2} as been added to your order ")
    else:
        print(f"order item {item_2} is not availabe!")
print(f"The total amount of items to pay is : {order_total}")