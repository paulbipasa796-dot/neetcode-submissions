class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num] = 1+ count.get(num,0)
        arr=[]
        for num,c in count.items():
            arr.append([c,num])
        arr.sort(reverse=True)

        res = []
        for j in arr[:k]:
            res.append(j[1])
        return res

            