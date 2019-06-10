def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else:
        evens = 0
        
        
    for number in numbers:
        if number % 2 == 0:
            evens += 1
            
    if evens == 0:
        return False
    else:
        return evens % 2 == 0

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")


"""

Write a function that accepts a list of numbers and returns True 
if the list contains an even number of even numbers.

If the list has no numbers or 0, return False.
If the list has odd numbers, return False.
If the list has a odd number of even numbers, return False.
If the list has a even number of evens numbers, return True.

"""