#!/usr/bin/python3
'''Module for validating UTF-8 characters.
'''


def validUTF8(data):
    '''Returns True if the data is valid UTF-8,
    otherwise returns False.
    '''
    cnt = 0
    for num in data:
        if cnt == 0:
            if num & 128 == 0:
                cnt = 0
            elif num & 224 == 192:
                cnt = 1
            elif num & 240 == 224:
                cnt = 2
            elif num & 248 == 240:
                cnt = 3
            else:
                return False
        else:
            if num & 192 != 128:
                return False
            cnt -= 1
    return cnt == 0
