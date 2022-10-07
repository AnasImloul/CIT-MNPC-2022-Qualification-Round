from math import sqrt


def max_area(a, b, c, d):
    """
    time complexity: O(1) -> we only did a few simple operations (addition, multiplication, division, square root)
    space complexity: O(1) -> we didn't use any extra variables
    """
    # given a,b,c,d the length of the sides of a 4-sided polygon
    # return the maximum area that can be obtained

    perimeter = a + b + c + d
    return sqrt((perimeter/2 - a) * (perimeter/2 - b) * (perimeter/2 - c) * (perimeter/2 - d))


a,b,c,d = map(int, input().split())
print(max_area(a,b,c,d))