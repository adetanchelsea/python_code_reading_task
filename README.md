# Budget Analyzer | A Python Code Reading Task
This repository shows my solution to the code reading task. The task is to thoroughly read through a python script, learn from it and answer a few questions.

## Table of Contents
- [Introduction](#budget-analyzer--a-python-code-reading-task)
- [Questions & Answers](#questions--answers)
- [Changes Made To The Project](#changes-made-to-the-project)

## Questions & Answers
### QUESTION 1: WHAT DOES THIS PROJECT DO?
This project is a simple budget analysis tool that helps track personal finances. It loads a list of transactions from a JSON file, where each transaction includes the date, amount, and category (for example, salary, groceries, utilities). The program then processes these transactions to calculate the total income, total expenses, and a breakdown of spending by category. Using this information, it generates a clear budget summary that shows how much money was earned, how much was spent, and where the money went.

### QUESTION 2: EXPLAIN WHAT EACH CLASS AND FUNCTION DOES.
a. Transaction Class: This class represents a single transaction. The class has three attributes:<br>
- date: The date of the transaction (converted from a string into a Python datetime object).
- amount: The amount of money.
- category: A label for what the transaction was for (for example  "salary", "groceries").<br>

The class has two methods namely:
-  __repr__(): This function returns a single line string representation for a transaction.
- is_expense(): This function returns True if the transaction is an expense (amount < 0), otherwise False.
In summary, the Transaction class is a blueprint for recording details of each transaction.<br>

b. Budget Analyzer Class: This class takes a list of transactions and produces financial insights. The class has one attribute:<br>
i. Transactions: A list of the transactions.
The class has two methods namely:
- total_spent: Adds up all expenses using the is_expense() method from the Transaction class.
- total_earned: Adds up all income using the is_expense() method from the Transaction class.
- pending_by_category: Groups and sums expenses by category (e.g., "groceries: $150", "rent: $500").
- print_summary: This function shows the budget summary with total earned, total spent, and breakdown of spending by category.
In summary the BudgetAnalyzer processes transactions and gives a breakdown of the total money earned, total money spent and spending by category.<br>

c. Load Transaction Function: This function reads the JSON file containing the transactions. It opens the file and loads the data, converts each dictionary (from JSON) into a Transaction object and handles errors like missing file or bad JSON format.<br>
In summary, it turns raw JSON transaction data into a list of Transaction objects.<br>

d. Main function: This is the entry point of the program. It defines the file path to the transactions file and calls the load_transactions function to read the data. If there are no transactions, it warns the user.
Otherwise, it creates a Budget Analyzer and prints a financial summary.<br>
In summary, the main() function runs the whole process from loading data to displaying the budget summary.

### QUESTION 3: DRAW A FLOWCHART OF HOW THE CODE WORKS
![image](flowchart.svg)

The flowchart illustrates the overall process of how the budget analysis code works.
- The program starts by calling the main() function.
- It attempts to load transactions from the transactions.json file using the load_transactions() function.
- If there is an error (such as the file not existing or being in the wrong format), the program logs an error and checks if any valid transactions were loaded.
- If no transactions are available, a warning is logged, and the program ends.
- If transactions are successfully loaded, the program creates a BudgetAnalyzer object using those transactions.
- The analyzer then prints a summary, showing the total amount earned, total spent, and a breakdown of spending by category.
- Finally, the program ends after displaying the results.

### QUESTION 4: WHAT DID YOU LEARN FROM READING THIS?
From reading this code, I picked up a better understanding of how Object Oriented Programming actually works in practice. I got to see how classes, attributes, and methods all come together in a real project. It was also a nice way to brush up on logging and remind myself why it’s more useful than just using print statements. On top of that, I learned how to define functions the right way and make my code more readable and organized.

### QUESTION 5: WHAT DID YOU FIND CLEVER OR CONFUSING?
I didn’t find any part of the code confusing, and that’s actually what I found most clever about it. The way it’s written embodies a lot of best practices and keeps everything so readable. Being able to write code that’s clear, structured, and easy to follow is honestly impressive.

### QUESTION 6: WHAT WOULD YOU DO DIFFERENTLY IF YOU WERE WRITING IT?
If I were writing this myself, I’d add a feature for data visualization, like charts or graphs to show spending by category. I think that would make the insights easier to understand at a glance and a lot more engaging.


## Changes Made To The Project
I extended the Budget Analyzer project by adding new features and making small improvements for better functionality:
- Added a new field (description) to the Transaction class to provide more details about each transaction and updated the code to support it.
- Implemented average_daily_spending() in the BudgetAnalyzer class to calculate how much is spent on average per day.
- Implemented transactions_per_category() in the BudgetAnalyzer class to count the number of transactions under each category.
- Added a simple data visualization method visualize_spending() that displays a bar chart of spending by category for better insight.

