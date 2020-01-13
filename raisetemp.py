from hottub import raise_temp

print("How warm do you want the hottub to be?")
try:
    t = float(input())
    raise_temp(t)
except Exception as err:
    print("That's not a number - try again!")