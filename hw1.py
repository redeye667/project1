# Function №1
def is_diagonal(matrix):
    # Loop through the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # If any off-diagonal element is not zero, return False
            if i != j and matrix[i][j] != 0:
                return False
    return True

# Function №2
def is_upper_triangular(matrix):
    # Loop through the elements below the main diagonal
    for i in range(1, len(matrix)):
        for j in range(i):
            # If any element below the main diagonal is not zero, return False
            if matrix[i][j] != 0:
                return False
    return True

# Function №3
def contains(matrix, value):
    for row in matrix:
        if value in row:
            return True
    return False

# Function №4
def biggest(matrix):
    # Initialize the maximum value with the first element of the matrix
    max_value = matrix[0][0]

    # Traverse through each row
    for row in matrix:
        # Traverse through each element in the row
        for value in row:
            # Update the maximum value if the current value is greater
            if value > max_value:
                max_value = value

    return max_value

# Function №5
def indices_biggest(matrix):
    # Initialize the initial values for the maximum and its indexes
    max_value = matrix[0][0]
    max_indices = [0, 0]

    # Go through all the elements of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # If a new maximum value is found
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_indices = [i, j]

    return max_indices

# Function №6 (Corrected)
def second_biggest(matrix):
    # Flatten the matrix into a single list
    flat_list = [item for sublist in matrix for item in sublist]

    # Find the unique elements and sort them in descending order
    unique_elements = sorted(set(flat_list), reverse=True)

    # Check if there's more than one unique element
    if len(unique_elements) > 1:
        # Check if the largest value occurs more than once
        if flat_list.count(unique_elements[0]) > 1:
            return unique_elements[0]  # Return the largest value as the second largest
        else:
            return unique_elements[1]  # Otherwise, return the second largest value
    else:
        return unique_elements[0]  # If only one unique element exists

# Function №7
def indices_second_biggest(matrix):
    # Flatten the matrix to a 1D list
    flat_matrix = [item for sublist in matrix for item in sublist]

    # Find the unique elements and sort them in descending order
    unique_sorted_values = sorted(set(flat_matrix), reverse=True)

    # Determine the second largest value
    if len(unique_sorted_values) > 1:
        second_largest = unique_sorted_values[1]
    else:
        second_largest = unique_sorted_values[0]

    # Find the indices of the second largest value in the original matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == second_largest:
                return [i, j]
    return [0, 0]

# Function №8
def substr_in_values(d, substr):
    result_keys = []
    substr_lower = substr.lower()

    for key, values in d.items():
        if any(substr_lower in value.lower() for value in values):
            result_keys.append(key)

    result_keys.sort()  # Sort the list of keys
    return result_keys

# Function №9
def indices_divisible_by_3(matrix):
    result = []
    for i in range(len(matrix)):  # External loop by lines
        for j in range(len(matrix[i])):  # Internal loop by columns
            if (i + j) % 3 == 0:  # Checking the divisibility of the sum of indices by 3
                result.append(matrix[i][j])
    return result

# Function №10
def sort_int_string(s: str) -> str:
    # Remove the extra spaces and divide the string into separate numbers
    numbers = s.split()

    # Convert strings to integers and sort them
    sorted_numbers = sorted(map(int, numbers))

    # Convert the sorted numbers back into strings and connect them separated by a space
    return ' '.join(map(str, sorted_numbers))

# Function №11
def dups_lol(lol):
    # Use a set to track unique values
    seen = set()
    # Go through each item in the list of lists
    for row in lol:
        for item in row:
            # If the element is already in the set, return True
            if item in seen:
                return True
            # Otherwise, add the element to the set
            seen.add(item)

    # If no duplicates are found, return False
    return False

# Function №12
def dups_dict(d):
    seen = set()  # Set to store seen values
    for key, values in d.items():
        for value in values:
            if value in seen:  # If value is already seen, return True
                return True
            seen.add(value)  # Otherwise, add the value to the set
    return False  # Return False if no duplicates are found
