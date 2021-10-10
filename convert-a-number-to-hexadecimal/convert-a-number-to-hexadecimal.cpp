const string HEX = "0123456789abcdef";
class Solution {
public:
    string toHex(int num) {
        string s;
        // char map[16] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', 
        //                 '9', 'a', 'b', 'c', 'd', 'e'};
        if (num == 0) return "0";
        while (num!=0 && s.size() < 8){
            s = HEX[(num & 0xf)] + s;
            num >>= 4; // shift 4 bin digits
        }
        return s;
    }
};