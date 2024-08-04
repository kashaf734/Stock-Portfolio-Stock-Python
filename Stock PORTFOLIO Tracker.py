import yfinance as yf
import pandas as pd
from datetime import datetime

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity):
        if ticker in self.portfolio:
            self.portfolio[ticker]['quantity'] += quantity
        else:
            stock_data = yf.Ticker(ticker)
            self.portfolio[ticker] = {
                'quantity': quantity,
                'purchase_date': datetime.now().strftime('%Y-%m-%d'),
                'current_price': stock_data.history(period='1d')['Close'][0]
            }

    def remove_stock(self, ticker, quantity):
        if ticker in self.portfolio:
            if self.portfolio[ticker]['quantity'] >= quantity:
                self.portfolio[ticker]['quantity'] -= quantity
                if self.portfolio[ticker]['quantity'] == 0:
                    del self.portfolio[ticker]
            else:
                print(f"Not enough quantity to remove. You have {self.portfolio[ticker]['quantity']} shares.")
        else:
            print("Stock not found in portfolio.")

    def update_prices(self):
        for ticker in self.portfolio:
            stock_data = yf.Ticker(ticker)
            self.portfolio[ticker]['current_price'] = stock_data.history(period='1d')['Close'][0]

    def view_portfolio(self):
        self.update_prices()
        portfolio_df = pd.DataFrame.from_dict(self.portfolio, orient='index')
        print(portfolio_df)

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter stock ticker: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(ticker, quantity)
        elif choice == '2':
            ticker = input("Enter stock ticker: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(ticker, quantity)
        elif choice == '3':
            portfolio.view_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
