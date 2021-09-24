class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;  
        int r = numbers.size() -1;
        cout <<"l:"<< l;
        cout << endl;
        cout <<"r:"<<r;
        vector<int> arr(2);
        while (l<r ){
            int sum=numbers[l]+numbers[r];
            if (sum==target) {
                arr = {l+1,r+1};
                break;
            }
            else if (sum > target) r--;
            else if (sum < target) l++;
        }
        return arr;
    }
};