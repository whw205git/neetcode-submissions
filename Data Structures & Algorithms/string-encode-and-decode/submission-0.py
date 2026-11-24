class Solution:

    # Encode hello to 5#hello
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += f"{len(string)}#{string}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Find the delimiter
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])

            start_of_str = j+1
            decoded_string = s[start_of_str:start_of_str+size]
            result.append(decoded_string)

            i = start_of_str+size
        
        return result