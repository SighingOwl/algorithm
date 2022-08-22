#include <iostream>

using namespace std;

int main() {
    
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    int curr_x = 0, curr_y = 0;
    
    int n;
    cin >> n;

    char dir[n];
    int dist[n];
    for(int i = 0; i < n; i++) {
        cin >> dir[i] >> dist[i];
    }
    
    for(int i = 0; i < n; i++) {
        if(dir[i] == 78) {
            curr_y += dy[3] * dist[i];
        }
        else if(dir[i] == 83) {
            curr_y += dy[2] * dist[i];
        }
        else if(dir[i] == 69) {
            curr_x += dx[0] * dist[i];
        }
        else if(dir[i] == 87) {
            curr_x += dx[1] * dist[i];
        }
    }
    
    cout << curr_x << " " << curr_y << endl;
    
    return 0;
}