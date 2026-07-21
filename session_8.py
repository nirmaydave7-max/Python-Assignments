order_amounts=[120, 250, 90, 310, 150]
total_sum=0
for i in order_amounts:
    total_sum=i+total_sum
    print(total_sum)
print("===============================")
cricket_scores=[45, 78, 102, 34, 67, 89]
i=0
while i<len(cricket_scores):
    print(cricket_scores[i])
    if cricket_scores[i]>=100:
        break
    i+=1
print("===============================")
Flipkart_cart=[299, 499, 199, 999, 149]
total_sum=0
for i in Flipkart_cart:
    total_sum=total_sum+i
    if i<=200:
        continue
    print(total_sum)
print("===============================")
favorite_song=['Kesariya', 'Believer', 'Shape of You', 'Blinding Lights', 'Excuses']
for index,favorite_song in enumerate(favorite_song):
    print(index,favorite_song)
print("===============================")
Instagram_follower_counts=[120, 1500, 23000, 800, 45000]
for i in Instagram_follower_counts:
    if i<=1000:
        print("micro")
    elif i>1000 and i<10000:
        print("influencer")
    else:
        print("celebrity")