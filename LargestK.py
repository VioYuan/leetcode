import json
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # select the pilot index
        def partition1(nums, start, end):
            # i is the index of the number smaller than the current pilot
            i = start - 1
            #start is the traversal index
            while(start < end):
                #let end be the pilot index
                if nums[start] >= nums[end]:
                    #if the number is no smaller than the pilot, mark it, swap it with i to make it prior to pilot
                    i += 1
                    if i != start:
                        nums[start],nums[i] = nums[i],nums[start]
                #if the number is smaller than pilot, pass it     
                start += 1
            i += 1
            nums[i], nums[end] = nums[end], nums[i]
            return i
        def partition2(nums, start, end):
            i = start - 1
            #randomly choose pilot index
            pilot = random.choice(range(start, end+1))
            while(start <= end):
                #skip when the traversal pointer equals to pilot
                if nums[start] >= nums[pilot] and start != pilot:
                    i += 1
                    if i != start:
                        nums[start],nums[i] = nums[i],nums[start]
                        #update pilot when swap happens to pilot
                        if i == pilot:
                            pilot = start
                start += 1
            #set bound to the pilot pointer
            if i < end:
                i += 1
            nums[i], nums[pilot] = nums[pilot], nums[i]
            return i   
        def findhelper(nums, start, end, k):
            if start >= end:
                return nums[k-1]
            pilot = end
            index = partition(nums, start, end)
            print index, nums,k, index==k
            if index == k-1:
                return nums[index]
            elif index < k-1:
                return findhelper(nums, index + 1, end, k)
            elif index > k-1:
                return findhelper(nums, start, index - 1, k)
        if not nums or not k:
            return -1
        return findhelper(nums, 0, len(nums) - 1, k)

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)
            line = lines.next()
            k = stringToInt(line)
            
            ret = Solution().findKthLargest(nums, k)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
