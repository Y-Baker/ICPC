#include <iostream>
#include <vector>
#include <map>
#define endl "\n"
#define int long long

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void backtrack(vector<vector<int>>& res, vector<int>& temp, vector<int>& nums, int start) {
    res.push_back(temp);
    for (int i = start; i < nums.size(); i++) {
        temp.push_back(nums[i]);
        backtrack(res, temp, nums, i + 1);
        temp.pop_back();
    }
}

vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> res;
    vector<int> temp;
    backtrack(res, temp, nums, 0);
    return res;
}

int32_t main() {
    fastIO();
    int t = 1;
    // cin >> t;

    for (int _ = 0; _ < t; _++) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        vector<vector<int>> subsetsVec = subsets(arr);
        map<pair<int, int>, int> cashe;
        int ans = 0;
        for (const auto& subset : subsetsVec) {
            if (subset.empty()) continue;
            int curr = subset[0];
            for (int j = 1; j < subset.size(); j++) {
                int one = min(curr, subset[j]);
                int two = max(curr, subset[j]);
                pair<int, int> key = make_pair(one, two);
                if (cashe.find(key) != cashe.end()) {
                    curr = cashe[key];
                    continue;
                }

                curr = one | two;
                cashe[key] = curr;
            }
            ans += curr;
        }
        cout << ans << endl;
    }

    return 0;
}
