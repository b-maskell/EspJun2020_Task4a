import pandas as pd
import datetime
import matplotlib.pyplot as plt


def profit_loss_menu():

    flag = True
    
    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show profit/loss for specific products")
        print("2. Show profit/loss for all products")
        print("###############################################")

        profit_loss_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(profit_loss_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(profit_loss_choice) < 1 or int(profit_loss_choice) > 2:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return int(profit_loss_choice) 



def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a product form the list:")
        print("Please enter the number of the product (1-16)")
        print("1.  Potatoes")
        print("2.  Carrots")
        print("3.  Peas")
        print("4.  Lettuce")
        print("5.  Onions")
        print("6.  Apples")
        print("7.  Oranges")
        print("8.  Pears")
        print("9.  Lemons")
        print("10. Limes")
        print("11. Melons")
        print("12. Cabbages")
        print("13. Asparagus")
        print("14. Broccoli")
        print("15. Cauliflower")
        print("16. Celery")
        print("######################################################")

        product_list = ["Potatoes", "Carrots", "Peas", "Lettuce", "Onions", 
"Apples", "Oranges", "Pears", "Lemons", "Limes","Melons", "Cabbages", 
"Asparagus", "Broccoli", "Cauliflower", "Celery"]

        product_choice = input("Please enter the number of your choice (1-16): ")

        try:
            int(product_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(product_choice) < 1 or int(product_choice) > 16:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                product_name = product_list[int(product_choice)-1]
                return product_name



def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Plese enter start date for your time range (DD/MM/YYYY): ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return pd.to_datetime(start_date, dayfirst=True)


def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Plese enter end date for your time range (DD/MM/YYYY): ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return pd.to_datetime(end_date, dayfirst=True)



def get_date_range_all():
    df1 = pd.read_csv("Task4a_data.csv") 
 
    # Convert Date column's type from String to DateTime so can do date comparisions
    df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True)

    results = df1.loc[(df1["Date"] >= start_date) & (df1["Date"] <= end_date), df1.columns != "Supplier"].copy()
    
    results["Cost Subtotal"] = results["KGs Purchased"] * results["Purchase Price"]
    results["Sales subtotal"] = results["KGs Sold"] * results["Selling Price"]
    results["Profit subtotal"] = results["Sales subtotal"] - results["Cost Subtotal"]
    
    total = round(results["Profit subtotal"].sum(),2)
    results_print = results.to_string(index=False)
    
    print(results_print)
    print("The overall profit/loss for the selected time frame was £{}".format(total))



def get_date_range_product():
    product_name = get_product_choice()
    df2 = pd.read_csv("Task4a_data.csv") 

    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True)
   
    product_results = df2.loc[(df2["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Product"] == product_name)].copy()

    product_results["Cost Subtotal"] = product_results["KGs Purchased"] * product_results["Purchase Price"]
    product_results["Sales subtotal"] = product_results["KGs Sold"] * product_results["Selling Price"]
    product_results["Profit subtotal"] = product_results["Sales subtotal"] - product_results["Cost Subtotal"]
    
    total = round(product_results["Profit subtotal"].sum(),2)
    results_print = product_results.to_string(index=False)
    
    print(results_print)
    print("The profit/loss for the {} for selected time frame was £{}".format(product_name, total))


def process_menu_choice():

    if profit_choice == 1:
        get_date_range_product()
    else:
        get_date_range_all()




def get_supplier_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a supplier form the list:")
        print("Please enter the number of the supplier (1-5)")
        print("1.  Clean Living")
        print("2.  Farm Direct")
        print("3.  Grocers Int.")
        print("4.  Natural Best")
        print("5.  Nature Food")
        print("######################################################")

        product_list = ["Clean Living", "Farm Direct", "Grocers Int.", "Natural Best", "Nature Food" ]

        product_choice = input("Please enter the number of your choice (1-5): ")

        try:
            int(product_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(product_choice) < 1 or int(product_choice) > 5:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                product_name = product_list[int(product_choice)-1]
                return product_name



def qty_products_by_supplier():
    """
    For a specified supplier and product print the qty sold over a time period
    """
    df2 = pd.read_csv("Task4a_data.csv")
    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True)

    # Remove unneeded columns (use inplace to make changes in existing dataframe)
    df2.drop(columns=["KGs Purchased", "Purchase Price", "Selling Price"], inplace=True)

    # Get user choices
    supplier = get_supplier_choice()
    product = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
        
    # Create row filter to extract rows that match what user specified and store in new df product_results
    row_mask = (df2["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Product"] == product) & (df2["Supplier"] == supplier)
    product_results = df2.loc[row_mask]

    # Can sort existing df using inplace=True instead of creating a new df
    sorted_results = product_results.sort_values(by="Date")
    
    # Also calculate the total quantity sold for period for potentially extra marks
    qty_sum = sorted_results["KGs Sold"].sum()

    # Print out results
    print("\n\n================================================")
    print("REPORT FOR QTY SOLD OVER TIME")
    print(f"Supplier={supplier}, Product={product}, Start={start_date}, End={end_date}")

    print("\n\nPRODUCTS SOLD OVER TIME TREND")
    print(sorted_results)
    print(f"\nTOTAL PRODUCTS SOLD OVER TIME PERIOD = {qty_sum}")
    print("================================================")

    product_results.plot.bar(x="Date", y="KGs Sold")
    plt.title("Qty Sold Trend for Product and Supplier")
    plt.xlabel("Date")
    plt.ylabel("Qty Sold")
    plt.show()


def profit_by_product_supplier():
    """
    For a specified supplier and product print the profit over a time period
    """
    df2 = pd.read_csv("Task4a_data.csv")
    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True)

    df2["Profit"] = (df2["Selling Price"] * df2["KGs Sold"]) - (df2["Purchase Price"] * df2["KGs Purchased"])
 
    # Remove unneeded columns (use inplace to make changes in existing dataframe)
    df3 = df2.drop(columns=["KGs Purchased", "Purchase Price", "Selling Price", "KGs Sold"])

    # Get user choices
    supplier = get_supplier_choice()
    product = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
        
    # Create row filter to extract rows that match what user specified and store in new df product_results
    row_mask = (df3["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Product"] == product) & (df2["Supplier"] == supplier)
    product_results = df3.loc[row_mask]

    # Can sort existing df using inplace=True instead of creating a new df
    sorted_results = product_results.sort_values(by="Date")
    
    # Also calculate the total quantity sold for period for potentially extra marks
    profit_sum = sorted_results["Profit"].sum()

    # Print out results
    print("\n\n================================================")
    print("REPORT FOR PROFIT FOR PRODUCT/SUPPLIER OVER TIME")
    print(f"Supplier={supplier}, Product={product}, Start={start_date}, End={end_date}")

    print("\n\nPROFIT OVER TIME TREND")
    print(sorted_results)
    print(f"\nTOTAL TOTAL PROFIT OVER TIME PERIOD = {profit_sum}")
    print("================================================")

    product_results.plot.bar(x="Date", y="Profit")
    plt.title("Qty Sold Trend for Product and Supplier")
    plt.xlabel("Date")
    plt.ylabel("Profit")
    plt.show()



# main program
while True:

    print(
"""\n\nMENU OPTIONS
(1) Qty of products sold by specified supplier
(2) Profit on products by specified supplier
(3) Profit/Loss for time period
(4) Exit Program
""")

    choice = input("Enter option 1 to 4: ")

    if choice == "1":
        qty_products_by_supplier()
    elif choice == "2":
        profit_by_product_supplier()
    elif choice == "3":
        start_date = get_start_date()
        end_date = get_end_date()
        profit_choice = profit_loss_menu()
        process_menu_choice()
    elif choice == "4":
        print("\n\n GOODBYE")
        exit()
    else:
        print("\nBad Choice - pls re-enter\n")


    




