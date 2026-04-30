class Solution:

    def encode(self, strs: List[str]) -> str:
        # get the length of eah string
        #append that len as a pre to word and keep adding in string
        encoded=""
        for s in strs:
            n=len(s)
            word=str(n)+"$"+s
            encoded = encoded+word
       # print(encoded)
        return encoded



    def decode(self, s: str) -> List[str]:
        # first get the number and convert into int and keep going ahead till the number ened
        words=[]
        i=0
        print(s)
        while i< len(s):
            j=i
            while j<len(s) and s[j].isdigit():
                j += 1

        
            count = int(s[i:j])
            if j < len(s):
                j += 1

            chunk = s[j:j+count]
            words.append(chunk)

            i=j+count
        return words
