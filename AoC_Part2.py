import os

def solve_part_two(file_path):
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' not found.")
        return

    # The dial starts at 50
    current_pos = 50
    total_zero_hits = 0

    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        for instruction in lines:
            if not instruction: continue

            direction = instruction[0]
            amount = int(instruction[1:])

            if direction == 'R':
                # We are moving UP.
                # We calculate the "virtual" number we would reach on a number line.
                # Example: At 99, moving R2 takes us to 101.
                # Every multiple of 100 we pass counts as hitting '0'.
                virtual_end = current_pos + amount
                
                # Math trick: integer division (//) tells us how many 100s fit in.
                hits = (virtual_end // 100) - (current_pos // 100)
                total_zero_hits += hits
                
                # Update actual position (0-99)
                current_pos = virtual_end % 100

            elif direction == 'L':
                # We are moving DOWN.
                # We look at the range of numbers touched: [start-1 down to end]
                virtual_end = current_pos - amount
                
                # We shift by -1 because leaving 0 (going 0 -> 99) doesn't count.
                # Only arriving at 0 (going 1 -> 0) counts.
                hits = ((current_pos - 1) // 100) - ((virtual_end - 1) // 100)
                total_zero_hits += hits
                
                # Update actual position (0-99)
                current_pos = virtual_end % 100

        print(f"Success! The dial passed or landed on 0 a total of {total_zero_hits} times.")
        print(f"ACTUAL PASSWORD (Part 2): {total_zero_hits}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    solve_part_two('sample_input_1.txt')