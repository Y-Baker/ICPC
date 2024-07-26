#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

#define endl "\n"
#define ll long long

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int binarySearch(const vector<int>& arr, int lowerRange, int upperRange) {
    int l = 0;
    int r = arr.size() - 1;

    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (arr[mid] < lowerRange) {
            l = mid + 1;
        } else if (arr[mid] > upperRange) {
            r = mid - 1;
        } else {
            return mid;
        }
    }
    return -1;
}



int main() {
    fastIO();
    int t;
    cin >> t;

    for (int _ = 0; _ < t; _++) {
        int n, q;
        cin >> n >> q;
        string one, two;
        cin >> one >> two;

        unordered_map<char, vector<int>> mapp;
        for (int i = 0; i < n; i++) {
            mapp[two[i]].push_back(i);
        }

        while (q--) {
            int i, j;
            cin >> i >> j;
            i -= 1;
            j -= 1;
            int cnt = 0;
            unordered_map<char, vector<int>> maptmp = mapp;

            for (int k = i; k <= j; k++) {
                if (!maptmp[one[k]].empty()) {
                    int idx = binarySearch(maptmp[one[k]], i, j);
                    if (idx == -1) {
                        cnt += 1;
                    } else {
                        maptmp[one[k]].erase(maptmp[one[k]].begin() + idx);
                    }
                } else {
                    cnt += 1;
                }
            }
            cout << cnt << endl;
        }
    }

    return 0;
}
