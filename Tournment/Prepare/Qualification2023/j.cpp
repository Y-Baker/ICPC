#include <iostream>
#include <deque>
#include <algorithm>
// #include <set>

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
    int n, q ;
    cin >> n>> q ;
    deque<string> arrN (n) ;
    deque<string> arrQ (q) ;
    deque<string> ans;
    
    for (int i =0;i<n;i++) cin >> arrN[i] ;
    for (int i =0;i<q;i++) cin >> arrQ[i] ;
    for (int i=0;i<q;i++){
        ans.clear();
        for (int j=0;j<n;j++){
            bool flag = true;
            for (int idx = 0; idx < 5; idx++) {
                if (arrQ[i][idx] == '?' ||arrN[j][idx] == arrQ[i][idx]) {
                    continue;
                } else {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                ans.push_back(arrN[j]);
            }
        }
        sort(ans.begin(), ans.end());
        for (auto it = ans.begin(); it != ans.end(); it++) {
            cout << *it << endl;
        }
    }
}
