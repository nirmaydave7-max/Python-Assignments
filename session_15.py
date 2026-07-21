def safe_divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("cant divide by zero")
safe_divide(2,1)

try:
    reviews=int(input("enter number of reviews:"))  
    star=int(input("enter stars:"))
    print("average rating=",reviews)
except ValueError:
    print("enter an integer")

def get_playlist_duration(songs):
        print(songs/60,"minutes")
        #if songs<0:
           # raise ValueError("time cannot be negative")
get_playlist_duration(-23)

a=int(input("enter item price:"))
b=int(input("enter qty:"))
try:
     print("total price:",a*b)
except ValueError:
     print("invalid input")
finally:
     print("Thank you for shopping!")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numeric values.")
