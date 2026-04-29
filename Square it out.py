squares = [1,2,3,4,5,6,7,8,9,10]
print("List of squares values:", squares)

odd_squares = [num for num in squares if num % 2 != 0 ]
even_squares = [num for num in squares if num % 2 == 0]
print("Odd squares:", odd_squares)
print("Even squares:", even_squares)
