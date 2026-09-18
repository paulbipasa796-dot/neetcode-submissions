class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res=[]
        for num in nums:
            count[num] = 1 + count.get(num,0)
        heap = []
        
        for num, c in count.items():
            heapq.heappush(heap,[c,num])
            if len(heap)>k:
                heapq.heappop(heap)
        for j in heap[:k] :
            res.append(j[1])
        return res