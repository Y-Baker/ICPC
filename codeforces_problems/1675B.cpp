#include <iostream>
#include <vector>
#include<cmath>
using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

bool check1(const vector<int>& array) {
    for (int i = 0; i < array.size() - 1; i++) {
        if (array.at(i) >= array.at(i + 1)) {
            return false;
        }
    }
    return true;
}


void fn() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr.at(i);

    int counter = 0;
    if (n==1) {
        cout<<0<<endl;
        return;
    }

    while (!check1(arr)) {
        for (int i = 0; i < n - 1; i++) {
            int x ;
            if (arr.at(i) >= arr.at(i + 1)) {
                if (arr.at(i+1) == 0) {
                    cout << -1 << endl;
                    return;
                }
                if(arr.at(i)==arr.at(i+1)){
                    x=1 ;
                }
                else {x =ceil(log2((double) arr.at(i) / arr.at(i + 1)));}
                arr.at(i) /= pow(2,x) ;
                counter +=x ;
            }
        }
    }

    cout << counter << endl;
}

int main() {
    fastIO();
    int t;
    cin >> t;
    while (t--) {
        fn();
    }
    return 0;
}
