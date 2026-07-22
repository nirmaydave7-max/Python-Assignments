add_gst=lambda price: price*1.18
print(add_gst(100))
print(add_gst(250))
print(add_gst(500))

song_titles=(["SHApe  of You","hONEY PIE","Mocking bird"])
song=list(map(lambda x:x.strip().upper(),song_titles))
print(song)

products = [
    "Samsung Galaxy",
    "Apple iPhone",
    "sony Headphones",
    "Boat Speaker",
    "smart Watch",
    "Redmi Phone",
    "Sandisk Pendrive"
]
s_products=list(filter(lambda x:x.lower().startswith('s'),products))
print(s_products)

from functools import reduce
order_amounts= [120, 340, 560, 80]
results=reduce(lambda x,y:x+y,order_amounts)
print(results)

from functools import reduce

numbers = [40, 60, 80, 120]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print("After map():", doubled)

# Keep only numbers greater than 100
filtered = list(filter(lambda x: x > 100, doubled))
print("After filter():", filtered)

# Sum all remaining numbers
total = reduce(lambda x, y: x + y, filtered)
print("After reduce():", total)

