
def multi_bracket_validation(string):
    brac_list = []
    begin = '{[('
    end = ')]}'
    dic = { ']': '[', ')': '(', '}': '{' }

    for str_ in string:
        if str_ in begin:
            brac_list.append(str_)
        elif str_ in end:
            if len(brac_list) == 0:
                return False
            if brac_list[-1] == dic[str_]:
                brac_list.pop()
    return len(brac_list) == 0
