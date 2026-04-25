class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> res = {};

        for (int i = 0; i < nums.size(); i++) {
            // if smallest is positive then impossible to sum to 0
            if (nums[i] > 0) {
                break;
            }
            else if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r) {
                int three_sum = nums[i] + nums[l] + nums[r];

                if (three_sum > 0) {
                    --r;
                }
                else if (three_sum < 0) {
                    ++l;
                }
                else {
                    vector<int> combo = {nums[i], nums[l], nums[r]};
                    res.push_back(combo);
                    ++l;
                    --r;
                    while (nums[l] == nums[l - 1] && l < r) {
                        l++;
                    }
                }
            }

        }

        return res;
    }
};