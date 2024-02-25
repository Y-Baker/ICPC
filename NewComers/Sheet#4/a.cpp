#include <sstream>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    int count = 0;
    int start = 0;
    vector<int> v;
    for (char c : str) {
        if (c != ',') {
            count++;
        } else {
            string temp = str.substr(start, count);
            start += count + 1;
            count = 0;
            int i = stoi(temp);
            
            v.push_back(i);
        }
    }
    string temp = str.substr(start, count);
    v.push_back(stoi(temp));
    return v;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
