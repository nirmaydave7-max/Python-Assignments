age=int(input("enter age:"))
if age >=18:
    print("eligible  for IPL ticket booking")
else:
    print("Not eligible")
print("==================================")
followers=int(input("enter number of followers"))
if followers<10000:
    print("micro influencer")
elif followers>=10000 and followers<100000:
    print("rising star")
else:
    print("celebrity")
print("==================================")
total=int(input("enter total of zomato  order"))
if total>=299:
    print("apply free delivery")
elif total>200 and total<299:
    print("add more items to get free delivery")
else:
    print("delivery charges apply")
print("==================================")
value=int(input("enter flipkart order value"))
payment_method=input("enter payment method")
if value>1000:
    if payment_method=="UPI":
        print("elgible for 10% cashback")
if value>1000:
    if payment_method!="UPI":
        print("eligible for 5% cashback")
else:
    print("no cashback")
print("==================================")



