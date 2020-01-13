import hottub 

print("How warm do you want the hottub to be?")
try:
    t = float(input())
    hottub.maintain_temp(t-1,t)
except Exception as err:
    print("That's not a number - try again!")
