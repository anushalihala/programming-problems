# 636. Exclusive Time of Functions
# https://leetcode.com/problems/exclusive-time-of-functions/
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = [logs[0].split(":")[0]]
        result = [0 for i in range(n)]
        for i in range(1, len(logs)):
            f_id, event, time = logs[i].split(":")
            f_id_prev, event_prev, time_prev = logs[i-1].split(":")
            if event==event_prev:
                if event=="start":
                    result[int(f_id_prev)] += int(time) - int(time_prev)
                    stack.append(f_id)
                else:
                    result[int(f_id)] += int(time) - int(time_prev)
                    stack.pop()
            else:
                if event == "end":
                    result[int(f_id)] += int(time) - int(time_prev) + 1
                    stack.pop()
                else:
                    if len(stack)>0:
                        f_id_start = stack[-1]
                        result[int(f_id_start)] += int(time) - int(time_prev) - 1
                    stack.append(f_id)

        return result