#include <iostream>
#include <stack>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int t, count = 0;
    cin >> t;

    string s;


    while (t--)
    {
        count = 0;
        stack <char> q;
        stack <char> q2;
        cin >> s;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                q.push('(');
            } else if (s[i] == ')'){
                if (!q.empty() && q.top() == '(') {
                    q.pop();
                    count++;
                }
            } else if (s[i] == '[') {
                q2.push('[');
            } else if (s[i] == ']') {
                if (!q2.empty() && q2.top() == '[') {
                    q2.pop();
                    count++;
                }
            }
        }
        cout << count << endl;
    }
}
