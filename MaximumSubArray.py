#LeetCode #53
# Find maximum length of subarray
# Sliding Window style problem
def MaximumSubArray(nums: list[int])-> int:
    maxSum = nums[0]
    currSum = 0

    if len(nums) < 2:
        return maxSum;
    for i in nums:
        if currSum < 0:
            currSum = 0
        currSum+=i
        maxSum = max(maxSum, currSum)
    return maxSum


#LeetCode #238
#Product of array except itself
def productOfArray(nums: list[int]) -> list[int]:
    output = [1] * len(nums)
   # print(f"Initial Output Array Initialization: {output}")
    prefix, postfix = 1,1
    for i,n in enumerate(nums):
        output[i] = prefix
        prefix = prefix * n
    
    for i in range(len(nums)-1,-1,-1):
        print(i)
        output[i] = postfix * output[i];
        postfix = postfix * nums[i]
    return output

if __name__ == "__main__":
    val = MaximumSubArray([-1,1,-3,4,-1,2,1,-5,4])
    print(val)

    product = productOfArray([2,1,6])
    print(product)


