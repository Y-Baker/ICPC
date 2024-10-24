#include <iostream>

#define endl "\n"
#define ll long long

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int t;
    cin >> t;

    while(t--) {
        int n, m;
        cin >> n >> m;
        char grid[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                cin >> grid[i][j];
        }
        int maxx = -1;
        pair<int, int> max_point = {0, 0};

        int x1, x2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                pair<int, int> point = {i, j};
                int count = 0;
                x1 = 0;
                x2 = 0;
                while (i + x1 < n && i - x1 >= 0 && j + x2 < m && j - x2 >= 0) {
                    if (grid[i + x1][j] == '.' || grid[i - x1][j] == '.' || grid[i][j + x2] == '.' || grid[i][j - x2] == '.') {
                        break;
                    }
                    x1++;
                    x2++;
                    count++;
                }
                if (count > maxx) {
                    maxx = count;
                    max_point = {i, j};
                }
            }
        }
        cout << max_point.first + 1 << " " << max_point.second + 1 << endl;
    }
}
