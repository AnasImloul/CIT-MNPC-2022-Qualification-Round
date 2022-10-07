def stoi(time_string):
    """
    time complexity: O(1) -> we only did a few simple operations (addition, multiplication, division)
    space complexity: O(1) -> we used only a few variables
    """
    # a function that converts a string representation of the time mm:ss or m:ss
    # to an integer representation (mm:ss <==> minutes*60 + seconds)
    minutes, seconds = map(int, time_string.split(":"))
    return minutes * 60 + seconds


def itos(time_integer):
    """
    time complexity: O(1) -> we only did a few simple operations (addition, division, modulo)
    space complexity: O(1) -> we used only a few variables
    """
    # the inverse function of stoi
    # takes an integer representation of the time
    # and converts it to a string representation (mm:ss)
    minutes, seconds = divmod(time_integer, 60)
    return "{:2d}:{:02d}".format(minutes, seconds)


def play():
    """
    n is the number of goals
    time complexity: O(n) -> we iterate over all the goals once
    space complexity: O(1) -> we used only a few variables
    """
    # initialize all necessary variables
    # at the start of the match all the stats are set to zero
    score_A = score_H = 0
    wintime_A = wintime_H = 0
    last_goal = "00:00"  # get track of the time of the last goal

    goals = int(input())
    for goal in range(goals):
        # split the input into relevant data
        team, points, time = input().split()
        points = int(points)

        # check which team has the most points right before the current goal
        # and increase their winning time by the the difference between
        # the current time and the last goal time
        if score_H > score_A:
            wintime_H += stoi(time) - stoi(last_goal)
        elif score_A > score_H:
            wintime_A += stoi(time) - stoi(last_goal)

        # after that, increase their score
        # note that updating score must be done after updating the winning time
        if team == "H":
            score_H += points
        else:
            score_A += points

        # finally update the last goal time to the current time
        last_goal = time

    # after no goals are getting scored
    # just increase the winning time of the winning team until the match ends
    if score_H > score_A:
        wintime_H += stoi("32:00") - stoi(last_goal)
    elif score_A > score_H:
        wintime_A += stoi("32:00") - stoi(last_goal)

    # finally print the result
    winning_team = "A" if score_A > score_H else "H"
    print("{} {} {}".format(winning_team, itos(wintime_H), itos(wintime_A)))


play()