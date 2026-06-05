#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <iostream>
#include <random>

template <typename KeyType, typename ValueType>
class HashTable {
private:
    static constexpr unsigned int HOP_RANGE = 4;

    struct Bucket {
        KeyType key;
        ValueType value;
        bool occupied;
        unsigned int hopInfo;

        Bucket() : occupied(false), hopInfo(0) {}
    };

public:
    unsigned int tableSize;
    double loadFactorThreshold;
    std::vector<Bucket> hashTable;
    class Iterator {
    public:
        Iterator(typename std::vector<Bucket>::iterator current, typename std::vector<Bucket>::iterator end)
                : current(current), end(end) {}

        Iterator& operator++() {
            ++current;
            while (current != end && !current->occupied) {
                ++current;
            }
            return *this;
        }

        bool operator!=(const Iterator& other) const {
            return current != other.current;
        }

        bool operator==(const Iterator& other) const {
            return current == other.current;
        }

        typename std::vector<Bucket>::iterator operator*() {
            return current;
        }

    private:
        typename std::vector<Bucket>::iterator current;
        typename std::vector<Bucket>::iterator end;
    };
    // TODO implement the following functions in ../src/HashTable.cpp
    //Hint: you will also need to implement a hashKey function which will allow you to
    // create hash values for different KeyTypes
    explicit HashTable(unsigned int size = 7, double threshold = 0.7);
    Iterator begin();
    Iterator end();
    ValueType& operator[](const KeyType& key);
    void updateValueForKey(const KeyType& key, ValueType newValue);
    void insert(const KeyType& key, const ValueType& value);
    ValueType* search(const KeyType& key);
    bool remove(const KeyType& key);
    void clear();
    unsigned int size() const;
    double loadFactor() const;

private:
    unsigned int hopRange = HOP_RANGE;
    // TODO implement the following functions in ../src/HashTable.cpp
    unsigned int findFreeSlot(std::vector<Bucket>& cTable, unsigned int startIndex, unsigned int& currentHop);
    void rehash();
};


#include <stdexcept>
#include <functional>

#include <string>
#include <vector>
#include <limits>
#include <type_traits>
#include <iostream>
using namespace std;


// Constructor. Initializes hashTable to initial input size with empty Buckets. 
template <typename KeyType, typename ValueType>
HashTable<KeyType, ValueType>::HashTable(unsigned int size, double threshold) {

   // cout << "created hashtable" << endl;
    this->tableSize = size;
    this->hashTable = std::vector<Bucket>(size,Bucket());  
    this->loadFactorThreshold = threshold;

}



// a hash function that maps int->uint, looks kinda random
static unsigned int knuth_hash(int x) {
    return static_cast<uint32_t>(x) * 2654435761u;  // Knuth's multiplicative constant. i.e. the golden ratio: (sqrt(5)-1)/2, multiplied by 2^32.
}


// wrapper hash function, where underlining hash function can be substituted. 
template <typename KeyType>
static unsigned int hash_f1(const KeyType& key){


    unsigned int hash1 = std::hash<KeyType>{}(key);
    return knuth_hash(hash1);

}


// utility function so I dont need to recalculate index distance all the time, with the wrap-around logic
static int get_hop_distance(unsigned int start_index, unsigned int end_index, unsigned int table_size){

    if(end_index >= start_index){
        return end_index - start_index;
    } else {
        return table_size - start_index + end_index; // end index looped around
    }

}


// Find free slot. Returns the available index that can be used to insert new value.
// Has second level recursion, where it will attempt to evict an item if possible, and this will run the findFreeSlot() function again for the potential eviction
// However, the recursion is limited to HOP_RANGE / 2 runs, so, this should still run in O1, unless HOP_RANGE became arbitrarily large.
// Recursion could be avoided all together if other class functions could have been created in the header, but this should still satisfy all requirements, as its not full recursion. 
template <typename KeyType, typename ValueType>
unsigned int HashTable<KeyType, ValueType>::findFreeSlot(std::vector<Bucket>& cTable, unsigned int startIndex, unsigned int& currentHop) {
  
    // If the hope exceeds the HOP_RANGE, the table will need to be rehashed, which means startIndex will also change.
    if(currentHop >= this->HOP_RANGE){
        return this->tableSize; // Return the tableSize as index, which will be out of range as signal to rehash.
    }


    unsigned int index_check = startIndex;
    // currentHop starts at 1
    for(unsigned int i = currentHop - 1; i < this->HOP_RANGE; i++){

        if (index_check >= this->tableSize){
            index_check = 0; // Loop back to the beginning of the table if out of bounds of the hashTable.
        }

        // If bucket no occupied, return available index
        if(!this->hashTable[index_check].occupied){
            return index_check;
        }
        
        index_check++; // increment for the next iteration
    }

    // Here if all values in the HOP_RANGE have been hashed to.
    // Try eviction
    index_check = startIndex;
    // currentHop starts at 1
    unsigned int hopstart = currentHop - 1;
    for(unsigned int i = hopstart; i < this->HOP_RANGE; i++){

        if (index_check >= this->tableSize){
            index_check = 0; // Loop back to the beginning of the table if out of bounds of the hashTable.
        }

        // if value is hashed to index. try to find next value in line
        if( hashTable[index_check].hopInfo & 1){
            unsigned int nexthop = currentHop + 1;
            unsigned int index_to_evict_to = findFreeSlot(cTable, index_check, nexthop);  // increment the hop by 1, so as not to recurse forever

            if (index_to_evict_to < this->tableSize){
                // found a eviction index for bucket
                this->hashTable[index_to_evict_to].key = hashTable[index_check].key;
                this->hashTable[index_to_evict_to].value = hashTable[index_check].value;
                this->hashTable[index_to_evict_to].occupied = true;

                unsigned int evict_hop = get_hop_distance(index_check, index_to_evict_to, this->tableSize);

                unsigned int hopval = (1 << evict_hop);

                // append hop info for the evicted value that got pushed down.
                if( !(hashTable[index_check].hopInfo & hopval )){
                    this->hashTable[index_check].hopInfo |= (1 << evict_hop);
                }

                // remove the last bit, since the index_check no longer holds the hashed value
                if (hashTable[index_check].hopInfo & 1){
                    this->hashTable[index_check].hopInfo &= ~1; 
                }  
               
                this->hashTable[index_check].occupied = false;

                return index_check; // return the index 

            }

        } else {
            // The value to check is not hashed to the same index
            // Find original hashed index:
            unsigned int original_hash_idx = hash_f1(hashTable[index_check].key) % tableSize;

            unsigned int index_to_evict_to;
            // check of original hash index is occupied
            if (!this->hashTable[original_hash_idx].occupied){

                // If not occupied, move to original hash position
                index_to_evict_to = original_hash_idx;

                this->hashTable[index_to_evict_to].key = hashTable[index_check].key;
                this->hashTable[index_to_evict_to].value = hashTable[index_check].value;
                this->hashTable[index_to_evict_to].occupied = true;

                if (! (hashTable[original_hash_idx].hopInfo & 1)){
                    this->hashTable[index_check].hopInfo |= 1 ;  // set the hop info to 1 for original hashed key 
                }  

                unsigned int evict_hop = get_hop_distance(original_hash_idx, index_check, this->tableSize);

                if (hashTable[original_hash_idx].hopInfo & evict_hop){
                    hashTable[original_hash_idx].hopInfo &= ~evict_hop; // remove the hop info of the evicted value
                }

                this->hashTable[index_check].occupied = false;

                // if index_check was successfully moved to its original hash index: 
                return index_check; // return the index 

            } else {
                unsigned int nexthop2 = currentHop + 1;
                index_to_evict_to = findFreeSlot(cTable, original_hash_idx, nexthop2);  // increment the hop by 1, so as not to recurse forever

                if (index_to_evict_to < this->tableSize){
            
                    // found an alternative value to evict to, that is not the original hashed value
                    this->hashTable[index_to_evict_to].key = hashTable[index_check].key;
                    this->hashTable[index_to_evict_to].value = hashTable[index_check].value;
                    this->hashTable[index_to_evict_to].occupied = true;

                    unsigned int evict_hop_old = get_hop_distance(original_hash_idx, index_check, this->tableSize);
                  
                    // Unset the original_hash_idx evict hop for the index_check key
                    if (hashTable[original_hash_idx].hopInfo & evict_hop_old){
                        hashTable[original_hash_idx].hopInfo &= ~evict_hop_old; // remove the hop info of the evicted value
                    }

                    // Set the new hop info 
                    unsigned int evict_hop_new = get_hop_distance(original_hash_idx, index_to_evict_to, this->tableSize);

                    if (! (hashTable[original_hash_idx].hopInfo & evict_hop_new)){
                        hashTable[original_hash_idx].hopInfo |= evict_hop_new; // add new hop info
                    }
    
                    this->hashTable[index_check].occupied = false;

                    return index_check; 


                }
           

            

            }


        }
        
        index_check++; // increment for the next iteration
    }


    return this->tableSize; // failed to find a bucket for new insert, will trigger a rehash
}


// Insert new key-value pair. Does not check if key is already occupied. Will just overwrite it if its the same key. 
// relies on the helper findFreeSlot() function to give it the insert index.
// Runs in O(N) because it checks the loadFactorThreshold with loadFactor() every time, which runs in O(N) because size() run in O(N)
template <typename KeyType, typename ValueType>
void HashTable<KeyType, ValueType>::insert(const KeyType& key, const ValueType& value) {
    
    // checking the loadFactor() take N time. Making inserts now run in N complexity. 
   
    unsigned int hash_idx = hash_f1(key) % tableSize;

    // cout << "inserting key: " << key << " indexed to: " << hash_idx << endl;

    // currentHop starts at 1, and increments until HOP_RANGE
    unsigned int hopstart = 1;
    unsigned int insert_idx = findFreeSlot(this->hashTable, hash_idx, hopstart);
    unsigned int hop = get_hop_distance(hash_idx, insert_idx, this->tableSize);

   // cout << "inserting key: " << key << " insert_idx: " << hash_idx << endl;

    if(insert_idx < this->tableSize){

        this->hashTable[insert_idx].key = key;
        this->hashTable[insert_idx].value = value;
        this->hashTable[insert_idx].occupied = true;
        this->hashTable[hash_idx].hopInfo |= (1 << hop); // update the original hash index hop value

    } else {
        // If insert_idx is above tableSize, then no slot was found.
        rehash(); // Rehash the whole table and upsize 2x
        insert(key, value); // Attempt re-insert
    }

}

// Search. Find is key is occupied, and return the value. 
// Will check the index key hashes to and next HOP_RANGE indexes.
// Could check if original index has a bit flag set for each subsequent index, 
// But this extra check is essentially equivalent to simply checking if the keys are also equal. Thereby making it reduncant.
template <typename KeyType, typename ValueType>
ValueType* HashTable<KeyType, ValueType>::search(const KeyType& key) {

   // cout << "searching key: " << key << endl;
    unsigned int hash_idx = hash_f1(key) % tableSize;
    unsigned int index_check = hash_idx;

    unsigned int hash_index_hopinfo = this->hashTable[index_check].hopInfo; //  redundant to check, when can just check each subsequent key. for small HOP_RANGE
    
   // cout << hash_idx << endl;
    for(unsigned int i = 0; i < this->HOP_RANGE; i++){

        if (index_check >= this->tableSize){
            index_check = 0; // Loop back to the beginning of the table if out of bounds of the hashTable.
        }
       // cout << this->hashTable[index_check].occupied << " key: " << this->hashTable[index_check].key << endl;

        // Could also check for hop info flag, but is just a redundant check when a simple loop also works well.
        if(this->hashTable[index_check].occupied && this->hashTable[index_check].key == key){
            return &this->hashTable[index_check].value;
        }
        
        index_check++; // increment for the next iteration
    }

   // cout << "did not find key: " << key << endl;

    ValueType* result = nullptr;
    return result;
  
}


// Update value for key. Very straight forward, find key, if exists, update its value. 
// If key does not exit, or not occupied (deleted), do nothing
template <typename KeyType, typename ValueType>
void HashTable<KeyType, ValueType>::updateValueForKey(const KeyType& key, ValueType newValue) {
   
   // cout << "updating key: " << key << " to value " << endl;
    unsigned int hash_idx = hash_f1(key) % tableSize;
    unsigned int index_check = hash_idx;
    
    for(unsigned int i = 0; i < this->HOP_RANGE; i++){

        if (index_check >= this->tableSize){
            index_check = 0; // Loop back to the beginning of the table if out of bounds of the hashTable.
        }

        // Could also check for hop info flag, but is just a redundant check when a simple loop also works well.
        if(this->hashTable[index_check].occupied && this->hashTable[index_check].key == key){
            this->hashTable[index_check].value = newValue;
            return;
        }
        
        index_check++; // increment for the next iteration
    }

}

// Remove a key. It is just flagged as not occupied. 
// Any hop info is adjusted. 
// This empty bucket can later be used to evict other keys into, or re-insert as needed.
// HashTable WILL NOT shrink in size if number of removed elements, ex. size() is far below some tableSize. 
// But in a production data structure, the hash table can shrink when size() < tableSize / 4
template <typename KeyType, typename ValueType>
bool HashTable<KeyType, ValueType>::remove(const KeyType& key) {
   

    unsigned int hash_idx = hash_f1(key) % tableSize;
    unsigned int index_check = hash_idx;

   // cout << "removing key: " << key << " indexed to: " << hash_idx << endl;
    
    for(unsigned int i = 0; i < this->HOP_RANGE; i++){

        if (index_check >= this->tableSize){
            index_check = 0; // Loop back to the beginning of the table if out of bounds of the hashTable.
        }

        // Could also check for hop info flag, but is just a redundant check when a simple loop also works well.
        if(this->hashTable[index_check].occupied && this->hashTable[index_check].key == key){
            
            this->hashTable[index_check].occupied = false;

            unsigned int hop_adj = get_hop_distance(hash_idx, index_check, this->tableSize);

            if (hashTable[hash_idx].hopInfo & hop_adj){
                hashTable[hash_idx].hopInfo &= ~hop_adj; // remove the hop info of the evicted value
            }

            return true;
        }
        
        index_check++; // increment for the next iteration
    }

    return false;
}

// Clear. Just sets all the buckets to not occupied, and no hops.
// DOES NOT REDUCE SIZE
template <typename KeyType, typename ValueType>
void HashTable<KeyType, ValueType>::clear() {

    for(unsigned int i = 0; i < this->tableSize; i++){
        this->hashTable[i].occupied = false;
        this->hashTable[i].hopInfo = 0;
    }

}

// Size. Runs in O(n) since we do not keep track of inserts and deletes at run time.
// Iterates for occupied vector hashtable buckets.
template <typename KeyType, typename ValueType>
unsigned int HashTable<KeyType, ValueType>::size() const {
   
    // Just loop over every index and count occupied buckets.
    unsigned int count = 0;
    for (const Bucket bucket : this->hashTable) {
        if (bucket.occupied) { count++; }
    }

    return count;
}


// Load factor. Returns the current size(), which takes O(n) to compute, devided by total hashtable spaces
template <typename KeyType, typename ValueType>
double HashTable<KeyType, ValueType>::loadFactor() const {
    
    return static_cast<double>(size()) / static_cast<double>(tableSize);

}


// Rehash when cannot evict or is above load factor threshold typically.
// Will double te table size exactly, as this is what the tests chekc for. 
// However, it would have been best to double in size and add 1. To keep more primes in totalSize. 
template <typename KeyType, typename ValueType>
void HashTable<KeyType, ValueType>::rehash() {

   // cout << "rehashing" << endl;
   // new hashtable size is twice as big + 1
   // bitshift to double
   this->tableSize = (this->tableSize << 1)+ 1; //can only double in size to pass tests. 

   std::vector<Bucket> oldhashTable = this->hashTable;
   this->hashTable = std::vector<Bucket>(this->tableSize, Bucket());

    // populate new hash table
    for(Bucket b : oldhashTable){
       if(b.occupied){
            insert(b.key, b.value);  // it is theoretically possible that another rehash will be called in the inserts of this rehash.
            b.occupied = false;
       }

    }

}


// Operator []. returns the search value, and will insert value if given = to
template <typename KeyType, typename ValueType>
ValueType& HashTable<KeyType, ValueType>::operator[](const KeyType& key) {
    ValueType* result = search(key);
    if (!result) {
        insert(key, ValueType{});  // insert default
        result = search(key);      // now safe to dereference
    }

    return *result;
}


// used for iterator, will loop over the hashtable vector for occupied buckets.
template <typename KeyType, typename ValueType>
typename HashTable<KeyType, ValueType>::Iterator HashTable<KeyType, ValueType>::begin() {
    auto it = hashTable.begin();
    auto endIt = hashTable.end();

    // Skip to the first occupied bucket
    while (it != endIt && !it->occupied) {
        ++it;
    }

    return Iterator(it, endIt);
}

// ends the iterator with final value.
template <typename KeyType, typename ValueType>
typename HashTable<KeyType, ValueType>::Iterator HashTable<KeyType, ValueType>::end() {
    return Iterator(hashTable.end(), hashTable.end());
}



class RandomizedSet {
public:

    size_t table_it;
    size_t hash_size = 0;
    HashTable<int,int> h;
    RandomizedSet() {
        h = HashTable<int,int>();
        table_it = 0;
    }
    
    bool insert(int val) {

        if(h.search(val)){
            return false;
        }
        h.insert(val,val);
        hash_size++;
        return true;
    }
    
    bool remove(int val) {
        if(h.search(val)){
            h.remove(val);
            hash_size--;

            if(hash_size < h.tableSize / 4){
               
                HashTable<int,int> h2 =  HashTable<int,int>();
                for(unsigned int i = 0; i < this->h.tableSize; i++){
                    if(h.hashTable[i].occupied){
                        h2.insert(h.hashTable[i].value, h.hashTable[i].value);
                    }
                   
                }

                this->h=h2;
                table_it=0;
                
            }

            return true;
        }
        return false;
    }
    

    int random1(){
        while(true){

            if(table_it >= this->h.tableSize){
                table_it=0;
            }
            
            if(h.hashTable[table_it].occupied){
                int val = h.hashTable[table_it].value;
                table_it++;
                return val;

            }

            table_it++;
            
        }
    }

    int random2(){

        std::random_device rd;               // Seed (non-deterministic)
        std::mt19937 gen(rd());              // Mersenne Twister PRNG
        std::uniform_int_distribution<> dist(0, this->h.tableSize-1);  // Range: [10, 50]

        while (true){

            int r = dist(gen);
            
            if(this->h.hashTable[r].occupied){
                return this->h.hashTable[r].value;
            }

        }
       

        
    }


    int getRandom() {

        return random2();

    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */