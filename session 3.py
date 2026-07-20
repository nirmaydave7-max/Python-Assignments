number_of_followers=int(input("enter number of followers"))
average_rating=float(input("enter average_rating"))
app_name=str(input("enter favourite app name"))
is_premium_user=bool(input("are you a premium user?true or false"))
print(type(number_of_followers))
print(type(average_rating))
print(type(app_name))
print(type(is_premium_user))
price_of_order=str(input("enter price of your zomato order"))
price_of_order=float(price_of_order)
tax=price_of_order*18/100+price_of_order
print("final bill amount:",tax)
product_price=['199.99', '299.50', '150']
product_price_flipkart=[float(x) for x in product_price]
total=sum(product_price_flipkart)
print("sum:",total)
def is_discount_applicable(order_amount):
    if order_amount>500:
        print("true")
    else:
        print("false")
is_discount_applicable(450)
is_discount_applicable(750)
spotify_ratings=['4.5', '3.0', '5', '4.2']
ratings=[float(x) for x in spotify_ratings]
print(ratings)
