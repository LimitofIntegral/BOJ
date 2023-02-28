#include <bits/stdc++.h>
#define pii pair<int, int>
using namespace std;

int n, m, i, j, k, row;
int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, 1, -1};
int a[100][100];
bool v[100][100];
queue<pii> q;

bool check(int n, int i, int j, int k){
    return (n == i || n == j || n == k);
}

bool dfs(int y_, int x_){
    if (y_ == n - 1)return true;
    int y, x;
    bool res;

    for (int d = 0;d < 4;d++){
        y = y_ + dy[d];
        x = x_ + dx[d];

        if (y == -1 || x == -1 || x == m || v[y][x] || !check(a[y][x], i, j, k))continue;

        v[y][x] = true;
        if (dfs(y, x))return true;
    }

    return false;
}

bool bfs(int y_, int x_){
    q.push(make_pair(y_, x_));
    int y, x, yy, xx;

    while (!q.empty()){
        yy = q.front().first;
        xx = q.front().second;
        q.pop();

        for (int d = 0;d < 4;d++){
            y = yy + dy[d];
            x = xx + dx[d];

            if (y == -1 || x == -1 || x == m || v[y][x] || !check(a[y][x], i, j, k))continue;

            v[y][x] = true;
            if (y == n - 1)return true;
            q.push(make_pair(y, x));
        }
    }

    return false;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> m >> n;
    for (i = 0;i < n;i++){
        for (j = 0;j < m;j++){
            cin >> a[i][j];
        }
    }

    for (i = 0;i < 10;i++){
        for (j = 0;j < 10;j++){
            for (k = 0;k < 10;k++){
                for (row = 0;row < m;row++){
                    memset(v, false, 10000);
                    if (!check(a[0][row], i, j, k))continue;
                    // bfs <=> dfs 교체 가능
                    if (bfs(0, row)){
                        cout << i << ' ' << j << ' ' << k;
                        return 0;
                    }
                }
            }
        }
    }
    cout << "-1 -1 -1";
    return 0;
}