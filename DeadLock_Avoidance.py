# input matrix {claim, allocation}
def matrix_input(row, column, matrix_name):
    print(matrix_name)
    matrix = [[0] * column for i in range(row)]

    for _row in range(row):
        print("Row(" + str(_row + 1) + "):")
        for _column in range(column):
            element = int(input("Enter element(" + str(_column + 1) + ") :"))
            matrix[_row][_column] = element
    print("----------------------------------------")
    return matrix


# calculate needed matrix resource
def calc_needed_matrix(claim_matrix, allocation_matrix):
    matrix = [[0] * len(claim_matrix[0]) for i in range(len(claim_matrix))]

    for _row in range(len(claim_matrix)):
        for _column in range(len(claim_matrix[_row])):
            matrix[_row][_column] = claim_matrix[_row][_column] - allocation_matrix[_row][_column]
    return matrix


# input resource
def resource_input(length, list_name):
    print(list_name)
    lis = [0] * length
    for item in range(length):
        element = int(input("Enter element(" + str(item + 1) + "):"))
        lis[item] = element
    print("----------------------------------------")
    return lis


# print matrix {claim, needed, allocation}
def matrix_print(matrix1, name1, matrix2, name2, matrix3, name3):
    length = 0
    temp_len = 0
    element_string = name1

    for item in range(len(name3)):
        element_string += " "
    element_string += name3
    for item in range(len(name3)):
        element_string += " "
    element_string += name2 + "\n"

    for _row in range(len(matrix1)):
        for _column in range(len(matrix1[_row])):
            element_string += str(matrix1[_row][_column]) + " "
            temp_len += len(str(matrix1[_row][_column])) + 1

        length = len(name1) - temp_len + len(name3)
        for item in range(length):
            element_string += " "
        temp_len = 0

        for _column in range(len(matrix3[_row])):
            element_string += str(matrix3[_row][_column]) + " "
            temp_len += len(str(matrix3[_row][_column])) + 1

        length = len(name3) - temp_len + len(name3)
        for item in range(length):
            element_string += " "
        temp_len = 0

        for _column in range(len(matrix2[_row])):
            element_string += str(matrix2[_row][_column]) + " "
        temp_len = 0

        element_string += "\n"
    print(element_string)
    print("----------------------------------------")


# print resource
def print_resource(res_list, name1, available_res, name2):
    lis_elements = name1
    temp_len = 0

    for item in range(len(name2)):
        lis_elements += " "
    lis_elements += name2 + "\n"

    for item in range(len(res_list)):
        lis_elements += str(res_list[item]) + " "
        temp_len += len(str(res_list[item])) + 1

    length = len(name1) - temp_len + len(name2)
    for item in range(length):
        lis_elements += " "

    for item in range(len(available_res)):
        lis_elements += str(available_res[item]) + " "

    print(lis_elements)
    print("----------------------------------------")


# check if the example is safe or not
def check_safe_or_not(resource, available_matrix, allocated_matrix):
    # the condition true when resource[index] = available_matrix[index] + summation of (allocated[_row][_column])
    summation = 0
    for _column in range(len(allocated_matrix[0])):
        for _row in range(len(allocated_matrix)):
            summation += allocated_matrix[_row][_column]
        summation += available_matrix[_column]
        if summation == resource[_column]:
            summation = 0
        else:
            return -1
    return 0


# solve the example
def solve_avoidance(claim_matrix, allocated_matrix, needed_matrix, resource_list, available_resource):
    temp_row = -1
    count = 0
    count_zero = 0

    for i in range(len(claim_matrix)):

        # to find any row is the chosen to process
        for _row in range(len(needed_matrix)):
            for _column in range(len(needed_matrix[_row])):
                if needed_matrix[_row][_column] == 0:
                    count_zero += 1
                if count_zero == len(needed_matrix[0]):
                    count = 0
                    count_zero = 0
                    break
                if needed_matrix[_row][_column] <= available_resource[_column]:
                    temp_row = _row
                    count += 1
            if count == len(needed_matrix[_row]):
                break
            count = 0
            count_zero = 0
        count = 0
        count_zero = 0

        for _column in range(len(allocated_matrix[temp_row])):
            available_resource[_column] += allocated_matrix[temp_row][_column]
            needed_matrix[temp_row][_column] = 0
            allocated_matrix[temp_row][_column] = 0
        matrix_print(claim_matrix, "Claim Matrix", needed_matrix, "Needed Matrix", allocated_matrix, "Allocation Matrix")
        print_resource(resource_list, "Resource List", available_resource, "Available resource")


def main():

    rows = int(input("Enter number of process :"))
    columns = int(input("Enter number of Resources :"))
    print("----------------------------------------")
    claim_matrix = matrix_input(rows, columns, "Claim Matrix")
    allocation_matrix = matrix_input(rows, columns, "Allocation Matrix")
    needed_matrix = calc_needed_matrix(claim_matrix, allocation_matrix)
    resource = resource_input(columns, "Resource List")
    available = resource_input(columns, "Available resource")

    # print the example matrix
    matrix_print(claim_matrix, "Claim Matrix", needed_matrix, "Needed Matrix", allocation_matrix, "Allocation Matrix")
    print_resource(resource, "Resource List", available, "Available resource")

    # check if the example save or not
    if check_safe_or_not(resource, available, allocation_matrix) == 0:
        print("save state")
        print("----------------------------------------")
        solve_avoidance(claim_matrix, allocation_matrix, needed_matrix, resource, available)
    else:
        print("un safe state")


if __name__ == '__main__':main()