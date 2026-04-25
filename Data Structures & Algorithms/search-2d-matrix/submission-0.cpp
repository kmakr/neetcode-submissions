class Solution {
public:

    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        for (int i = 0; i < matrix.size(); ++i) {
            // binary search each row

            int l = 0, r = matrix[i].size() - 1;

            while (l <= r) {
                int mid = (l + r) / 2;

                if (matrix[i][mid] > target) {
                    r = mid - 1;
                }
                else if (matrix[i][mid] < target) {
                    l = mid + 1;
                }
                else {
                    return true;
                }
            }
        }        

        return false;
    }
};
