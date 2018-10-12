def count_substring(string, sub_string):
    i = 0
    cnt = 0
    for _ in range(len(string)):
        if string.find(sub_string,i) >=0:
            i = string.find(sub_string,i)+1
            cnt = cnt +1
        else:
            break

    return cnt
