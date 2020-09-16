is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male and are tall")
    # else if # not(is_tall)cit negates the statement
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male neither tall")


# Comparison
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:  # != not equal to
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 4, 5))
