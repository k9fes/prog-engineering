from collections import Counter

def melon(s):
    count = Counter(map(int, s))
    top_three = dict(count.most_common(3))
    return dict(sorted(top_three.items()))

s = "113131515515051851512941414414125166"
print(melon(s))