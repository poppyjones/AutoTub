from hottub import maintain_temp 

print("How warm do you want the hottub to be?")
try:
    t = float(input())
    maintain_temp(t-1,t)
except Exception as err:
    print("That's not a number - try again!")
