class Solution:
    from itertools import islice
    def rec_fun(self, remove, s):
        return s.replace(remove, "")
    def del_duplicate(self, result, k, total_runs, final_res):
        stack = ''
        no_duplicates = []
        idx = 0
        loop_count = len(result)
        
        while idx + k <= loop_count:
            total_runs += 1
            
            stack += result[idx:idx+k]
            if len(set(stack)) == 1:
                # print("to be removed",stack)
                # result = result.replace(stack,"")
                final_res = final_res[:idx]
                no_duplicates.append(False)
                idx = idx+k
                loop_count = len(final_res)

            else:
                final_res += stack
                idx+=1
            # print(f" idx {idx} loop_count {loop_count} Stack {stack} and result {final_res}")
            stack =''
            
        return result, no_duplicates, total_runs, final_res
    def removeDuplicates(self, s: str, k: int) -> str:
        result = ''
        final_res = ''
        total_runs = 0
        flag = True
        while flag:
            result, no_duplicates, total_runs, final_res = self.del_duplicate(s, k, total_runs,final_res)
            s = result
            # print("no duplicates", no_duplicates)
            if not no_duplicates:
                flag = False
            # print("result", result)
            
            print("total_runs", total_runs)
        return result
        
        
            
        