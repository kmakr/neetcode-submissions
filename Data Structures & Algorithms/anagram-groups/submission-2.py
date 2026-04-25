class Solution:
    def getCharCount(self, word: str):
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1

        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = defaultdict(list)
    
        for st in strs:
            groupedAnagrams[self.getCharCount(st)].append(st)
        
        return list(groupedAnagrams.values())

    
