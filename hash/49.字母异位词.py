import collections


def groupAnagrams(str1):
    mp = collections.defaultdict(list)
    for st in str1:
        key = ''.join(sorted(st))
        mp[key].append(st)
    return mp.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = groupAnagrams(strs)
print(list(res))