class Solution {
public:
    int find(int node, vector<int> parent)
    {
        while(parent[node]!=node)
        {
            node = parent[node];
        }

        return node;
    }

    // void union(int x, int y, vector<int> parent, vector<int> rank)
    // {

    // }

    int countComponents(int n, vector<vector<int>>& edges) {
        int unions = n;
        int e = edges.size();
        int x,y;

        vector<int> parent(n);
        vector<int> rank(n,1);

        for(int i=0;i<n;i++)
        {
            parent[i] = i;
        }

        for(int i=0;i<e;i++)
        {
            x = edges[i][0];
            y = edges[i][1];
            if(find(x, parent)!=find(y, parent))
            {
                parent[find(y,parent)] = find(x,parent);
                unions--;
            }
        }

        return unions;
    }
};
