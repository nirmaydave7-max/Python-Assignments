def reverse_string(string):
    if string!=str(string):
        return "no string"
    return string[::-1]
print(reverse_string("hello"))
print("=================================")
def sum_playlist_durations(durations):
    if min(durations)==0:
        return "no duration"
    return sum(durations)
print(sum_playlist_durations([1,2,3,4,5]))
print("=================================")
count = 10
def update_count():
    count=5
    print('Inside:',count)
#this will give 5 as the count is written under function which makes it local variable.
update_count()
print('Outside:', count)
#this  will give 10 as the  count is written before and printed without any function that makes it a global varriable.
"""def  count_likes(posts):
    if sum(posts.values())==0:
        return 0
    return sum(posts.values())
print(count_likes(posts = {
    "post1": {"likes": 100,"replies": { "reply1": {"likes": 15},"reply2": {"likes": 8} }}}))"""
print("=================================")
user_status="online"
print("Before function",user_status)
def status():
    app_status="offline"
    print("app_status:",app_status)
print("Between function",user_status)
status()
print("After function",user_status)
#this demonstrates the  usage of local ad global variable in python.
# global variable gives value throughout the code,whereas local variable gives only inside function because it does not exiat outside function.
print("=================================")





