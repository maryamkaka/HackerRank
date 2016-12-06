# Davis has staircases in his house and he likes to climb each staircase 1, 2 or
# 3 steps at a time. Being a very precocious child, he wonders how many ways
# there are to reach the top of the staircase.
# Given the respective heights for each of the staircases in his house, find the
# number of ways he can climb each staircase on a new line.

stepMemo = {1:1, 2:2, 3:4}

def steps(n):
    if(not (n in stepMemo)):
        stepMemo[n] = steps(n-1) + steps(n-2) + steps(n-3)

    return stepMemo[n]
