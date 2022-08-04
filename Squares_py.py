# Program to write squares of a number from 1 through 20

squares = []
for value in range(1,21):
    square = value ** 2
    squares.append(square)

print(squares)
print(max(squares))
print(min(squares))
print(sum(squares))