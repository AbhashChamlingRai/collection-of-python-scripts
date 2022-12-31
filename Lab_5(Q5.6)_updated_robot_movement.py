"""
5.6 Modify exercise Lab_5(Q3.2)_robot_movement.py 
to complete this exercise. Using the current
location (x1,y1) and the destination location (x2,y2) the software should also be able
to identify direction of the movement. For example, if the robot is moving to the
Bottom, Top, Right, Left or combination of them e.g. Top Right or Bottom Left.
As in exercise 3.2, when the user inputs a special number/character, the software
should print all previous movements by showing a combination of the moved
distance and the direction of each step. The trace function also displays the total
distance travelled by the robot
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
    Parameter: li --> a dictionary
    This function prints the given list of units in aproper format
    '''
    print("----------")
    counter = 1
    for k, v in li.items():
        print(f"Step {counter}: {k:.2f} meters to {v}")
        counter += 1
    print("----------")

    total = sum(li)
    print(f"Total distance (in meters) travelled by the robot: {total:.2f} meters")



def direction_of_movement(tup1, tup2):
    '''
    Return the direction of (based on two coordinates tuples):
        Top, Right, Bottom, Left, Top Right, Bottom Left, Bottom Right, Top Left
    '''
    x1, y1 = tup1
    x2, y2 = tup2

    if x1 == x2 and y1 > y2:
        return "Bottom"
    elif x1 == x2 and y1 < y2:
        return "Top"
    elif x1 > x2 and y1 == y2:
        return "Left"
    elif x1 < x2 and y1 == y2:
        return "Right"

    elif x1 > x2 and y1 > y2:
        return "Bottom Left"
    elif x1 < x2 and y1 > y2:
        return "Bottom Right"
    elif x1 > x2 and y1 < y2:
        return "Top Left"
    elif x1 < x2 and y1 < y2:
        return "Top Right"



def main():
    '''
    It runs the whole robot program.
    It uses get_next_point() to take user inputs.
    It uses cal_distance() to calculate the distance between
    two points.
    '''
    each_step = {}
    coordinates_outer_previous = (0,0)
    coordinates_outer_current = (0,0)
    step_taken = 0
    while True:
        # coordinates_inner = get_next_point(step_taken+1)

        if step_taken == 0:
            coordinates_outer_current = get_next_point(step_taken+1)

        elif step_taken != 0:
            coordinates_outer_previous = coordinates_outer_current
            coordinates_outer_current = get_next_point(step_taken+1)

        distance_cover = cal_distance(coordinates_outer_previous, coordinates_outer_current)

        direction = direction_of_movement(coordinates_outer_previous, coordinates_outer_current)

        step_taken += 1

        if coordinates_outer_current == (999, 999):
            break
        else:
            each_step[distance_cover] = direction

    
    print_distances(each_step)




if __name__ == "__main__":
    main()
            
