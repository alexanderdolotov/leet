#include <vector>
#include <unordered_map>

using namespace std;


// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};




class Solution {

public:
    unordered_map<Node*, Node*> visited;
    Node* cloneGraph(Node* node) {

        if(node == nullptr){
            return nullptr;
        }
        
       visited = unordered_map<Node*, Node*>();
       return clone(node, visited);
    }

private:
    Node* clone(Node* node, unordered_map<Node*, Node*>& visited) {
        if (visited.count(node)) {
            return visited[node];
        }

        Node* new_node = new Node(node->val);
        visited[node] = new_node;

        for (Node* neighbor : node->neighbors) {
            new_node->neighbors.push_back(clone(neighbor, visited));
        }

        return new_node;
    }
};


