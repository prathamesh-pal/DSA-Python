from typing import List
class Codec:
    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for i in strs:
            encoded += str(len(i))+"#"+i
        return encoded
        
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i =0
        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
                lenght = int(s[i:j])
                string = s[j+1 : j+1+lenght]
                print(string)
                decoded.append(string)
                i = j+1+lenght
        return decoded
            


codec = Codec()

original = ["hello", "world", "", "123"]
encoded = codec.encode(original)
print("Encoded:", encoded)

decoded = codec.decode(encoded)
print("Decoded:", decoded)