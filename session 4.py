name=str(input("enter product name"))
print(name.upper())
print(name.lower())
clean_brand_name=name.strip()
final=clean_brand_name.replace("-"," ")
print(final)
phone="Apple iphone14 pro max"
print(phone[0:5])
print(phone[6:22])
def format_product_display(name,price):
    print(f"{name}-₹{price}")
format_product_display("boat earbuds","1299")
products=[' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']
space_remove=[item.strip() for item in products]
replacement=[item.replace("-"," ") for item in space_remove]
capital=[[word.upper() if word.lower in ['mi','samsung','realme'] else word for word in item] for item in replacement]
print(capital)
