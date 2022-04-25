# brute force and sliding window

from typing import List


class Solution:
    def find_repeated_dna_sequences(self, s: str) -> List[str]:
        sequence_size = 10
        dna_sequences = set()
        repeated_dna_sequences = list()

        for index in range(len(s) - sequence_size + 1):
            current_dna_sequences = s[index : index + sequence_size]
            if current_dna_sequences in dna_sequences:
                if current_dna_sequences not in repeated_dna_sequences:
                    repeated_dna_sequences.append(current_dna_sequences)
            else:
                dna_sequences.add(current_dna_sequences)

        return repeated_dna_sequences


def test_solution():
    solution = Solution()
    assert solution.find_repeated_dna_sequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == [
        "AAAAACCCCC",
        "CCCCCAAAAA",
    ]
    assert solution.find_repeated_dna_sequences(s="AAAAAAAAAAAAA") == ["AAAAAAAAAA"]
    assert solution.find_repeated_dna_sequences(s="AAAAAAAAAAA") == ["AAAAAAAAAA"]
