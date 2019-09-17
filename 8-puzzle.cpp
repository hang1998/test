#include <iostream>
#include <queue>
#include <unordered_map>
#include <set>
using namespace std;

typedef struct node
{
    int state[3][3];
    struct node* parent;
    int action;
    int path_cost;
}node;
typedef node* node_pointer; 

node_pointer child_node(node_pointer parent, int action);
int det(node_pointer xyz);
void printnode(node_pointer xyz);

int main(int argc, char const *argv[])
{
    set<int> viewed;
    node_pointer result;
    int matrix[3][3] = {{5, 4, 0}, {6, 1, 8}, {7, 3, 2}};
    node_pointer root = (node_pointer) malloc(sizeof(node));
    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            root->state[i][j] = matrix[i][j];
        }
    }
    root->path_cost = 0;
    queue<node_pointer> bfs;
    bfs.push(root);
    while (!bfs.empty()) {
        node_pointer xyz = bfs.front();
        bfs.pop();
        for (int i = 1; i < 5; ++i)
        {
            node_pointer xyz_child = child_node(xyz, i);
            int temp = det(xyz_child);
            if (temp == 0) {
                result = xyz_child;
                break;
            }
            if (viewed.count(temp) == 0) {
                viewed.insert(temp);
                bfs.push(xyz_child);
            }
        }
    }
    printnode(result);
    return 0;
}

node_pointer child_node(node_pointer parent, int action){
    node_pointer son = (node_pointer) malloc(sizeof(node));
    son->parent = parent;
    son->action = action;
    son->path_cost = parent->path_cost + 1;
    int tempi = 0;
    int tempj = 0;
    int tempx = 0;
    int tempy = 0;
    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            son->state[i][j] = parent->state[i][j];
            if (parent->state[i][j] == 0)
            {
                tempi = i;
                tempj = j;
                tempx = i;
                tempy = j;
            }
        }
    }
    switch (action){
        case 1: tempi--; break;
        case 2: tempj++; break;
        case 3: tempi++; break;
        case 4: tempj--; break;
    }
    if (tempi >= 0 && tempj >= 0 && tempi < 3 && tempj < 3)
    {
        int temp = son->state[tempi][tempj];
        son->state[tempi][tempj] = son->state[tempx][tempy];
        son->state[tempx][tempy] = temp;
    }
    return son;
}

int det(node_pointer xyz){
    return xyz->state[0][0] * xyz->state[1][1] * xyz->state[2][2]
         + xyz->state[0][1] * xyz->state[1][2] * xyz->state[2][0]
         + xyz->state[0][2] * xyz->state[1][0] * xyz->state[2][1]
         - xyz->state[0][2] * xyz->state[1][1] * xyz->state[2][0]
         - xyz->state[0][0] * xyz->state[1][2] * xyz->state[2][1]
         - xyz->state[0][1] * xyz->state[1][0] * xyz->state[2][2];
}

void printnode(node_pointer xyz){
    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            cout << xyz->state[i][j] << " ";
        }
        cout << endl;
    }
}
