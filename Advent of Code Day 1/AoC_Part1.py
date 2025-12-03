import os

def solve_secret_entrance(file_path):
    # Check if file exists to avoid crashing
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' not found. Make sure the file is in the same folder.")
        return

    # The dial starts at 50
    current_pos = 50
    zero_hits = 0

    try:
        with open(file_path, 'r') as f:
            # Read lines and strip whitespace (newlines)
            lines = [line.strip() for line in f.readlines()]

        for instruction in lines:
            if not instruction: continue  # Skip empty lines

            direction = instruction[0]
            amount = int(instruction[1:])

            if direction == 'R':
                # Add and wrap around 0-99
                current_pos = (current_pos + amount) % 100
            elif direction == 'L':
                # Subtract and wrap around 0-99
                current_pos = (current_pos - amount) % 100
            
            # Check if we landed on 0
            if current_pos == 0:
                zero_hits += 1

        print(f"Success! The dial hit 0 a total of {zero_hits} times.")
        print(f"ACTUAL PASSWORD: {zero_hits}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure input.txt is in the same directory as this script
    solve_secret_entrance('sample_input_1.txt')
