#include <iostream>
#include <map>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();
    int t;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;
		map<string, long long>pairs;
		map<char, long long>p1, p2;
		long long count = 0;
		while (n--)
		{
			string s;
			cin >> s;

			count += p1[s[0]] + p2[s[1]] - 2 * pairs[s];

			p1[s[0]]++;
			p2[s[1]]++;
			pairs[s]++;
		}
		cout << count << endl;
	}
	return 0;
}
