#include <iostream>
#include <stack>
using namespace std;

int main() {
    int max = 0;
    int count = 0;
    int number_max = 1;
    int total_streak = 0;

    string s;
    cin >> s;

    stack<char> stc;
    stack<int> sti;
    stack<int> streak;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[' || s[i] == '<') {
            stc.push(s[i]);
            sti.push(i);
        } else {
            if (!stc.empty() && ((s[i] == ')' && stc.top() == '(') ||
                               (s[i] == '}' && stc.top() == '{') ||
                               (s[i] == ']' && stc.top() == '[') ||
                               (s[i] == '>' && stc.top() == '<'))) {
                    stc.pop();
                    streak.push(2);
                    sti.pop();
            } else {
                while (!streak.empty()) {
                    int value = streak.top();
                    if (value != -1) {
                        count += value;
                    }
                    streak.pop();
                }
                if (count != 0 && count == max) {
                    number_max++;
                }
                if (count > max) {
                    max = count;
                }
                count = 0;
                streak.push(-1);
                while(!stc.empty()) {
                    stc.pop();
                    sti.pop();
                }
            }
        }
    }
    while (!streak.empty()) {
        int value = streak.top();
        if (value != -1) {
            count += value;
        }
        streak.pop();
    }
    if (count != 0 && count == max) {
        number_max++;
    }
    if (count > max) {
        max = count;
    }
    cout << max << " " << number_max << endl;
}
