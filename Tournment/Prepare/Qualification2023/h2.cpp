#include <iostream>
#include <string>
#include <numeric>
#include <cstdlib>
#define endl "\n"
#define ll long long

using namespace std;
int sum_digits(const string &str, int start, int end) {
    int cnt = 0;
    for (int i = start; i < end; i++) {
        cnt += str[i] - '0';
    }
    return cnt;
}



void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

    
int main() {
    fastIO();
    int t;
    cin >> t;
    
    while (t--) {
        string str_n;
        cin >> str_n;
        int n = stoi(str_n);
        int arr[] = {196, 394, 592, 790, 970};
        
        int sum_first = sum_digits(str_n, 0, 3);
        int sum_last = sum_digits(str_n, 3, 6);
        
        if (sum_first == 16 && sum_last == 16) {
            cout << "YES" << endl;
            continue;
        }
        
        if (sum_first != 16) {
            cout << "NO" << endl;
            continue;
        }
        
        int last_three = n % 1000;
        int start = (str_n[3] - '0') * 100 + (str_n[4] - '0')  * 10 + (str_n[5] - '0') ;
        int k = (last_three / 200);
        int end = (200 * (last_three / 200)) + 200;
        
        bool valid = true;
        if (start > arr[k]) {
            valid = false;
        }
        
        cout << (valid ? "YES" : "NO") << endl;
    }
    
    return 0;
}
