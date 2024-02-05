#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main() {
    int max = 0;
    int number_max = 1;

    string s;
    cin >> s;

    stack<char> stc;
    stack<int> sti;
    vector<int> streak(s.size(), 0);

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[' || s[i] == '<') {
            stc.push(s[i]);
            sti.push(i);
        } else if (!stc.empty() && ((s[i] == ')' && stc.top() == '(') ||
                               (s[i] == '}' && stc.top() == '{') ||
                               (s[i] == ']' && stc.top() == '[') ||
                               (s[i] == '>' && stc.top() == '<'))) {
                    stc.pop();
                    streak[i] = i - sti.top() + 1;
                    if (sti.top() - 1 > 0) {
                        streak[i] += streak[sti.top() - 1];
                    }
                    sti.pop();
                    if (max < streak[i]) {
                        max = streak[i];
                        number_max = 1;
                    } else if (max == streak[i]) {
                        number_max++;
                    }
                }
        else {
                while(!stc.empty()) {
                    stc.pop();
                    sti.pop();
                }
            }
        }

    cout << max << " " << number_max << endl;
}
