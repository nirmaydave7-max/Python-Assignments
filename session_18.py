import re
text = """
Call me at 9876543210.
Office: 8123456789.
Old number: 6123456789.
Customer care: 7012345678.
Price is ₹2500.
Order ID: OD12345.
Emergency: 9988776655.
Random number: 1234567890.
WhatsApp: 7654321098.
"""
phone_number=re.findall(r"\b[7,8,9]\d{9}\b",text)
print(phone_number)

text_2 = """
Meeting Date: 25/06/2024
Delivery expected next week.
Invoice generated successfully.
"""
match=re.search(r'\b\d{2}/\d{2}/\d{4}\b',text_2)
print(match)

review = """
Contact us at support@zomato.com
Manager: raj123@gmail.com
Feedback: user.test@yahoo.in
Invalid email: abc@gmail
Another email: customer_service@outlook.com
"""
find_reviews=re.findall(r'\S+@\S+',review)
print(find_reviews)

text_3 = """
Customer 1: 9876543210

"""
masked = re.sub(r"^(?:\D*\d){7}(.*)", r"*******\1", text_3)
print(masked)

orders = [
    "OD12345678901234500",
    "OD98765432109876543",
    "OD11112222333344445",
    "AB12345678901234500",
    "OD12345",
    "OD1234567890ABCDE12"
]

pattern = r"^OD\d{17}$"

for order in orders:
    if re.search(pattern, order):
        print(order, "-> Valid Order ID")
    else:
        print(order, "-> Invalid Order ID")
