#include <iostream>
using namespace std;
bool isSubString(string S, string T);

int main() {
    string S;
    string T;
    cin >> S >> T;
    if (T == "") {
        cout << "YES";
        return 0;
    }
    
    if (isSubString(S, T)) {
        cout << "Yes";
    } else {
        cout << "No";
    }
}

bool isSubString(string S, string T) {
    if (S.find(T) != string::npos){
        return true;
    } else {
        return false;
    }
}
