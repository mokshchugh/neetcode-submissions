class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num]=count.get(num,0)+1
        
        bucket = [[] for _ in range(len(nums)+1)]
        
        for num, i in count.items():
            bucket[i].append(num)

        answer=[]

        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                answer.append(num)
                if len(answer)==k:
                    return answer
