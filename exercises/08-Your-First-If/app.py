
total = int(input('How much money do you have in your pocket\n'))

# YOUR CODE HERE


if(total > 100):
    answer = "Give me your money!"

elif(total > 50):
    answer = "Buy me some coffee you cheap!"

else:
    answer = "You are a poor guy, go away!"

print(answer)