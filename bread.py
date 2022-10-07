def minimum_permutations(permutation, n):
    """
    n is the length of the permutation
    time complexity: O(n) -> we iterate over the permutation once
    ### IMPORTANT ###
        even though we used a nested while loop inside the for loop, the time complexity is still O(n)
        because inside the while loop, we mark the elements that we have visited
        and we only visit each element once
        that means that the while loop will only run n times in total
    ### END IMPORTANT ###
    space complexity: O(n) -> we use a set to store the visited elements
    """
    # returns minimum number of swaps to sort the permutation
    # can be computed in linear time using permutation cycle decomposition
    # initialize the visited array
    visited = [False for i in range(n)]
    permutations = 0
    for i in range(1, n + 1):
        # if the element is already visited, skip it
        if visited[i - 1]:
            continue
        # otherwise, start a new cycle
        element = permutation[i - 1]
        cycle_length = 0
        # traverse the cycle until we get back to the starting element
        # and mark all the elements as visited
        while not visited[element - 1]:
            # mark the element as visited
            visited[element - 1] = True
            # move to the next element
            element = permutation[element - 1]
            # increase the cycle length
            cycle_length += 1
        # if the cycle length is greater than 1, then we need to swap
        # otherwise, the cycle is already sorted since it has only one element
        permutations += cycle_length - 1
    return permutations


def solve(permutation1, permutation2, n):
    # the idea is use the fact that each operation performed on permutation1 (rotation to the right by 1)
    # will result in a permutation whose minimum number of swaps is equal to
    # the minimum number of swaps of permutation1 plus or minus 2
    # this means that if the minimum number of swaps of permutation1
    # have different parity to the minimum number of swaps of permutation2
    # then it is impossible to transform permutation1 into permutation2
    # otherwise there is always a way to transform permutation1 into permutation2
    return minimum_permutations(permutation1, n) % 2 == minimum_permutations(permutation2, n) % 2


n = int(input())
bread = list(map(int, input().split()))
target = list(map(int, input().split()))

print("Possible" if solve(bread, target, n) else "Impossible")