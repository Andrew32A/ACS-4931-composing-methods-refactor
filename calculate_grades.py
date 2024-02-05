# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def get_input_from_user():
    grade_list = []

    n_student = 5
    for _ in range(n_student):
        grade_list.append(int(input('Enter a number: ')))

    return grade_list

def calculate_grades(grade_list):
    total = 0
    for grade in grade_list:
        total += grade
    mean = total / len(grade_list)
    sd = 0
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))

    return mean, sd

def print_grade_statistics(mean, sd):
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

def main():
    grade_list = get_input_from_user()
    completed_calculations = calculate_grades(grade_list)
    print_grade_statistics(completed_calculations[0], completed_calculations[1])

main()
