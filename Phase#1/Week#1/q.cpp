#include <iostream>
#include <vector>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int t, n, m;
    int count = 0;
    cin >> t;

    while(t--) {
        count = 0;
        cin >> n >> m;
        vector <pair<int, bool>> v(n);
        for (int i = 0; i < n; i++) {
            cin >> v[i].first;
            if (i == m) {
                v[i].second = true;
            } else {
                v[i].second = false;
            }
        }
        while (true)
        {
            int max_index = 0;
            for (int i = 1; i < n; i++) {
                if (v[i].first > v[max_index].first) {
                    max_index = i;
                }
            }
            for (int i = 0; i < max_index; i++) {
                v.push_back(v[0]);
                v.erase(v.begin());
            }
            count++;
            if (v[0].second) {
                cout << count << endl;
                break;
            }
            v.erase(v.begin());
        }
        
    }
}
