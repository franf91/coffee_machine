# Coffee Machine Program Requirements

This program simulates a coffee machine and provides the following features:

1. **User Interaction:**
   - Prompt the user with the question: "What would you like? (espresso/latte/cappuccino)"
   - The prompt is displayed after each action, ensuring a smooth user experience.

2. **Shutdown Option:**
   - For maintainers, the program can be turned off by entering "off" as a secret command, ending the execution.

3. **Report Generation:**
   - When the user inputs "report," a report is generated, displaying current resource values:
     - Water: 100ml
     - Milk: 50ml
     - Coffee: 76g
     - Money: $2.5

4. **Resource Availability Check:**
   - The program checks if there are sufficient resources to make the selected drink.
   - If resources are depleted (e.g., not enough water), it informs the user.

5. **Coin Processing:**
   - If sufficient resources are available, the user is prompted to insert coins.
   - The program calculates the monetary value of the inserted coins (quarters, dimes, nickels, pennies).

6. **Transaction Validation:**
   - The program checks if the user has inserted enough money to purchase the selected drink.
   - If not enough money is inserted, it refunds the money with a message.
   - If the transaction is successful, the cost of the drink is added to the machine's profit.

7. **Change Handling:**
   - In case the user inserts more money than required, the program offers change rounded to two decimal places.
   - For example, "Here is $2.45 in change."

8. **Coffee Making:**
   - If the transaction is successful and resources are available, the program deducts ingredients to make the drink from the machine's resources.
   - The user is then served their selected drink with the message "Here is your latte. Enjoy!" (or the chosen drink).

These features ensure a user-friendly coffee machine experience, managing resources, handling transactions, and providing delightful coffee beverages.
