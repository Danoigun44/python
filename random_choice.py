# code to determine if a user guess is same as computer random guess
import random
car = ["benz", "bmw", "porche", "toyota", "volvo", "honda"]

random_car = random.choice(car)

user_favorite = input("What is your favorite car? ")

if user_favorite.lower() == random_car:
    print(f"Yes, that is correct! {random_car.capitalize()} is my favorite car.")
else:
    print("Wrong guess, you have one more chance.")
    # Second attempt
    user_favorite = input("Try again! What is your favorite car? ") 
    if user_favorite.lower() == random_car:
        print(f"Yes, that is correct! {random_car.capitalize()} is my favorite car.")
    else:
        print(f"Wrong again! My favorite car was {random_car.capitalize()}.")
