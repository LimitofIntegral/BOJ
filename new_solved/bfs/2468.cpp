#include <bits/stdc++.h>
#define pii pair<int, int>
using namespace std;

int n, i, j, k, y, y_, x, x_, temp, r, res = 0;
int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, 1, -1};
int a[101][101];
bool v[101][101] = {false};
queue< pii > q;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;

    for (i = 0;i < n;i++){
        for (j = 0;j < n;j++){
            cin >> a[i][j];
        }
    }

    for (r = 0;r <= 100;r++){
        memset(v, false, 10101);
        temp = 0;

        for (i = 0;i < n;i++){
            for (j = 0;j < n;j++){
                if (a[i][j] - r > 0 && !v[i][j]) {
                    q.push(make_pair(i, j));
                    v[i][j] = true;
                    temp++;

                    while(!q.empty()){
                        y_ = q.front().first;
                        x_ = q.front().second;
                        q.pop();

                        for (k = 0;k < 4;k++){
                            y = y_ + dy[k];
                            x = x_ + dx[k];

                            if (y == -1 || y == n || x == -1 || x == n || v[y][x])continue;
                            
                            if (a[y][x] - r > 0){
                                q.push(make_pair(y, x));
                                v[y][x] = true;
                            }
                        }
                    }
                }
            }
        }


        res = max(res, temp);
    }

    cout << res;
    return 0;
}