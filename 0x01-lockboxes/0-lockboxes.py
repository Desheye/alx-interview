#!/usr/bin/python3
"""Module for determining if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of lists): Each inner list represents a box and contains
                               keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    box_count = len(boxes)
    unlocked_boxes = {0}  # Start with the first box unlocked
    keys_to_try = boxes[0]  # Initialize with keys from the first box
    examined_keys = set()

    while keys_to_try:
        current_key = keys_to_try.pop()
        
        if current_key not in examined_keys and current_key < box_count:
            examined_keys.add(current_key)
            unlocked_boxes.add(current_key)
            keys_to_try.extend(boxes[current_key])

        if len(unlocked_boxes) == box_count:
            return True

    return False
