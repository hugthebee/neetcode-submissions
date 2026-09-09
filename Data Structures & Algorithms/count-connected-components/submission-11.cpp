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

    void unionfun(int x, int y, vector<int> &parent, vector<int> &rank)
    {
        int par1 = find(x,parent);
        int par2 = find(y,parent);

        if(rank[par2]>rank[par1])
        {
            parent[par1] = par2;
            rank[par2]+=rank[par1];
        }
        else
        {
            parent[par2] = par1;
            rank[par1]+=rank[par2];
        }
        return;
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        int unions = n;
        int e = edges.size();
        int x,y;

        vector<int> parent(n);
        vector<int> rank(n);

        for(int i=0;i<n;i++)
        {
            parent[i] = i;
            rank[i] = 1;
        }

        for(int i=0;i<e;i++)
        {
            x = edges[i][0];
            y = edges[i][1];
            if(find(x, parent)!=find(y, parent))
            {
                unionfun(x,y,parent,rank);
                unions--;
            }
        }

        return unions;
    }
};
