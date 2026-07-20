playlist_ids=[45,56,67,89,34]
playlist_ids.append(23)
print(playlist_ids)
cart_items=['t-shirt', 'shoes']
cart_items.extend(['jeans','cap'])
print(cart_items)
def remove_last_item(order_list):
    remove_item=order_list.pop(-1)
    print(remove_item)
remove_last_item(['a','b','c','d'])
insta_filters=('Clarendon','Juno','Not So Basic','Inkwell')
#insta_filters[1]="Valencia"
print(insta_filters)
#this gives a type error because tupples are not mutable like lists and thus it cannot be updated.
#=================================================================================================#
#Q5 for first scenerio "list" should be used as the favourite genres because the lists are mutable and thus change can bee possible.
#Q5 for second scenerio "tupple" should be used because the tain coaches are not required to be changed and thus tupples are non mutable.
    