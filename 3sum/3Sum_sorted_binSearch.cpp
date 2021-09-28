class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int threeSum;
        std::vector<int> arr;
        std::vector< vector<int> > output;
        
        if (nums.size() < 3) return output;
        for (int i = 0; i < nums.size()-2; i++){
            if (nums[i] > 0) break;
            if (i > 0 && nums[i-1]== nums[i]) continue;
            
            // initialize left right pointers
            int l = i + 1;
            int r = nums.size() - 1;
            while (l<r){
                threeSum = nums[i] + nums[l] + nums[r];
                if (threeSum == 0){
                    int a[] = {nums[i], nums[l], nums[r]};
                    arr.assign(a, a+3);
                    output.push_back(arr);
                    l++;
                    while (nums[l-1] == nums[l] && l<r){
                        l++;
                    }
                }
                else if (threeSum > 0) r--;
                else if (threeSum < 0) l++;
                }
            }
            return output;
        }
};
