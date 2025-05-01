#include <iostream>
#include <vector>
#include <ctime>    // for time
#include <functional>
#include <random>

using namespace std;

class Unit {
    private:

        // a hash function that maps uint->uint, looks kinda random
        unsigned int knuth_hash(int x) {
            return static_cast<uint32_t>(x) * 2654435761u;  // Knuth's multiplicative constant
        }

        unsigned int hashf(int val){
            return knuth_hash(val);
        }

    public:
        int val;
        unsigned int flag;
        unsigned int hash;

        Unit(int val){
            this->val = val;
            this->flag = 0;
            this->hash = hashf(val);
        }

};

class RandomizedSet {

private:
    size_t size;
    vector<Unit*> table;

    void initialize(size_t size){

        // generate a table of null pointers (empty values initially.)
        this->table = vector<Unit*>(size, nullptr);

    }

    void resize_set(){

        cout << "resizing table" << endl;
        size_t old_size = this->size;
        vector<Unit*> old_table = table;

        size_t new_size = (old_size << 1) + 1;
        this->size = new_size;

        cout << "new size: " << new_size << endl;

        if (new_size == old_size){
            throw std::runtime_error("size limit reached in RandomizedSet");
        }

        vector<Unit*> newtable = vector<Unit*>(new_size, nullptr);
        
        this->table = newtable;

        for(size_t i=0; i < old_size; i++){
            
            if (old_table[i] != nullptr){
                
                this->insert( old_table[i]->val ); // insert new value to be re-indexed as per new sizing

                delete  old_table[i];
                old_table[i] = nullptr; // reset all pointers to null in the old table.
            }

            
        }

    }

   


public:
    RandomizedSet() {
        this->size = 7;
        initialize(size);

    }
    
    bool insert(int val) {
        
        Unit unit = Unit(val);
        size_t val_idx = unit.hash % size;

        cout << val << " hashed to: " << unit.hash << " at index: " <<  val_idx << endl;

        // check if empty:
        Unit* u = this->table[val_idx];
        if (u == nullptr) {
            this->table[val_idx] = new Unit(val);
            cout << "inserting new value at index: " << val_idx << endl;
            return true;
        } else if (u->val == val){
            cout << u->val << " value already exists " << val << endl;
            return false;
        } else {
            // unit value exists, but indexes collide:
            std::cout << "index collision for: " << val << std::endl;

            // check if next 3 spaces are available:
            size_t nextidx = val_idx;
            for(int j=0; j<3; j++ ){
                
                nextidx++;
                if (nextidx >= this->size){
                    nextidx = 0; // loop around to start.
                }

                Unit* u_next = this->table[nextidx];
                if(u_next == nullptr){
                    table[nextidx] = new Unit(val);

                    u->flag |= (1 << j); // set the bit flag for the value that got filled.
                    return true;
                }

            }

            resize_set();
            insert(val);
        }

        return true;
    }

    bool hasval(int val){

        Unit unit = Unit(val);
        size_t val_idx = unit.hash % size;

        Unit* u = this->table[val_idx];
        if (u == nullptr) {
            return false;
        }

        if (u->val == val){
            return true;
        }

        if(u->flag == 0){
            return false;
        } else {
            size_t nextidx = val_idx;
            for (size_t i = 0; i < 3; i++){
                nextidx++;

                if (nextidx >= this->size){
                    nextidx = 0; // loop around to start.
                }

                // check if flag is set. sort of meaningless, because can just check the next index anyways.
                if (u->flag & ( 1<<i )){  
                    Unit* next_u = this->table[nextidx];
                    if(next_u != nullptr){
                        if(next_u->val==val){
                            return true;
                        }
                    }
                }
               
            }

        }

        return false;
    }
    
    bool remove(int val) {
        

        return true;
    }
    
    int getRandom() {
        
        return 0;
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */



int main() {
    std::cout << "Starting Script" << std::endl;

    std::vector<int> vec1 = {1,1,2,3,4,5,6,7,8,9,10};
    std::vector<int> vec2 = {2,4,8,16,32,64,128,256,512,1024,2048,2049,2050,2051};

    std::vector<int> vec = vec2;

    RandomizedSet rs = RandomizedSet();
    
    for(int i=0;i<vec.size();i++){
        rs.insert(vec[i]);
    }

    for(int i=0;i<vec.size();i++){
        std::cout <<  rs.hasval(vec[i]) << std::endl;
    }

    std::cout << "All Done" << std::endl;


    return 0;
}


//  g++ -std=c++11 randomset.cpp -o randomset && ./randomset