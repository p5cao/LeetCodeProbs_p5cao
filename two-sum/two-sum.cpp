class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hashMap;
        vector<int> arr(2);
        for(int i = 0; i< nums.size(); i++){
            hashMap[nums[i]] = i;
        }
        for(int i = 0; i< nums.size(); i++){
            int diff = target - nums[i];
            if (hashMap[diff]){
                arr[0] = hashMap[diff];
                if (hashMap[diff]!= i){
                arr[1] = i;
                }
            }
        }
        return arr;
    }
};