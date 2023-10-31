import csv
from random import choice
import matplotlib.pyplot as plt

print("BUDGET TRACKER\n")

print("Enter amount of money spent on each category\nAlso reply with Y/N if asked.\n")

tips = {
    "Food": ["Avoid fast food", "Do not go for shopping empty stomach", "Cook at home more often", "Plan meals ahead"],
    "Travel": ["Use public transport", "Look for travel deals", "Book flights in advance", "Stay in budget accommodations"],
    "Shopping": ["Make a shopping list", "Wait for sales and discounts", "Compare prices before buying", "Avoid impulsive purchases"],
    "HealthCare": ["Use generic medicines", "Opt for preventive care", "Shop around for healthcare services", "Maintain a healthy lifestyle"],
    "Miscellaneous": ["Limit impulse purchases", "Track small expenses", "Cancel unused subscriptions", "DIY whenever possible"]
}

spend_analytics = ["Food", "Travel", "Shopping", "HealthCare", "Miscellaneous", "Savings"]

spending_data = {}

# Asks user for income
income = float(input("Enter your income: "))

# We use [:-1] to Exclude "Savings"
for category in spend_analytics[:-1]:  
    amount = float(input(f"Enter spending on {category}: "))
    spending_data[category] = amount

total_spending = sum(spending_data.values())
savings = income - total_spending
spending_data["Savings"] = savings

percentages = {}
for category, amount in spending_data.items():
    percentage = (amount / income) * 100
    percentages[category] = percentage

# Display spending analysis
print("\nSpending Analysis:")
for category, percentage in percentages.items():
    print(f"{category}: {percentage:.2f}% of total income")

print(f"\nTotal Income: {income}")
print(f"Total Savings: {savings}\n")

major_spending_category = max(percentages, key=percentages.get)
if major_spending_category in tips:
    random_tip = choice(tips[major_spending_category])
    print(f"Tip for {major_spending_category}: {random_tip}")

save_csv = input("Do you want to save to CSV? (Y/N): ")
if save_csv.lower() in ["yes",'y']:
    with open('spending_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Amount'])
        writer.writerow(['Income', income])
        for category, amount in spending_data.items():
            writer.writerow([category, amount])

show_pie_chart = input("Do you want to view the pie chart? (Y/N): ")
if show_pie_chart.lower() in ["yes",'y']:
    labels = list(percentages.keys())
    sizes = list(percentages.values())

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.title("Spending Breakdown")
    plt.show()
