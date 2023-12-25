menu_items = ["black tea", "black coffee", "white coffee", "iced tea", "iced coffee", "iced chocolate", "cookie",
              "sausage roll", "hotdog"]
item_prices = [3.5, 4, 4.5, 3.2, 4.8, 4.4, 1, 3, 3]
total_cost = 0
loop_running = True
order = []
for item in menu_items:
    print(item.title())
while loop_running:

    user_input = input("What would you like to have today?").lower().strip()
    if user_input in menu_items:
        print("Okay")
        order.append(user_input)
        total_cost = total_cost+item_prices[menu_items.index(user_input)]
        print(order)
    elif user_input == "quit":
        loop_running = False
        print("closing")
        print(total_cost)