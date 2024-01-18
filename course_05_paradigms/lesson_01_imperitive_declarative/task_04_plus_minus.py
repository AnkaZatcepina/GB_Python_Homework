#Доля чисел
def plus_minus_imperitive(arr):
    pos_cnt, neg_cnt, zero_cnt = 0, 0, 0
    for el in arr:
        if el > 0: pos_cnt += 1
        elif el < 0: neg_cnt += 1
        else: zero_cnt += 1
    pos_frac = pos_cnt / len(arr)
    neg_frac = neg_cnt / len(arr)
    zero_frac = zero_cnt / len(arr)
    return pos_frac, neg_frac, zero_frac

def plus_minus_declarative(arr):
    pos_cnt = len(list(filter(lambda x: x > 0, arr)))
    neg_cnt = len(list(filter(lambda x: x < 0, arr)))
    zero_cnt = len(list(filter(lambda x: x == 0, arr)))
    counts = [pos_cnt, neg_cnt, zero_cnt]
    return list(map(lambda count: count / len(arr), counts))