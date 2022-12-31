# 5.2 Write a program that get two lists as input and check if they have at least one common member.

def list_intersection_checker(list1, list2):
    '''
    This function check if two lists have at least one common member
    '''
    common_members = []

    for each in list1:
        if each in list2:
            common_members.append(each)
    
    if len(common_members) == 0:
        print(f"\nThere are no common members between the two lists: {list1} & {list2}")
    else:
        print(f"\nThere are common members between the two lists: {list1} & {list2}")
        print("They are:")
        for i in common_members:
            print(f"\t{i}")
        print("\n\n\n")

if __name__ == "__main__":
    list_intersection_checker([1,2,3,4,5], [6,343,5,1,8,6])

    list_intersection_checker([123,123,5432,77], [1234,55,2])