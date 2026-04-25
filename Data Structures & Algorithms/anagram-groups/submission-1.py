class Solution:
    def toWordCount(self, word: str):
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1

        return count

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = defaultdict(list)

        for st in strs:
            summed = self.toWordCount(st)
            print(summed)
            summed = tuple(summed)

            if (summed in groupedAnagrams):
                groupedAnagrams[summed].append(st)
            else:
                groupedAnagrams[summed] = [st]
        
        return list(groupedAnagrams.values())

    
