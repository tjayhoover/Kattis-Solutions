#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> max_sum(vector<int>& vec)
{
    int start_index { 0 };
    int end_index { 0 };
    int cur_sum { 0 };
    int max_sum { 0 };

    for (int i = 0; i < vec.size(); i++) {
        cur_sum += vec[i];
        if (cur_sum > max_sum) {
            max_sum = cur_sum;
            end_index = i;
        } else if (cur_sum < 0) {
            start_index = i + 1;
            cur_sum = 0;
        }
    }
    vector<int> ret = { start_index + 1, end_index + 1, max_sum };
    return ret;
}

int main()
{
    string str;
    int letter;
    vector<int> Rs;
    vector<int> Bs;

    cin >> str;

    for (int i = 0; i < str.size(); ++i) {
        if (str[i] == 'B') {
            Bs.push_back(1);
            Rs.push_back(-1);
        } else if (str[i] == 'R') {
            Rs.push_back(1);
            Bs.push_back(-1);
        }
    }

    vector<int> reds = max_sum(Rs);
    vector<int> blues = max_sum(Bs);

    if (reds[2] > blues[2]) {
        cout << reds[0] << " " << reds[1];
    } else if (reds[2] < blues[2]) {
        cout << blues[0] << " " << blues[1];
    } else if (reds[2] == blues[2]) {
        if (reds[0] < blues[0]) {
            cout << reds[0] << " " << reds[1];
        } else if (reds[0] > blues[0]) {
            cout << blues[0] << " " << blues[1];
        } else if (reds[0] == blues[0]) {
            if (reds[1] < blues[1]) {
                cout << reds[0] << " " << reds[1];
            } else
                cout << blues[0] << " " << blues[1];
        }
    }
}
