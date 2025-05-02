// https://leetcode.com/problems/insert-delete-getrandom-o1/description/

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
    size_t current_size = 0;
    vector<Unit*> table;
    size_t max_next_spaces = 3;

    void initialize(size_t size){

        // generate a table of null pointers (empty values initially.)
        this->table = vector<Unit*>(size, nullptr);

    }

    void resize_set(bool up){

        cout << "resizing table from: " << this->size << " current count: " << this->current_size << endl;
        size_t old_size = this->size;
        vector<Unit*> old_table = table;

        size_t new_size;
        if (up){
            new_size = (old_size << 1) + 1; // set size to be 2^n-1 in size, as 2^n distributes too nicely for knuth's hash function
        } else if (this->size > 7) {
            new_size = (old_size >> 1);
        } else {
            return; // will not resize below size 7
        }
        
        this->size = new_size;

        cout << "new size: " << new_size << endl;

        if (new_size == old_size){
            throw std::runtime_error("size limit reached in RandomizedSet");
        }

        vector<Unit*> newtable = vector<Unit*>(new_size, nullptr);
        
        this->table = newtable;
        this->current_size=0;

        for(size_t i=0; i < old_size; i++){
            
            if (old_table[i] != nullptr){
                
                this->insert( old_table[i]->val ); // insert new value to be re-indexed as per new sizing

                delete  old_table[i];
                old_table[i] = nullptr; // reset all pointers to null in the old table.
            }

            
        }

    }


    void delete_and_check_idx(size_t idx){

        Unit* u = this->table[idx];
        if (u == nullptr) {
            return;
        }

        if(u->flag == 0){
                
            delete this->table[idx];
            this->table[idx] = nullptr;
            this->current_size--;
            
        } else {
            size_t nextidx = idx;
            vector<Unit*> flagged_units;

            // collect the dangling flag values

            for (size_t i = 0; i < this->max_next_spaces; i++){
                nextidx++;

                if (nextidx >= this->size){
                    nextidx = 0; // loop around to start.
                }

                // check if flag is set. 
                if (u->flag & ( 1<<i )){  
                    Unit* next_u = this->table[nextidx];
                    if(next_u != nullptr){
                        flagged_units.push_back(next_u);
                        this->table[nextidx] = nullptr;  // set the flagged indexes to null.

                    }
                }
               
            }

            
            delete this->table[idx];
            this->table[idx] = nullptr;
            this->current_size--;

            // re-insert the flagged dangling values:
            for(int i =0; i < flagged_units.size(); i++){
                insert(flagged_units[i]->val);
                delete flagged_units[i];
                flagged_units[i] = nullptr;
            }
        }

        if(current_size < this->size / 4){
            resize_set(false);
        }

    }
   


public:
    RandomizedSet() {
        this->size = 7;
        initialize(size);

    }
    
    bool insert(int val) {

        if(this->hasval(val)){
            return false;
        }
        
        Unit unit = Unit(val);
        size_t val_idx = unit.hash % size;

        //cout << val << " hashed to: " << unit.hash << " at index: " <<  val_idx << endl;

        // check if empty:
        Unit* u = this->table[val_idx];
        if (u == nullptr) {
            this->table[val_idx] = new Unit(val);
            cout << "inserting new value " << val << " at index: " << val_idx << endl;
            this->current_size++;
            return true;
        } else {
            // unit value exists, but indexes collide:
            std::cout << "index collision for: " << val << std::endl;

            // check if next 3 spaces are available:
            size_t nextidx = val_idx;
            for(int j=0; j < this->max_next_spaces; j++ ){
                
                nextidx++;
                if (nextidx >= this->size){
                    nextidx = 0; // loop around to start.
                }

                Unit* u_next = this->table[nextidx];
                if(u_next == nullptr){
                    table[nextidx] = new Unit(val);
                    cout << "inserting new value " << val << " at index: " << nextidx << endl;

                    u->flag |= (1 << j); // set the bit flag for the value that got filled.
                    
                    this->current_size++;
                    return true;
                }

            }

            resize_set(true);
            insert(val);
        }


        return false;
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
            for (size_t i = 0; i < this->max_next_spaces; i++){
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

        Unit unit = Unit(val);
        size_t val_idx = unit.hash % size;

        Unit* u = this->table[val_idx];
        if (u == nullptr) {
            return false;
        }

        if (u->val == val){
            delete_and_check_idx(val_idx);
            cout << "removing value " << val << " at index: " << val_idx << endl;
            return true;
        }

        if(u->flag == 0){
            return false;
        } else {
            size_t nextidx = val_idx;
            for (size_t i = 0; i < this->max_next_spaces; i++){
                nextidx++;

                if (nextidx >= this->size){
                    nextidx = 0; // loop around to start.
                }

                // check if flag is set. sort of meaningless, because can just check the next index anyways.
                if (u->flag & ( 1<<i )){  
                    Unit* next_u = this->table[nextidx];
                    if(next_u != nullptr){
                        if(next_u->val==val){
                            cout << "removing value " << val << " at index: " << nextidx << endl;
                            delete_and_check_idx(nextidx);
                            return true;
                        }
                    }
                }
               
            }

        }

        return false;

    }

   
    
    int getRandom() {

        if(this->current_size == 0){
            return 0;
        }

        std::random_device rd;                         // Seed
        std::mt19937 gen(rd());                        // Mersenne Twister engine
        std::uniform_int_distribution<> dist(0, this->size - 1);  // Range: [1, 100]

        int random_number = dist(gen);  

        

        if(this->table[random_number] != nullptr){
            
            cout << "returning random number " << this->table[random_number]->val << " at index: " << random_number << endl;
            return this->table[random_number]->val;
        } else {
            cout << "did not find random number at index: " << random_number << endl;
            return getRandom();
        }

    }

    int getSize() {
        return this->current_size;
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
        std::cout << "size: " << rs.getSize() << std::endl;
    }

     for(int i=0;i<vec.size();i++){
        rs.remove(vec[vec.size()-i-1]);
        std::cout << "size: " << rs.getSize() << std::endl;
    }

    std::cout << "size: " << rs.getSize() << std::endl;

    for(int i=0;i<vec.size();i++){
        std::cout <<  rs.hasval(vec[i]) << std::endl;
    }

    std::cout << "Random Number" << std::endl;
    for(int i=0; i<10; i++){
        std::cout << rs.getRandom() << std::endl;
    }

    std::cout << "All Done" << std::endl;


    return 0;
}


//  g++ -std=c++11 randomset.cpp -o randomset && ./randomset

