from typing import List, Set

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        common_prefix = self.get_common_prefix(strs)
        return self.get_longest_common_prefix(common_prefix)

    def get_common_prefix(self, strs: List[str]) -> List[Set]:
        minimum_str_length = len(strs[0])

        for string in strs:
            if minimum_str_length > len(string):
                minimum_str_length = len(string)

        common_prefix = list()

        for string in strs:
            for index, character in enumerate(string[:minimum_str_length]):
                try:
                    common_prefix[index].add(character)
                except IndexError:
                    common_prefix.append({character})
                
        return common_prefix

    def get_longest_common_prefix(self, common_prefix: List[Set]) -> str:
        longest_common_prefix = ""

        for prefix in common_prefix:
            if len(prefix) >= 2:
                break
            longest_common_prefix += prefix.pop()
        return longest_common_prefix


def test_longestCommonPrefix():
    solution = Solution()

    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert solution.longestCommonPrefix(["flower", "flow"]) == 'flow'
    assert solution.longestCommonPrefix([]) == ''
    assert solution.longestCommonPrefix(["dog","racecar","car"]) == ''

if __name__ == "__main__":
    solution = Solution()
    solution.longestCommonPrefix(["reflower","flow","flight"])