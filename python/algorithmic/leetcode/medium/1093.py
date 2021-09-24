# 1093. Statistics from a Large Sample
# https://leetcode.com/problems/statistics-from-a-large-sample/

class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        sample_size = sum(count)
        maximum = 0
        minimum = 255
        total = 0
        cum_count = 0
        median_index = []
        max_count = 0
        median = 0
        if sample_size % 2 == 0:
            median_index.append(sample_size / 2)
            median_index.append((sample_size / 2) + 1)
        else:
            median_index.append((sample_size + 1) / 2)
            median_index.append((sample_size + 1) / 2)

        arr = count
        for i, count in enumerate(arr):
            total = total + i * count
            if count != 0:
                maximum = i
            if count != 0 and i < minimum:
                minimum = i
            if cum_count < median_index[1] and (cum_count + count) >= median_index[1]:
                median += i
            if cum_count < median_index[0] and (cum_count + count) >= median_index[0]:
                median += i
            if count > max_count:
                max_count = count
                mode = i

            cum_count += count

        mean = total / float(sample_size)

        # for idx, i in enumerate(arr):
        #    if i>0:
        #        print(idx, i)
        return [minimum, maximum, mean, median / 2.0, mode]
