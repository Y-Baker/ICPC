#include <iostream>
#include <deque>
using namespace std;

void process(deque<int> &R, deque<int> &A);


int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        deque<int> R, A;
        for (int i = 0; i < n; i++) {
            R.push_back(i+1);
        }

        process(R, A);

        for (int i = 0; i < n; i++) {
            cout << A[i];
            if (i < n-1) {
                cout << " ";
            }
        }
        cout << endl;
    }


}

void process(deque<int> &R, deque<int> &A) {
    while(!R.empty()) {
        if (A.size() > 1) {
            A.push_front(A.back());
            A.pop_back();
        }
        A.push_front(R.back());
        R.pop_back();
    }
}
