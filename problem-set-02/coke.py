def coke_machine(price):
    """
    Loop as long as collected money is lower than "price"

    Parameter: 
        price (int): actual price that the user has to pay

    Returns: 
        collected_money (int): sum of coins payed by user
    """

    collected_money = 0

    while True:
        # if collect_money is not enough, print due, and reloop
        # print(f"Amount Due: {price - collected_money}")
        print(f"Amount Due: {price - collected_money}")

        user_input = input("Insert Coin (5, 10, 25): ")

        try:
            coin = int(user_input)
        except ValueError:
            pass
        else: 
            if coin == 5 or coin == 10 or coin == 25:
                collected_money += coin

        if collected_money >= price:
            # if enough money is collected, calculate the owed money
            return collected_money - price

        

if __name__ == "__main__":
    actual_price = 50
    due = coke_machine(actual_price)

    print(f"Change owed: {due}")