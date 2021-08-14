'''
A teacher must divide a class of students into two teams to play dodgeball.
Unfortunately, not all the kids get along, and several refuse to be put on the
same team as that of their enemies.

Given an adjacency list of students and their enemies, write an algorithm
that finds a satisfactory pair of teams, or returns False if none exists.

For example, given the following enemy graph you
should return the teams {0, 1, 4, 5} and {2, 3}.

students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}

On the other hand, given the input below, you should return False.
students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}

**Assumptions**
Students rivalry is bidirectional graph. ie: if student 0 hates student 3, then student 3 hates student 0.
'''


def Solution(students):
    temp = Helper([], [], students)
    if temp is not None:
        return temp
    else:
        return False
    
    
def Helper(team1, team2, students):
    if len(team1) + len(team2) == len(students):
        return (team1, team2)
    
    for key, val in students.items():
        if canPutInTeam(key, val, team1, team2):
            temp = []
            temp.extend(team1)
            temp.append(key)
            retVal = Helper(temp, team2, students)
            if retVal is not None:
                return retVal
        if canPutInTeam(key, val, team2, team1):
            temp = []
            temp.extend(team2)
            temp.append(key)
            retVal = Helper(team1, temp, students)
            if retVal is not None:
                return retVal
    return None


def canPutInTeam(student, enemies, team, otherTeam):
    if student in team or student in otherTeam:
        return False
    for enemy in enemies:
        if enemy in team:
            return False
    return True

# Return True
students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}
print(Solution(students))

# Return False
students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}
print(Solution(students))

# Return True
students = {
    0: [1,5],
    1: [0,2],
    2: [1,3],
    3: [2,4],
    4: [3,5],
    5: [0,4]
}
print(Solution(students))

# Return False
students = {
    0: [1,5],
    1: [0,2],
    2: [1,3,4],
    3: [2,4],
    4: [2,3,5],
    5: [1,4]
}
print(Solution(students))