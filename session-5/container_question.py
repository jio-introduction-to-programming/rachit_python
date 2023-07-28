def sum_function(input_list: list) -> list:
    """
    Function to take the list as an input and return its sum.\n
    Args:\n
        input_list = list containing numbers.\n
    Returns:
        sum of numbers in list.\n
    """

    sum_numbers = 0
    for i in input_list:
        sum_numbers += i

    return sum_numbers

def max_function(input_list: list) -> int:
    """
    Function to take the list as an input and return its sum.\n
    Args:\n
        input_list = list containing numbers.\n
    Returns:\n
        max of the list.\n
    """

    max_number = input_list[0] # Taking the first index of the list as max
    for i in range(1,len(input_list)):
        if max_number < input_list[i]:
            max_number = input_list[i]

    return max_number

def reverse(input_list: list) -> list:
    """
    Function to take the list as an input and return its reverse.\n
    Args:\n
        input_list = the list to be reversed.\n
    Returns:\n
        reverse the list.\n
    """

    return input_list[::-1]

def sort_list(input_list: list) -> list:
    """
    Function to take the list as an input and return the sorted the list.\n
    Args:\n
        input_list = the list to be sorted.\n
    Returns:\n
        sorted list.\n
    """

    for i in range(len(input_list)):
        swapped = False
        for j in range(len(input_list) - 1 - i):
            if input_list[j] > input_list[j+1]:
                # Swapping
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swapped = True
        
        if not swapped:
            break

    return input_list


def mean_mode(input_list)-> tuple:
    """
    Function to take the input list as an input and return the sorted the list.\n
    Args:\n
        input_list = the list containing numbers whose mean and mode is to be calculated.\n
    Returns:\n
        mean and mode
    """

    if len(input_list)!= 0:
        mean = sum_function(input_list) / len(input_list)
    else:
        raise ZeroDivisionError("Mean and Mode cannot be calculated as the list is empty")
    
    dict_mode = {}
    for i in input_list:
        if i not in dict_mode.keys():
            dict_mode[i] = 1
        else:
            dict_mode[i] += 1

    mode = max(dict_mode, key=dict_mode.get)
    return mean, mode

def problem_six():
    """
    Function to solve the problem number six.\n
    """

    input_string = input("Enter sequence of numbers :- ")
    list_input = list(map(int, input_string.split()))
    
    k = int(input("Enter the integer k :- "))
    result= []
    for i in range(k):
        start_index = int(input("Enter the starting index :-"))
        end_index = int(input("Enter the ending index :-"))

        result.append(sum_function(list_input[start_index: end_index+1]))

    return result
