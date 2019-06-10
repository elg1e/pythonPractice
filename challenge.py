def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("B") == 1, "This should only be one character"
assert count_upper_case("ABC") <= 3, "This should be less than or equal to three characters"
assert count_upper_case("a") == 1, "It must be upper case"

print("The tests show complete")