#include <bits/stdc++.h>

using namespace std;


int main() {


    int t = 1;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        int c[26];
        bool a[26];
        map<int, int> mapp;

        vector<int> arr(n + 1);
        for(int i = 1; i <= n; i++)
        {
            cin >> arr[i];
        }
    
	    int q; cin >> q;
	    for(int i = 1; i <= q; i++) {
	    	string q;
            cin >> q;
	    	mapp.clear();

	    	if(q.size() != n) {
	    		cout << "NO" << '\n';
	    		continue;
	    	}

	    	for(int j = 0; j < 26; j++) {
	    		a[j] = false;
	    	}

	    	bool valid = true;
	    	for(int i = 0; i < n; i++) {
	    		int d = q[i] - 'a';
	    		if(!a[d]) {
	    			if(mapp[arr[i + 1]]) {
                        valid = false;
                    }
	    			mapp[arr[i + 1]] = true;
	    			a[d] = true;
	    			c[d] = arr[i + 1];
	    		}

	    		valid &= (c[d] == arr[i + 1]);
	    	}

	    	cout << (valid ? "YES" : "NO") << endl;
	    }
    }
    return 0;
}
