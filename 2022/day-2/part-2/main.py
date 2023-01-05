from enum import Enum

INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        list = [x.split(" ") for x in f.read().split("\n")]
        round_list = get_round_list(list)
        score_list = [get_score(x) for x in round_list]
        print(sum(score_list)) # <Part 2>

def get_round_list(list):
    for x in list:
        opponent_shape = x[0]
        outcome_end = x[1]
        x[1] = get_own_shape(opponent_shape, outcome_end)
    return list

def get_own_shape(opponent_shape, outcome_end):
    if outcome_end == Results.draw:
        return opponent_shape
    if outcome_end == Results.win:
        match opponent_shape:
            case Shapes.rock:
                return Shapes.paper.value
            case Shapes.paper:
                return Shapes.scissors.value
            case Shapes.scissors:
                return Shapes.rock.value
    if outcome_end == Results.lose:
        match opponent_shape:
            case Shapes.rock:
                return Shapes.scissors.value
            case Shapes.paper:
                return Shapes.rock.value
            case Shapes.scissors:
                return Shapes.paper.value

def get_score(round):
    opponent_shape = round[0]
    own_shape = round[1]

    result = 0
    result += get_default_score(own_shape)
    result += get_outcome_score(opponent_shape, own_shape)
    return result

def get_shape(str):
    match str:
        case "A":
            return Shapes.rock
        case "B":
            return Shapes.paper
        case "C":
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
    rock = "A"
    paper = "B"
    scissors = "C"

class Results(str, Enum):
    lose = "X"
    draw = "Y"
    win = "Z"

if __name__ == "__main__":
    main()