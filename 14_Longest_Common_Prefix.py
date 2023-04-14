class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        # loop over each character of strs[0]
        # loop will end due to return statment thus no out of bound error
        for i in range(1, len(strs[0]) + 1):
            prefix = strs[0][:i]
            # loop over each word and compare with prefix
            for str in strs:
                if str[:i] != prefix:
                    return prefix[:- 1]

        # when strs[0] is the shortest string and also is prefix
        return prefix

ans = Solution()
strs = ["flowingg", 'flow', 'flo']
print(ans.longestCommonPrefix(strs))
                

