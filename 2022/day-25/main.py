INPUT_FILE_PATH = 'data/test-input.txt'

SNAFU_symbols = ['2', '1', '0', '-', '=']
SNAFU_values = ['2', '1', '0', '-1', '-2']
BASE_number = 5

def main():

    input_SNAFU_list = parse_file(INPUT_FILE_PATH)

    # SNAFU to DECIMAL
    DECIMAL_list = list_from_SNAFU_to_DECIMAL(input_SNAFU_list)

    DECIMAL_list_sum = sum (DECIMAL_list)

    # DECIMAL to SNAFU
    SNAFU_list = from_DECIMAL_to_SNAFU(DECIMAL_list_sum)

    print(SNAFU_list) # <Part 1>

def from_DECIMAL_to_SNAFU(DECIMAL_num):
    n = DECIMAL_num
    r = ""
    while n > 0:
        d = ((n + 2) % BASE_number) - 2
        r += SNAFU_symbols[SNAFU_values.index(str(d))]
        n -= d
        n //= BASE_number
    return r[::-1]

def list_from_SNAFU_to_DECIMAL(ls):
    # Iterative function

    decimal_list = []
    for snafu_number in ls:
        decimal_list.append(from_SNAFU_to_DECIMAL(snafu_number))
    return decimal_list

def from_SNAFU_to_DECIMAL(snafu_nummber_symbols): # TODO: bad function
    snafu_number_values = get_SNAFU_values(snafu_nummber_symbols)
    i = len(snafu_number_values) - 1
    
    k = 0
    r = 0
    while i >= 0:
        r += int(snafu_number_values[k]) * pow(BASE_number, i)
        k += 1
        i -= 1
    
    return r

def get_SNAFU_values(snafu_number_symbols):
    s = []
    for i in snafu_number_symbols:
        s.append(SNAFU_values[SNAFU_symbols.index(i)])
    return s

def parse_file(path):
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')
    return lines

if __name__ == "__main__":
    main()