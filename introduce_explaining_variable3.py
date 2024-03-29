# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    cooking_value = time * temperature * pressure * COOKED_CONSTANT
    
    is_well_done = desired_state == 'well-done' and cooking_value >= WELL_DONE
    is_medium = desired_state == 'medium' and cooking_value >= MEDIUM
    
    return is_well_done or is_medium

def main():
    time = 30
    temp = 103
    pressure = 20
    desired_state = 'well-done'
    
    if is_cookeding_criteria_satisfied(time, temp, pressure, desired_state):
        print('cooking is done.')
    else:
        print('ongoing cooking.')

main()