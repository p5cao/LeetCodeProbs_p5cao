class Solution {
public:
    int getSum(int a, int b) {
        int diff, carry;
        while (b){
            diff = a^b; // exclusive or for 4 binary digits
            carry = (uint32_t)(a&b) << 1; //if produces a carry, shift 1
            a = diff;
            b = carry;
        }
        return a;
    }
};