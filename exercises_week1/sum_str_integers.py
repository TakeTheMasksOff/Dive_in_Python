def sum_integers_in_str(digit_string):
    print(digit_string)
    sum=0
    for letter in digit_string:
        sum += int(letter)
    print(sum)

