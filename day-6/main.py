
INPUT_FILE_PATH = 'input.txt'
# INPUT_FILE_PATH = 'test-input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        signal = f.read()
        # only for test
        # test_index = 4
        # signal = signal.split("\n")[test_index]

        start_of_packet_marker_index = find_start_of_packet_index(signal, 4)
        print(start_of_packet_marker_index) # Part 1

        start_of_packet_marker_index = find_start_of_packet_index(signal, 14)
        print(start_of_packet_marker_index) # Part 2

def find_start_of_packet_index(string, window_length):  # TODO Not Optimized Alghoritm
    # window_length = 4
    start_index = 0 # start index of sliding window
    end_index = start_index + window_length - 1

    while (end_index <= len(string)):
        unique_chars = set()
        unique_chars.update(string[end_index-window_length:end_index])
        if len(unique_chars) == window_length: return end_index
        end_index += 1

if __name__ == "__main__":
    main()