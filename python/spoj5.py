def find_palindrome(value):
    value = str(value + 1)
    whole_len = len(value)
    half_len = whole_len/2
    end_index = whole_len - 1  

    left_ptr = half_len - 1 
    if whole_len % 2 == 0:
        right_ptr = half_len
        middle_ptr = None
    else:
        right_ptr = half_len + 1
        middle_ptr = half_len
        middle_val = value[middle_ptr]

    if left_ptr >= 0:
        left_val = value[0:left_ptr+1] 
        right_val = value[right_ptr:end_index+1]
        del value

        left_int = int(left_val)
        right_int = int(right_val)

        if left_int > right_int:
            right_val = left_val[::-1]
            if middle_ptr:
                return "%s%s%s" % (left_val, middle_val, right_val)
            else: return "%s%s" % (left_val, right_val)

        elif right_int > left_int:
            if middle_ptr:
                middle_val = int(middle_val) + 1
                right_val = left_val[::-1]
                return "%s%i%s" % (left_val, middle_val, right_val)
            else:
                left_int = left_int + 1
                left_val = str(left_int)
                right_val = left_val[::-1]
                return "%s%s" % (left_val, right_val)

    return value

cases = int(raw_input())

for i in range(0, cases):
    case = int(raw_input())
    print str(find_palindrome(case))
