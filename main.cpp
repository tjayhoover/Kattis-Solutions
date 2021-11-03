#include <iostream>
#include <vector>
#include <stack>
using namespace std;


int main() {
    int sz = 0;
    vector<int> cards;

    cin >> sz;
    for (int i=0; i<sz; ++i) {
        int c;
        cin >> c;
        cards.push_back(c);
    }

    sort(cards.begin(), cards.end(), [](int a, int b) (return a>b;))
    stack<int> stk;

    for (auto c : cards) {
        if (!stk.empty() || ((c+stk.top()) % 2) != 0) {
            stk.push(c);
        }
        else {
            stk.pop();
        }
    }

    cout << stk.size()<< endl;
}
