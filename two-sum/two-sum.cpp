class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> arr(2);
        // O(n^2)
        for (int i =0; i<nums.size(); i++){
            for (int j =0; j<nums.size(); j++){
                if (nums[i] + nums[j] == target){
                    arr[0] = i;
                    if (i != j){
                    arr[1] = j;
                    }
                }
            }
        }
        return arr;    
    }
};