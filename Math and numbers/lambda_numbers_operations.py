def lambda_numbers(num1, num2, arr):
    sum_numbers = lambda num1, num2: num1 + num2
    print("Sum:", sum_numbers(num1, num2))

    square_number = lambda num1: num1 * num1
    print("Square:", square_number(num1))

    sum_elements = lambda nums: sum(nums)
    print("Sum of array elements:", sum_elements(arr))

    max_element = lambda nums: max(nums)
    print("Maximum in array:", max_element(arr))

    squares = list(map(lambda num1: num1 ** 2, range(10)))
    squares = [num1 ** 2 for num1 in range(10)]  # same as above


lambda_numbers(2, 3, [1, 2, 3, 4, 5])
