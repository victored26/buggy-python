def lambda_array():
    """Initialize an empty array"""
    lambda_methods = []
    # Implement a for loop to count from 0 to 9
    for j in range(100):
        # Append the lambda function to the array defined above
        lambda_methods.append(lambda x: x + j)
    return lambda_methods