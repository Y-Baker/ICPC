#include <iostream>

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
    cin>>n;

    string s;
    while (n--)
    {
        cin>>s;
        int i = 0;
        while (!s.empty() && i < s.size() - 1)
        {
            if ((s.at(i)=='A' && s.at(i+1)=='B') ||(s.at(i)=='B' && s.at(i+1)=='A') || (s.at(i)=='B' && s.at(i+1)=='C') ||(s.at(i)=='C' && s.at(i+1)=='B'))
            {
                s.erase(i,2);
                i = 0;
            } else {
                i++;
            }
        }
        if(s.size()==0)
        {
            cout<<"YES\n";
        }
        else 
        cout <<"NO\n";
    }
}
