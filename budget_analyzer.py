import json
import logging
from datetime import datetime
from typing import List, Dict
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)


class Transaction:
    """
    Represents a financial transaction.
    """

    def __init__(self, date: str, amount: float, category: str, description: str):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.amount = amount
        self.category = category
        
        # Adding a new attribute, description
        self.description = description or "No description"

    def __repr__(self):
        return f"<Transaction {self.amount} {self.category} on {self.date.date()} - {self.description}>"  # noqa: E501

    def is_expense(self):
        return self.amount < 0


class BudgetAnalyzer:
    """
    Analyzes a list of transactions to produce financial insights.
    """

    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions

    def total_spent(self) -> float:
        return sum(t.amount for t in self.transactions if t.is_expense())

    def total_earned(self) -> float:
        return sum(t.amount for t in self.transactions if not t.is_expense())

    def spending_by_category(self) -> Dict[str, float]:
        summary = {}
        for t in self.transactions:
            if t.is_expense():
                summary[t.category] = summary.get(t.category, 0) + abs(t.amount)  # noqa: E501
        return summary
    
    # Adding the extra functions: average_daily_spending, transactions_per_category and visualize_spending.
    
    def average_daily_spending(self) -> float:
        """
        Calculate the average daily spending across unique days.
        """
        daily_spending = {}
        for t in self.transactions:
            if t.is_expense():
                day = t.date.date()
                daily_spending[day] = daily_spending.get(day, 0) + abs(t.amount)
        if not daily_spending:
            return 0.0
        return sum(daily_spending.values()) / len(daily_spending)
    
    def transactions_per_category(self) -> Dict[str, int]:
        """
        Count the number of transactions in each category.
        """
        counts = {}
        for t in self.transactions:
            counts[t.category] = counts.get(t.category, 0) + 1
        return counts

    def visualize_spending(self):
        """
        Show a bar chart of spending by category.
        """
        data = self.spending_by_category()
        if not data:
            logging.warning("No spending data to visualize.")
            return
        categories, amounts = list(data.keys()), list(data.values())
        plt.bar(categories, amounts)
        plt.title("Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount Spent ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def print_summary(self):
        logging.info("------ Budget Summary ------")
        logging.info(f"Total Earned: ${self.total_earned():.2f}")
        logging.info(f"Total Spent:  ${abs(self.total_spent()):.2f}")
        logging.info(f"Average Daily Spending: ${self.average_daily_spending():.2f}")
        logging.info("Spending by Category:")
        for category, amount in self.spending_by_category().items():
            logging.info(f"  {category}: ${amount:.2f}")
        logging.info("Transactions per Category:")
        for category, count in self.transactions_per_category().items():
            logging.info(f"  {category}: {count} transactions")


def load_transactions(filepath: str) -> List[Transaction]:
    """
    Load transactions from a JSON file.
    JSON format:
    [
        {"date": "2024-05-01", "amount": -50.25, "category": "groceries"},
        {"date": "2024-05-02", "amount": 2000.00, "category": "salary"}
    ]
    """
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return [Transaction(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Failed to load transactions: {e}")
        return []


def main():
    filepath = "transactions.json"
    transactions = load_transactions(filepath)

    if not transactions:
        logging.warning("No transactions to analyze.")
        return

    analyzer = BudgetAnalyzer(transactions)
    analyzer.print_summary()
    # Print the visual
    analyzer.visualize_spending()


if __name__ == "__main__":
    main()
