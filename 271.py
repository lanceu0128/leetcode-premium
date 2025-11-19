# Encode and Decode Strings

class Codec:
    def encode(self, strs: List[str]) -> str:
        return "\n".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("\n")     

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
