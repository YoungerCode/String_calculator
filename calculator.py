import re

def add(num):
    num_list = []
    neg_num = []

    if len(num) == 0: return 0
    
    try:
        int(num[-1])
    except:
        return "Not ok"
       
    for each_letter in re.findall(r"-?\d+", num):
        try:
            if int(each_letter) > 1000:
                each_letter = 0
            if int(each_letter) < 0:
                neg_num.append(each_letter)
            num_list.append(int(each_letter))
        except:
            continue
            
    if len(neg_num) > 0:
        raise Exception('negatives not allowed: {}'.format(neg_num))

    return sum(num_list)
