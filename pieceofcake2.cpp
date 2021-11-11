#include <iostream>
using namespace std;

int main()
{
    int v1 = 0, h1 = 0, n1 = 0, w2 = 0, h2 = 0, x5 = 0;
    cin >> n1 >> h1 >> v1;
    x5 = 0.5 * n1;
    
    if (h1 > x5) {
        h2 = h1;
    } else {
        h2 = n1 - h1;
    }
    if (v1 > x5) {
        w2 = v1;
    } else {
        w2 = n1 - v1;
    }

    int volume = 4 * w2 * h2;
    cout << volume << endl;
}
