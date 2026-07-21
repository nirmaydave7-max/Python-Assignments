playlist_prices={
    "playlist_1":450,
    "playlist_2":455,
    "playlist_3":344,
    "playlist_4":993,
    "playlist_5":560
}
print(playlist_prices)
def update_playlist_price(playlist,new_price):
    playlist_prices.update({playlist:new_price})
    print(playlist_prices)
update_playlist_price("playlist_6","344")

del playlist_prices["playlist_3"]
print(playlist_prices)

restaurants_1={"zomato 1","zomato 2","swiggy 1","zomato 4","zomato 5"}
restaurants_2={"swiggy 1","swiggy 2","swiggy 3","swiggy 4","zomato 2"}
print (restaurants_1.union(restaurants_2))
print(restaurants_1.intersection(restaurants_2))
