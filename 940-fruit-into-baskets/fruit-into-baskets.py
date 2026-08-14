class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ## O(n) Time, O(k) Space k<n
        max_fruits = 0
        left = 0
        fruit_count = defaultdict(int)
        for right,fruit in enumerate(fruits):
            fruit_count[fruit] += 1
            if len(fruit_count)>2:
                fruit_count[fruits[left]]-=1
                if fruit_count[fruits[left]]==0:
                    del fruit_count[fruits[left]]
                left += 1
            if len(fruit_count)<=2:
                max_fruits = max(right-left+1,max_fruits)
        return max_fruits

        ## O(n) Time, O(1) Space
        ## Only works for 2 baskets is not a scalable solution
        # last = second_last = -1
        # last_count = curr = res = 0
        # for f in fruits:
        #     if f==last or f==second_last:
        #         curr+=1
        #     else:
        #         curr=last_count+1
        #     if f==last:
        #         last_count += 1
        #     else:
        #         second_last,last = last,f
        #         last_count = 1
        #     res = max(res,curr)
        # return res