#https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(":")
        start_num, end_num = int(start[1]), int(end[1])
        start_ord, end_ord = ord(start[0]), ord(end[0])
        # print(f"start{start} end {end}")
        requ_char = [chr(x) for x in range(start_ord, end_ord+1)]
        result = []
        for c in requ_char:
            for num in range(start_num, end_num+1):
                result.append(c+str(num))
                # print(result)
        return result
            
        