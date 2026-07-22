trending_movies=["movie_1","movie_2","movie_3","movie_4","movie_5"]
it=iter(trending_movies)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

songs=["song_1","song_2","song_3","song_4","song_5","song_6"]
for i,song in enumerate(songs):
    print(i,song)

food_items=["item 1","item 2","item 3"]
prices=[250,300,150]
a=zip(food_items,prices)
print(list(a))

def insta_posts_generator(posts):
    for post in posts:
        yield post

posts = ["Morning Coffee ☕", "Gym Time 💪", "Sunset 🌅"]

gen = insta_posts_generator(posts)

try:
    while True:
        print(next(gen))
except StopIteration:
    print("No more post captions.")

def cashback_generator(transactions):
    for transaction in transactions:
        yield transaction*5/100

gen=cashback_generator([500,4000,200,100000])
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))