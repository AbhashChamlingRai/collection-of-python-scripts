"""
3.2 You are going to design a program which allows a robot to move in a 2D coordinate system
starting from the original point (0, 0). The robot can move to the next point (x, y) specified by
the user. If the next point is (999, 999), the program ends and prints out the distance moved at
each step.
"""


def int_value_checker(val):
    '''
    This function checkes where a value is an integer or not
    '''
    try:
        val = int(val)
    except:
        print("\nPlease Enter an integer value only!")



def get_next_point(step):
    '''
    It returns a tuple (x, y) from the user input. 
    The parameter step indicates the step number.
    '''
    var_x = input(f"\nInput x{step} cordinates: ")
    int_value_checker(var_x) # Checking if user input is integer or not
    var_x = int(var_x) 

    var_y = input(f"\nInput y{step} cordinates: ")
    int_value_checker(var_y)
    var_y = int(var_y)

    return (var_x, var_y)



def cal_distance(p1, p2):
    '''
    Parameters: p1, p2 --> both tuples
    It returns the distance (float) between the two points with 2 decimal places
    '''
    distance = (  (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2  )**0.5

    return round(distance, 2)



def print_distances(li):
    '''
    Parameter: li --> a list
    This function prints the given list of units in aproper format
    '''
    print("----------")
    for num, i in enumerate(li):
        print(f"Step {num+1}: {i:.2f} units")
    print("----------")

    total = sum(li)
    print(f"Total distance travelled by the robot: {total:.2f} units")



def main():
    '''
    It runs the whole robot program.
    It uses get_next_point() to take user inputs.
    It uses cal_distance() to calculate the distance between
    two points.
    '''
    each_step_distance = []
    coordinates_outer = (0,0)
    step_taken = 0
    while True:
        coordinates_inner = get_next_point(step_taken+1)

        distance_cover = cal_distance(coordinates_outer, coordinates_inner)

        coordinates_outer = coordinates_inner

        step_taken += 1

        if coordinates_inner == (999, 999):
            break
        else:
            each_step_distance.append(distance_cover)
    
    print_distances(each_step_distance)




if __name__ == "__main__":
    main()
            
