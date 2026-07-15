#cust detail: regular - membership, phone no., amount, GST, offer, 2000+membership = offer, category?

# user input
cust_name = input("Enter customer name: ")
cust_age = int(input("Enter customer age: "))
product_name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))
membership = input("Is the customer a member? (yes/no): ").lower()
payment_method = input("Enter payment method: ").lower()

# data type checking
print("\n------ Data Type ------")
print("Customer_name:",type(cust_name))
print("Customer_age:",type(cust_age))
print("Product_name:",type(product_name))
print("Quantity:",type(quantity))
print("Price:",type(price))
print("Membership:",type(membership))
print("Payment_method:",type(payment_method))

# data type conversion
#  qty as float, price as int, age as string, price as string
quantity_float = float(quantity)
price_int = int(price)
age_str = str(cust_age)
price_str = str(price)

print("\n------ Data Type Conversion ------")
print("Quantity as float:",quantity_float, type(quantity_float))
print("Price as int:",price_int, type(price_int))
print("Age as string:",age_str, type(age_str))
print("Price as string:",price_str, type(price_str))

# arithmetic operation 
total_price = quantity * price

# user defined function 1
def calculate_discount(total, member):
    if member == "yes":
        return total * 0.10
    else:
        return total * 0.05
    
# user defined function 2
def calculate_gst(total):
    return total * 0.18

# user defined function 3
def sales_insights(final_amount):
    # if final_amount >= 8000:
    #     return "High value sale"
    # elif final_amount >= 3000:
    #     return "Medium value sale"
    # else:
    #     return "Low value sale"
    
    return lambda final_amount: "High value sale" if final_amount >= 8000 else "Medium value sale" if final_amount >= 3000 else "Low value sale"

# function call 
discount = calculate_discount(total_price, membership)
gst = calculate_gst(total_price - discount)
final_amount = total_price - discount + gst

# customer rank
if final_amount >=10000:
    category = "Diamond Customer"
elif final_amount >=5000:
    category = "Gold Customer"
elif final_amount >=2000:
    category = "Silver Customer"
else:
    category = "Regular Customer"

# reward system
if membership == "yes":
    if final_amount >= 5000:
        reward = "Free Gift Voucher"
    else:
        reward = "100 reward points"
else:
    if final_amount >= 5000:
        reward = "Invite for Membership"
    else:
        reward = "Thank you for shopping"

# payment validation
# if payment_method not in ["cash", "card", "upi"]:
#     print("Invalid payment method. Please choose from cash, card, or UPI.")\
if payment_method == "upi":
    payment_status = "Instant Payment"
elif payment_method == "card":
    payment_status = "Card Verified"
elif payment_method == "cash":
    payment_status = "Cash Received"
else:
    payment_status = "Invalid payment method. Please choose from cash, card, or UPI."

# final bill
print("\n------ Billing Details ------")
print("Customer Name:", cust_name)
print("Customer Age:", cust_age)
print("Product Name:", product_name)
print("Quantity:", quantity)
print("Price per unit:", price)
print("Total Price:", total_price)
print("Membership:", membership)
print("Discount:", discount)
print("GST:", gst)
print("Final Amount to be paid:", final_amount)

print("\n------ Customer Insights ------")
print("Sales Insights:", sales_insights(final_amount))
print("Customer Category:", category)
print("Payment Method:", payment_method)
print("Payment Status:", payment_status)
print("Customer Category:", category)
print("Reward:", reward)