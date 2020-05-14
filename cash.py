# print(0.61 / 0.25)
# print(0.61 % 0.25)
# print(161 // 25)
def dispenser(dollars):

    numbens_of_coins = 0;
    quarters = 25;
    dimes = 10;
    nickels = 5;
    pennies = 1;
    coins = round(dollars * 100);
    print(coins)

    while coins > 0:
        if (coins >= quarters):
            remainder = coins // quarters
            coins = coins - (quarters * remainder)
            numbens_of_coins += remainder;
        elif (coins >= dimes):
            remainder = coins // dimes
            coins = coins - (dimes * remainder)
            numbens_of_coins += remainder
        elif (coins >= nickels):
            remainder = coins // nickels
            coins = coins - (nickels * remainder)
            numbens_of_coins += remainder
        else:
            remainder = coins // pennies
            coins = coins - (pennies * remainder)
            numbens_of_coins += remainder

    print(numbens_of_coins)


entrada = input('Change owed: ')
dispenser(float(entrada))