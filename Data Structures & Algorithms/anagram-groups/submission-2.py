class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for word in strs:
            asci = [0] * 26
            arr = list(word)

            for letter in word:
                asci[ord(letter) - 97] += 1

            key = ",".join(map(str, asci))
            print(asci)
            res.setdefault(key, []).append(word)
        
        return list(res.values())

        