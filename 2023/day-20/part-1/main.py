
import re


INPUT_FILE_PATH = '../data/test-input-1-1.txt'

def main():
    # BD: (broadcaster destinations) list of destination modules of broadcaster 
    # M: (modules) dict key=module_name value=(module_type, list_of_destinations_modules)
    BD, M = parse_input_file() 

    # Click button (send L to Broadcast)
    # BroadCast (send L to all modules)

    # so starting states in a queue

    # L, b[0]
    # L, b[1]
    # L, b[2]
    # ...
    # L, b[n-1]

    # % and & works? HERE____>>
    
    print(BD)
    print(M)


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

    broadcaster_dests = []
    modules = dict()
    regex = re.compile('([%&]?)([a-zA-z]+)\s+->\s+(.*)')
    for line in file.split('\n'):
        match_obj = re.match(regex, line)
        type = None

        type, name, dests = match_obj.groups()
        dests = dests.split(', ')    
        
        match type:
            case '':
                broadcaster_dests = dests
            case '%':
                type = "ff"
                modules[name] = (type, dests)
            case '&':
                type = "cj"
                modules[name] = (type, dests)

    return broadcaster_dests,  modules


if __name__ == "__main__":
    main()