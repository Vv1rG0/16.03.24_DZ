height = 5
i = 1
while i <= height:
    spaces = height - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)
    i += 1