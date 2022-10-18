#python program that reverses your name
user_input = input('Enter space-separated characters and use "_" to indicate space: ') #example: G a b r i e l _ S . _ C a t a n a o a n

array = user_input.split()
array.reverse()
for i in array:
    print(i, end="")
