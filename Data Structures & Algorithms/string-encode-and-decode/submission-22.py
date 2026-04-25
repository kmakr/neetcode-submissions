class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""
        sentence = ''
        for s in strs:
            sentence += str(len(s)) + "#"
            sentence += s
            

        return sentence

    def decode(self, s: str) -> List[str]:
        print("String: " + '"' + s + '"')
        print("Length: " + str(len(s)))

        if s =="":
            return []
    
    
        res = []
        i = 0
        
        while (i < len(s)):
            print("length: " + s[i])
            length_word_string = ''
            while (s[i] != '#'):
                length_word_string += s[i]
                i += 1
            
            length_word = int(length_word_string)
        
            # length_word = int(s[i])
            word = s[i+1:i+1+length_word]
            print(word)
            res.append(word)
            
            i = i + length_word + 1

        
        return res
