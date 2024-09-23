class Solution:
    def TwoSum(num: list[int], target: int) -> list[int]:
        dict = {} 
        output = []
        for i, n in enumerate(num):
            if (target - n) in dict:
                output.append([dict[target-n], i])
            else:
                dict[n] = i
        return output
    

    # Best time to sell Stock question : LeetCode #121
    def BestProfit(nums: list[int]) -> int:
        l, r = 0,1
        Profit = 0
        while (r < len(nums)):
            if nums[l] < nums[r]:
                Profit = max( Profit, (nums[r] - nums[l]))
            else:
                l = r
            r+=1;
        return Profit;

if __name__ == "__main__":
    result = Solution.TwoSum([1,2,3,4,5], 5)
    print (result)

    profit = Solution.BestProfit([7,1,6,3,5,1])
    print(profit)

    nums = [1,1,2,3,1,2,5]
