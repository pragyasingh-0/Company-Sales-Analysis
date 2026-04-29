import numpy as np  
months = np.array(["Jan", "Feb", "March","Apr", "May", "Jun", "Jul","Aug", "Sep", "Oct", "Nov", "Dec"])
sales = []
print("Enter the sales (in 1000$) for each month")

for month in months :
    value = float(input(f"{month}:"))
    sales.append(value)

sales = np.array(sales)
print("\n --- COMPANY SALES ANALYSIS ---")
print("Total Sales Of The Year", np.sum(sales) , "$")
print("Average Monthly Sales", np.mean(sales) , "$")
print("Highest Sales", np.max(sales) , "$")
print("Lowest Sales" , np.min(sales) , "$")

best_month = months[np.argmax(sales)]
worst_month = months[np.argmin(sales)]

print("The Best Month :" ,best_month)
print("The Worst Month: " ,worst_month)


above_average = months[sales > np.mean(sales)]
below_average = months[sales < np.mean(sales)]

print("The Above Average Months :" ,above_average)
print("The Below Average Months :" ,below_average)
