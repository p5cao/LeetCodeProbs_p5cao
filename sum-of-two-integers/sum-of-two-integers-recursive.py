class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0b11111111111111111111111111111111       
        MAX =  0b01111111111111111111111111111111
        
        if b == 0:
            return a if a <= MAX else ~(a ^ mask)
        
        return self.getSum(
            (a ^ b) & mask,
            ((a & b) << 1) & mask
        )
