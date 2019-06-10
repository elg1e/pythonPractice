def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("ABC") == 3, "Three upper case"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%^") == 0, "Special characters"
assert count_upper_case("AB") <= 2, "Less than or equal to two characters"
assert count_upper_case("ABC") >= 3, "More than or equal to Three characters"
assert count_upper_case("1") == 1, "This is the number one, not the letter 'l'"

print("All the tests passed")