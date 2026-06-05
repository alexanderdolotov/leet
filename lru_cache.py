'''
146. LRU Cache
Medium
Topics
premium lock iconCompanies

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

 

Constraints:

    1 <= capacity <= 3000
    0 <= key <= 10^4
    0 <= value <= 10^5
    At most 2 * 10^5 calls will be made to get and put.

 

'''


# only beats 15%

DEBUG = True

class Node:

    key: int = None
    val:int = None 
    ranking = 0
    next = None
    prev = None
    def __init__(self, key, val, ranking, next=None, prev=None):
        self.key = key
        self.val = val 
        self.ranking = ranking
        self.next = next
        self.prev=prev




class LRUCache:

    lru:dict[int,Node] = None 
    least_used_node:Node = None
    most_used_node:Node = None
    max_capacity = 1
    current_capacity = 0
    time = 0

    def __init__(self, capacity: int):

        self.lru = {}
        self.max_capacity = capacity
        self.current_capacity = 0
        self.time = 1

        if DEBUG:
            print('initiated LRU: ', self.lru, 'max capacity: ', self.max_capacity )
        
        
    def adjust_nodes(self, node: Node):

        if node is self.most_used_node: # do nothing
            return 


       # remove node from middle 
        if node is self.least_used_node:
            self.least_used_node = self.least_used_node.next # move up the least node
            self.least_used_node.prev = None
        else:

            prevNode = node.prev 
            nextNode = node.next 

            prevNode.next = nextNode
            nextNode.prev = prevNode
        

        # always set node ot be new max node
        node.prev = self.most_used_node 
        self.most_used_node.next = node 
        self.most_used_node = node
        node.next = None

        if DEBUG:
            print('after node adj, most used: ', self.most_used_node.key, 'least: ', self.least_used_node.key)
       




    def get(self, key: int) -> int:
        if DEBUG:
            print(self.lru.keys())

        self.time += 1

        if self.lru and key in self.lru:
            node = self.lru[key]
            node.ranking = self.time

            self.adjust_nodes(node)

            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        self.time += 1
        
        if self.lru is not None and self.max_capacity > 0:
            if key in self.lru:
                found_node = self.lru[key]
                found_node.ranking = self.time
                found_node.val = value
                self.adjust_nodes(node=found_node)

            else:
                # check capacity 
                if self.current_capacity < self.max_capacity:
                    
                    self.current_capacity += 1
                    node = Node(key=key, val=value, ranking=self.time, prev=self.most_used_node)
                    if DEBUG:
                        print('adding node ', node.key)

                    self.lru[key] = node 

                    if self.most_used_node:
                        self.most_used_node.next = node
                        self.most_used_node = node
                        
                    else:
                        self.most_used_node = node 
                        self.least_used_node = node
                        self.least_used_node.prev = None

                else:
                    # if over capacity 
                    node = Node(key=key, val=value, ranking=self.time, prev=self.most_used_node)

                    # pop last used node 
                    
                    if DEBUG:
                        print('adding node ', node.key)

                    self.lru[key] = node 

                    if DEBUG:
                        print('removing node: ', self.least_used_node.key)

                    self.lru.pop(self.least_used_node.key) # remove least used node 

                    if self.most_used_node:
                        if self.max_capacity > 1:

                            self.most_used_node.next = node
                            self.most_used_node = node
                            self.least_used_node = self.least_used_node.next
                            self.least_used_node.prev = None


                        else:
                            self.most_used_node = node 
                            self.least_used_node = node
                            self.least_used_node.prev = None

                    else:
                        self.most_used_node = node 
                        self.least_used_node = node
                        self.least_used_node.prev = None


        if DEBUG:
            print('after put: ', self.lru.keys())


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




