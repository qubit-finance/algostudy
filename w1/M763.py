from collections import Counter
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # search new alphabet
        s_counter = Counter(s)
        answer_lst = []  # answer list
        aset = set()  # alphabet set
        count = 0

        # split if all alph in this set does not exit in remain str
        for i in range(len(s)):  # O(n)
            alph = s[i]
            if s_counter[alph] >= 2:
                s_counter[alph] -= 1
                aset.add(alph)
                count += 1
            elif s_counter[alph] == 1:
                # check end
                s_counter[alph] -= 1
                aset.add(alph)
                count += 1
                total = 0
                for x in aset:
                    total += s_counter[x]
                if total == 0: # no more alphs in remained str
                    answer_lst.append(count)
                    count = 0
                    aset = set()




        return answer_lst

    # 후보 1 : 시작과 끝을 뽑아서 최적화 (뽑는게 O(n^2))
    # 후보 2 : 2이상이면 그냥 넣고 내 set안에 있는게 전부 남은거에 없으면
    # 자른다. counter(O(n)) 1이면 새로운 counter를 만들어서 관리해야할 듯.

if __name__ == "__main__":
    s = Solution()
    ans = s.partitionLabels("ababcbacadefegdehijhklij")
    print(ans)