#include <iostream>
#include <utility>
#include <vector>
#include <unordered_map>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

struct hash_pair {
    template <class T1, class T2>
    size_t operator () (const pair<T1,T2> &p) const
    {
        auto hash1 = hash<T1>{}(p.first);
        auto hash2 = hash<T2>{}(p.second);
        return hash1 ^ hash2;
    }
};


int main() {
    fastIO();
    int n, m;
    cin >> n >> m;

    pair <int, int> arr[m];
    unordered_map<pair<int, int>, int, hash_pair> freq_pair;
    int freq[n] = {0};

    for (int i = 0; i < m; i++) {
        cin >> arr[i].first >> arr[i].second;
        freq[arr[i].first - 1]++;
        freq[arr[i].second - 1]++;

        freq_pair[make_pair(arr[i].first, arr[i].second)]++;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int duplicate = 0;
            if (i == j || freq[i] == 0 || freq[j] == 0) continue;

            duplicate = freq_pair[make_pair(i + 1, j + 1)] + freq_pair[make_pair(j + 1, i + 1)];
            if (freq[i] + freq[j] - duplicate >= m) {
                cout << "YES" << endl;
                return 0;
            }
        }
    }
    cout << "NO" << endl;
}
