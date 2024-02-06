#include <iostream>
#include <deque>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int n;
    cin >> n;

    deque <int> q;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        q.push_back(x);
    }

    int sereja = 0, dima = 0;
    bool turn = true;

    while (!q.empty()) {
        if (turn) { // sereja 
            if (q.front() > q.back()) {
                sereja += q.front();
                q.pop_front();
            } else {
                sereja += q.back();
                q.pop_back();
            }
        } else { // dima
            if (q.front() > q.back()) {
                dima += q.front();
                q.pop_front();
            } else {
                dima += q.back();
                q.pop_back();
            }
        }
        turn = !turn;
    }

    cout << sereja << " " << dima << endl;
}
