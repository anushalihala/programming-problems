# 1371. Find the Longest Substring Containing Vowels in Even Counts
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

from bisect import bisect_left

class Solution:
    def newStart(self, occurrences, minStart):
        maximum = minStart
        while True:
            for ch, positions in occurrences.items():
                if len(positions) == 0:
                    continue

                i = bisect_left(positions, minStart)
                if i == len(positions):
                    continue
                charCount = len(positions) - i
                if charCount % 2 == 0:
                    if i!=0:
                        maximum = max(maximum, positions[i-1]+1) #include position[i]
                else:
                    maximum = max(maximum, positions[i]+1) #exclude position[i]

            if maximum == minStart:
                break
            else:
                minStart = maximum

        # print(minStart, maximum)
        return maximum

    def findTheLongestSubstring(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        counts = {v: 0 for v in vowels}
        occurrences = {v:[] for v in vowels}
        start = 0 #inclusive
        maxLen = 0
        maxIndices = [0, 0]
        for i, ch in enumerate(s):
            if ch in vowels:
                counts[ch] += 1
                occurrences[ch].append(i)
                if counts[ch] == 1:
                    start = i + 1
                else:
                    if counts[ch]%2 == 0:
                        minStart = 0
                    else:
                        minStart = occurrences[ch][0]+1 if (len(occurrences[ch]) > 0) else 0
                    start = self.newStart(occurrences, minStart)
                    currLen = i - start + 1
                    if currLen > maxLen:
                        maxLen = currLen
                        maxIndices = [start, i + 1]
                        # print(maxLen)

            else:
                currLen = i - start + 1
                if currLen > maxLen:
                    maxLen = currLen
                    maxIndices = [start, i + 1]
                    # print((maxLen))
        # print(s[maxIndices[0]:maxIndices[1]])
        return maxIndices, maxLen

if __name__=='__main__':
    str = "tyrwpvlifrgjghlcicyocusukhmjbkfkzsjhkdrtsztchhazhmcircxcauajyzlppedqyzkcqvffyeekjdwqtjegerxbyktzvrxwgfjnrfbwvhiycvoznriroroamkfipazunsabwlseseeiimsmftchpafqkquovuxhhkpvphwnkrtxuiuhbcyqulfqyzgjjwjrlfwwxotcdtqsmfeingsxyzbpvmwulmqfrxbqcziudixceytvvwcohmznmfkoetpgdntrndvjihmxragqosaauthigfjergijsyivozzfrlpndygsmgjzdzadsxarjvyxuecqlszjnqvlyqkadowoljrmkzxvspdummgraiutxxxqgotqnxwjwfotvqglqavmsnmktsxwxcpxhuujuanxueuymzifycytalizwnvrjeoipfoqbiqdxsnclcvoafqwfwcmuwitjgqghkiccwqvloqrxbfjuxwriltxhmrmfpzitkwhitwhvatmknyhzigcuxfsosxetioqfeyewoljymhdwgwvjcdhmkpdfbbztaygvbpwqxtokvidtwfdhmhpomyfhhjorsmgowikpsdgcbazapkmsjgmfyuezaamevrbsmiecoujabrbqebiydncgapuexivgvomkuiiuuhhbszsflntwruqblrnrgwrnvcwixtxycifdebgnbbucqpqldkberbovemywoaxqicizkcjbmbxikxeizmzdvjdnhqrgkkqzmspdeuoqrxswqrajxfglmqkdnlescbjzurknjklikxxqqaqdekxkzkscoipolxmcszbebqpsizhwsxklzulmjotkrqfaeivhsedfynxtbzdrviwdgicusqucczgufqnaslpwzjhgtphnovlrgz"
    # str = "eleetminicoworoep"
    maxIndices, maxLen = Solution().findTheLongestSubstring(str)
    print(maxLen, maxIndices)
    # s = "dqyzkcqvffyeekjdwqtjegerxbyktzvrxwgfjnrfbwvhiycvoznriroroamkfipazunsabwlseseeiimsmftchpafqkquovuxhhkpvphwnkrtxuiuhbcyqulfqyzgjjwjrlfwwxotcdtqsmfeingsxyzbpvmwulmqfrxbqcziudixceytvvwcohmznmfkoetpgdntrndvjihmxragqosaauthigfjergijsyivozzfrlpndygsmgjzdzadsxarjvyxuecqlszjnqvlyqkadowoljrmkzxvspdummgraiutxxxqgotqnxwjwfotvqglqavmsnmktsxwxcpxhuujuanxueuymzifycytalizwnvrjeoipfoqbiqdxsnclcvoafqwfwcmuwitjgqghkiccwqvloqrxbfjuxwriltxhmrmfpzitkwhitwhvatmknyhzigcuxfsosxetioqfeyewoljymhdwgwvjcdhmkpdfbbztaygvbpwqxtokvidtwfdhmhpomyfhhjorsmgowikpsdgcbazapkmsjgmfyuezaamevrbsmiecoujabrbqebiydncgapuexivgvomkuiiuuhhbszsflntwruqblrnrgwrnvcwixtxycifdebgnbbucqpqldkberbovemywoaxqicizkcjbmbxikxeizmzdvjdnhqrgkkqzmspdeuoqrxswqrajxfglmqkdnlescbjzurknjklikxxqqaqdekxkzkscoipolxmcszbebqpsizhwsxklzulmjotkrqfaeivhsedfynxtbzdrviwdgicusqucczgufqnaslpwzjhgtphnovlrgz"
    counts = {ch:0 for ch in "aeiou"}
    for ch in str[maxIndices[0]:maxIndices[1]]:
        if ch in "aeiou":
            counts[ch] += 1
    print(counts)