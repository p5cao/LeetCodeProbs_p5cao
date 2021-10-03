class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0b11111111111111111111111111111111       
        MAX =  0b01111111111111111111111111111111
        
        while b:
            diff, carry = a, b
            diff = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a,b = diff, carry
     
        return a if a <= MAX else ~(a ^ mask)
        
       
