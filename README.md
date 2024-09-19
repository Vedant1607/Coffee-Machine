# Coffee-Machine

This Python program simulates the functionality of a basic coffee machine. The user can select from three available drinks: espresso, latte, or cappuccino. The program checks if there are sufficient ingredients to make the chosen drink and calculates the cost based on the currency input provided by the user. If enough money is entered, it deducts the ingredients and provides change if necessary. The machine also allows the user to check available resources and the total profit earned so far.

## Features

### Drink Options:

espresso
latte
cappuccino

### Operations:

off: To stop the coffee machine
report: To view the remaining resources and profit

### Ingredients Management: The machine checks for sufficient ingredients and deducts them as needed.

### Coin Processing: Users enter the currency values they insert, and the program calculates whether enough money has been provided.

### Change Calculation: If the user provides more money than required, the machine returns the change.

## How it Works

1. The machine asks the user for their drink choice.
2. If the user enters "report", the machine prints the current resource levels and total profit.
3. If the user enters "off", the machine powers down.
4. For valid drink selections, the machine checks if there are sufficient ingredients.
5. The user is prompted to enter money in the form of different currency notes (10, 20, 50, 100, 200, and 500 rupee notes).
6. If sufficient funds are provided, the machine deducts the required ingredients and serves the coffee, otherwise, it refunds the money.
7. The program continues to run until the user turns it off.
