# DATA-609: Assignment 02
# Ken Noppinger (knoppin1@umbc.edu)
#
# Requirements
#
# Prompt a user to enter 10 integers. 
# If the user enters anything other than integers, remind her that only integers are allowed and let her retry. 
# Don't allow # the user to enter more than 10 or less than 10 integers. 
# Display the 10 integers back to the user at the end. 
# Calculate the following statistics from the 10 # # integers entered:
#
#   Minimum
#   Maximum
#   Range
#   Mean
#   Variance
#   Standard Deviation

def get_input_list(num_elements=10):
    """get_input_list - Prompts user for a list of integers and returns a raw unvalidated list of the inputs"""
    input_string = input(f"Enter {num_elements} integers: ")
    return input_string.split()

def validate_integers(input_list):
    """validate_integers - Verifies if all inputs are integers"""
    valid_status = False
    try:
        for item in input_list:
            item_int = int(item)
        valid_status = True
    except:
        print("Invalid input: Only integers are allowed in the list\n")
    return valid_status    

def validate_list_length(input_list, target_length):
    """validate_list_length - Verifies the length of input list"""
    valid_status = False
    if len(input_list)==target_length:
        valid_status = True
    else:
        print(f"Invalid input: {target_length} integers are required in the list\n")
    return valid_status

def convert_to_integers(valid_list):
    """convert_to_integers - Converts a list of raw inputs into an integer list."""
    integer_list = []
    for num in valid_list:
        integer_list.append(int(num))
    return integer_list

def mean(data):
    """mean - Return the mean of the values in a given input list of data."""
    mean = sum(data) / len(data)
    return mean

def variance(data):
    """variance - Return the variance of the values in a given input list of data."""
    # Mean of the data
    m = mean(data)
    # Square the deviations from the mean for each value in the data
    deviations = [(x - m) ** 2 for x in data]
    # Calculate variance by summing the deviations and dividing by the number of elements in the data
    variance = sum(deviations) / len(data)
    return variance

def std_deviation(data):
    """std_deviation - Return the standard deviation of the values in a given input list of data."""
    # Square root of variance
    std_dev = variance(data) ** .5
    return std_dev

def main():
    
    # Initializations
    valid_inputs = False
    num_integers = 10

    # Collect and validate inputs
    while not valid_inputs:
        inputs = get_input_list(num_integers)
        if validate_integers(inputs) and validate_list_length(inputs, num_integers):
            print("Input validation check successful\n")
            valid_inputs = True
        
    # Convert the validated list of inputs into a list of integers        
    valid_integers_list = convert_to_integers(inputs)

    # Report the minimum, maximum, range, mean, variance, standard deviation, and echo the input list as integers.
    print(f"Minimum\t\t: {min(valid_integers_list)}") 
    print(f"Maximum\t\t: {max(valid_integers_list)}") 
    print(f"Range\t\t: {min(valid_integers_list)} to {max(valid_integers_list)}") 
    print(f"Mean\t\t: {mean(valid_integers_list)}") 
    print(f"Variance\t: {variance(valid_integers_list)}")
    print(f"Std Deviation\t: {std_deviation(valid_integers_list)}") 
    print(f"Integer List\t: {valid_integers_list}")
    
if __name__ == "__main__":
    main()
