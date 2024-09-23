
def CheckDuplicate(nums: list[int])-> bool:
    dict = {}
    s = set()

    for i,n in enumerate(nums):
        if n in s:
            return True;
        else:
            s.add(n)
    print(s)
    return False




if __name__ == "__main__":
    print(CheckDuplicate([1,2,3,4,5,1]))
   

