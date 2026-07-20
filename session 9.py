def calculate_final_price(price, discount_rate):
    final_price=price-price*discount_rate/100
    print(final_price)
calculate_final_price(1200,0.15)
def get_delivery_charge(amount, city='Ahmedabad'):
    if city=='ahmedabad':
        print("delivery charge:30")
    else:
        print("delivery charge:50")
get_delivery_charge(80,'ahmedabad') 
get_delivery_charge(25) 
def  format_coupon_message(username, discount=10):
    print(f" 'Hi {username} you get {discount}% off")



