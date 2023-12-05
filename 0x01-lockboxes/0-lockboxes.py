#!/usr/bin/python3

def canUnlockAll(boxes):
    # Set to keep track of opened boxes
    opened_boxes = {0}

    # List to store keys to be checked
    keys_to_check = [0]

    while keys_to_check:
        current_box = keys_to_check.pop()

        # Check keys in the current box
        for key in boxes[current_box]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                keys_to_check.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)

# Example usage for testing
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
