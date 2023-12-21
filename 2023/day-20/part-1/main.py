
from collections import deque
import re


INPUT_FILE_PATH = '../data/test-input-1-1.txt'

# 333,000,000 TO low

T = 1000 # HEREE FOR LOOP 

FF = "ff" # Flip-Flop
CJ = "cj" # Conjunction

LOW = "L"
HIGH = "H"

def main():
    # BD: (broadcaster destinations) list of destination modules of broadcaster 
    # M: (modules) dict key=module_name value=(module_type, list_of_destinations_modules)
    BD, M = parse_input_file() 


    count_pulse = [0, 0] # [L, H] 
    

    # FOR LOOP T
    # L + 1 -> Button -> Broadcaster

    # state = ({LOW,HIGH}, source_module_name, destination_module_name)
    queue = deque() 
    
    # Pushing Button Module + Broadcast Module
    for destination_module_name in BD:
        queue.append((LOW, 'broadcaster', destination_module_name))
    
    while queue:
        pulse, source_module_name, destination_module_name = queue.popleft()
        print(pulse, source_module_name, destination_module_name)
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
            # PROBLEM HERE !!!
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

    print(count_pulse)

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
    
    # BAD
    tmp_cj_input_module_dict = dict()
    for name, module in modules.items():
        _, dests, _ = module
        for dest in dests:
            if dest in cj_modules:
                if dest in tmp_cj_input_module_dict:
                    tmp_cj_input_module_dict[dest].append(name)
                else:
                    tmp_cj_input_module_dict[dest] = [name]
    
    for module_name, input_modules_name in tmp_cj_input_module_dict.items():
        (type, dests, state) = modules[module_name]
        modules[module_name] = (type, dests, {key: LOW for key in input_modules_name})


    return broadcaster_dests,  modules


if __name__ == "__main__":
    main()