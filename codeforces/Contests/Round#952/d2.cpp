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
        // int maxx = -1;
        // pair<int, int> max_point = {0, 0};

        bool flag = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '#') {
                    int cnt = 0;
                    int x = i;
                    while (x < n && grid[x][j] == '#') {
                        cnt++;
                        x++;
                    }
                    cnt -= 1;
                    cout << i+cnt/2+1 << " " << j+1 << endl;
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }
    }
}
