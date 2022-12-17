from enum import Enum

INPUT_FILE_PATH = '../data/input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        round_list = [x.split(" ") for x in f.read().split("\n")]
        score_list = [get_score(x) for x in round_list]
        print(sum(score_list)) # <Part 1>

def get_score(round):
    opponent_shape = get_shape(round[0])
    own_shape = get_shape(round[1])

    result = 0
    result += get_default_score(own_shape)
    result += get_outcome_score(opponent_shape, own_shape)
    return result

def get_shape(str):
    match str:
        case "A" | "X":
            return Shapes.rock
        case "B" | "Y":
            return Shapes.paper
        case "C" | "Z":
            return Shapes.scissors

def get_default_score(shape):
    match shape:
        case Shapes.rock:
            return 1
        case Shapes.paper:
            return 2
        case Shapes.scissors:
            return 3
    return 0

# very bad function
def get_outcome_score(opponent_shape, own_shape):
    if opponent_shape == own_shape:
        return 3
    if (opponent_shape == Shapes.rock and own_shape == Shapes.scissors) or (opponent_shape == Shapes.scissors and own_shape == Shapes.paper) or (opponent_shape == Shapes.paper and own_shape == Shapes.rock):
        return 0
    return 6

class Shapes(str, Enum):
    rock = 'rock'
    scissors = 'scissors'
    paper = 'paper'
        
if __name__ == "__main__":
    main()


# class round():    
#     def __init__(self, opponent_shape, your_shape) -> None:
#         self.opponent_shape = opponent_shape
#         self.your_shape = your_shape

# opponent  you     shape       score
# ---------------------------------
# A         X       rock        1
# B         Y       paper       2
# C         Z       scissors    3

# outcome of the round  score
# lost                  0
# draw                  3 
# won                   6


# input
# opponent - you

# Rock defeats Scissors
# Scissors defeats Paper
# Paper defeats Rock

# total_score = sum(round_scores)
# round_scores = score + outcome_score