from typing import List, Set

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = self.get_common_prefix(strs)
        return self.get_longest_common_prefix(common_prefix)

    def get_common_prefix(self, strs: List[str]) -> List[Set]:
        strs.sort(key=lambda x: len(x))
        common_prefix = list()

        for string in strs:
            for index, character in enumerate(string):
                try:
                    common_prefix[index].add(character)
                except IndexError:
                    common_prefix.append({character})
                
        if strs:
            minimum_str_length = len(strs[0])
            return common_prefix[:minimum_str_length]
        return []

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