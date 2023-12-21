
from collections import deque
import re


INPUT_FILE_PATH = '../data/test-input-1-1.txt'

T = 1000 

FF = "ff" # Flip-Flop
CJ = "cj" # Conjunction
BC = "bc" # Broadcaster

LOW = "L"
HIGH = "H"

def main():
    # BD: (broadcaster destinations) list of destination modules names of broadcaster 
    # M: (modules) dict key=module name, value=(module_type in {ff, cj}, list_of_destinations_modules, state)
    #     state:
    #       - [type == ff] (is_on) 
    #            is_on: boolean (default False)
    #       - [type == cj] (most_recent_pulse_dict)
    #            most_recent_pulse_dict: dict key=source module name, value=most recent pulse received from source module (default LOW)
    BD, M = parse_input_file() 

    count_pulse = [0, 0] # [LOW, HIGH] 
    
    for _ in range(T):
        # Button Module -> Broadcaster Module
        count_pulse[0] += 1

        # state = ({LOW,HIGH}, source_module_name, destination_module_name)
        queue = deque() 
        
        # Broadcaster Module
        for destination_module_name in BD:
            queue.append((LOW, BC, destination_module_name))
        
        while queue:
            pulse, source_module_name, destination_module_name = queue.popleft()

            # Update count_pulse
            count_pulse[pulse == HIGH] += 1 # NOTE: True = 1, False = 0 
            
            if destination_module_name not in M:
                continue

            type, dests, state = destination_module = M[destination_module_name]

            # Flip-Flop
            if type == FF:
                is_on = state
                if (pulse == LOW):
                    is_on = not is_on
                    # Update module state
                    M[destination_module_name] = (type, dests, is_on)
                    # Emit pulses
                    if is_on:
                        for dest in dests:
                            queue.append((HIGH, destination_module_name, dest))
                    else:
                        for dest in dests:
                            queue.append((LOW, destination_module_name, dest))
            # Conjunction
            else:
                most_recent_pulse_dict = state            
                most_recent_pulse_dict[source_module_name] = pulse
                # Update module state
                M[destination_module_name] = type, dests, (most_recent_pulse_dict)
                # Emit pulses
                if all(value == HIGH for value in most_recent_pulse_dict.values()):
                    for dest in dests:
                        queue.append((LOW, destination_module_name, dest))
                else:
                    for dest in dests:
                        queue.append((HIGH, destination_module_name, dest))
    # Part 1
    print(count_pulse[0] * count_pulse[1])

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

    broadcaster_dests = []
    modules = dict()
    cj_modules = []
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
                type = FF
                state = (False) # False: off, True: on 
                modules[name] = (type, dests, state)
            case '&':
                type = CJ
                state = (dict()) # key: module name, value: most recent pulse received
                modules[name] = (type, dests, state)
                cj_modules.append(name)
    
    # Input modules for cj modules
    tmp_cj_input_module_dict = dict()
    for name, module in modules.items():
        _, dests, _ = module
        for dest in dests:
            if dest in cj_modules:
                if dest in tmp_cj_input_module_dict:
                    tmp_cj_input_module_dict[dest].append(name)
                else:
                    tmp_cj_input_module_dict[dest] = [name]

    # Update state for cj modules
    for module_name, input_modules_name in tmp_cj_input_module_dict.items():
        (type, dests, state) = modules[module_name]
        modules[module_name] = (type, dests, {key: LOW for key in input_modules_name})

    return broadcaster_dests,  modules


if __name__ == "__main__":
    main()