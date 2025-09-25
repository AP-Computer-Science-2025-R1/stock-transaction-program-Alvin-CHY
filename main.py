Stock_Amount = 1000
Initial_Cost = 32.87
Commission = 0.02
Final_Cost = 33.92

print("Paid for stock =" , Stock_Amount * Initial_Cost)
print("Paid Broker1 =" , Stock_Amount * Initial_Cost * Commission)
First = Stock_Amount * Initial_Cost - Initial_Cost * Stock_Amount * Commission
print("Sold amount =" , Stock_Amount * Final_Cost)
print("Paid Broker2 =" , Stock_Amount * Final_Cost * Commission)
Second = Stock_Amount * Final_Cost - Stock_Amount * Final_Cost * Commission
print("Profit/Loss =" , Second - First)