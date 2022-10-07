def missing(complete, incomplete, n):
    """
    n is the length of the complete list
    time complexity: O(nlog(n)) -> sorting the lists takes O(nlog(n)) time and the rest of the algorithm takes O(n) time
    space complexity: O(1) -> we didn't use any extra variables
    """
    # given a complete list and an incomplete list, return the missing item
    # the missing item is the only item that is in the complete list but not in the incomplete list
    # the missing item is guaranteed to exist, and it is unique

    # sort the lists
    complete.sort()
    incomplete.sort()

    # iterate over the lists until we find the missing item
    # it is guaranteed that up until the missing item, the lists will be equal
    # example: [1,2,3,4,5] and [1,2,3,5] -> 4 is the missing item
    for i in range(n-1):
        if complete[i] != incomplete[i]:
            return complete[i]

    # if we didn't find the missing item, then it is the last item in the complete list
    return complete[-1]


n = int(input())
complete = list(map(int, input().split()))
incomplete = list(map(int, input().split()))

print(missing(complete, incomplete, n))
