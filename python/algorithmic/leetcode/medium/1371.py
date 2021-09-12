# 1371. Find the Longest Substring Containing Vowels in Even Counts
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

from bisect import bisect_left

class Solution:
    def newStart(self, occurrences, minStart):
        maximum = 0
        for ch, positions in occurrences.items():
            i = bisect_left(positions, minStart)
            charCount = len(positions) - i
            if charCount % 2 == 0:
                maximum = max(maximum, positions[i])
            else:
                maximum = max(maximum, positions[i]+1)

    def findTheLongestSubstring(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        counts = {v: 0 for v in vowels}
        occurrences = {v:[] for v in vowels}
        start = 0
        maxLen = 0
        maxIndices = [0, 0]
        for i, ch in enumerate(s):
            if ch in vowels:
                counts[ch] += 1
                occurrences[ch].append(i)
                if counts[ch] % 2 == 0:
                    start = self.newStart(occurrences, i)
                    currLen = i - start + 1
                    if currLen > maxLen:
                        maxLen = currLen
                        maxIndices = [start + 1, i + 1]
                elif counts[ch] == 1:
                    firstOccurrences[ch] = i
                    startMap[ch] = i
                else:
                    startMap[ch] = firstOccurrences[ch]
                    start = max(startMap.values())
                    currLen = i - start
                    if currLen > maxLen:
                        maxLen = currLen
                        maxIndices = [start + 1, i + 1]

            else:
                start = max(startMap.values())
                currLen = i - start
                if currLen > maxLen:
                    maxLen = currLen
                    maxIndices = [start + 1, i + 1]
        # print(s[maxIndices[0]:maxIndices[1]])
        return maxLen

if __name__=='__main__':
    str = "tyrwpvlifrgjghlcicyocusukhmjbkfkzsjhkdrtsztchhazhmcircxcauajyzlppedqyzkcqvffyeekjdwqtjegerxbyktzvrxwgfjnrfbwvhiycvoznriroroamkfipazunsabwlseseeiimsmftchpafqkquovuxhhkpvphwnkrtxuiuhbcyqulfqyzgjjwjrlfwwxotcdtqsmfeingsxyzbpvmwulmqfrxbqcziudixceytvvwcohmznmfkoetpgdntrndvjihmxragqosaauthigfjergijsyivozzfrlpndygsmgjzdzadsxarjvyxuecqlszjnqvlyqkadowoljrmkzxvspdummgraiutxxxqgotqnxwjwfotvqglqavmsnmktsxwxcpxhuujuanxueuymzifycytalizwnvrjeoipfoqbiqdxsnclcvoafqwfwcmuwitjgqghkiccwqvloqrxbfjuxwriltxhmrmfpzitkwhitwhvatmknyhzigcuxfsosxetioqfeyewoljymhdwgwvjcdhmkpdfbbztaygvbpwqxtokvidtwfdhmhpomyfhhjorsmgowikpsdgcbazapkmsjgmfyuezaamevrbsmiecoujabrbqebiydncgapuexivgvomkuiiuuhhbszsflntwruqblrnrgwrnvcwixtxycifdebgnbbucqpqldkberbovemywoaxqicizkcjbmbxikxeizmzdvjdnhqrgkkqzmspdeuoqrxswqrajxfglmqkdnlescbjzurknjklikxxqqaqdekxkzkscoipolxmcszbebqpsizhwsxklzulmjotkrqfaeivhsedfynxtbzdrviwdgicusqucczgufqnaslpwzjhgtphnovlrgz"
    maxLen = Solution().findTheLongestSubstring(str)
    print(maxLen)
    # s = "dqyzkcqvffyeekjdwqtjegerxbyktzvrxwgfjnrfbwvhiycvoznriroroamkfipazunsabwlseseeiimsmftchpafqkquovuxhhkpvphwnkrtxuiuhbcyqulfqyzgjjwjrlfwwxotcdtqsmfeingsxyzbpvmwulmqfrxbqcziudixceytvvwcohmznmfkoetpgdntrndvjihmxragqosaauthigfjergijsyivozzfrlpndygsmgjzdzadsxarjvyxuecqlszjnqvlyqkadowoljrmkzxvspdummgraiutxxxqgotqnxwjwfotvqglqavmsnmktsxwxcpxhuujuanxueuymzifycytalizwnvrjeoipfoqbiqdxsnclcvoafqwfwcmuwitjgqghkiccwqvloqrxbfjuxwriltxhmrmfpzitkwhitwhvatmknyhzigcuxfsosxetioqfeyewoljymhdwgwvjcdhmkpdfbbztaygvbpwqxtokvidtwfdhmhpomyfhhjorsmgowikpsdgcbazapkmsjgmfyuezaamevrbsmiecoujabrbqebiydncgapuexivgvomkuiiuuhhbszsflntwruqblrnrgwrnvcwixtxycifdebgnbbucqpqldkberbovemywoaxqicizkcjbmbxikxeizmzdvjdnhqrgkkqzmspdeuoqrxswqrajxfglmqkdnlescbjzurknjklikxxqqaqdekxkzkscoipolxmcszbebqpsizhwsxklzulmjotkrqfaeivhsedfynxtbzdrviwdgicusqucczgufqnaslpwzjhgtphnovlrgz"
    # counts = {ch:0 for ch in "aeiou"}
    # for ch in s:
    #     if ch in "aeiou":
    #         counts[ch] += 1
    # print(counts)