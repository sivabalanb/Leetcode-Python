class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        new_num = num
        while new_num != 0:
            if new_num %2==0:
                count+=1
                new_num /= 2
            else:
                new_num -= 1
                count+=1
            # print(f"new_num {new_num} count {count}")
        return count
            