// https://leetcode.com/problems/number-of-islands/

#include <vector>
#include <iostream>
#include <unordered_set> 

using namespace std;

class Solution {

    struct coord {
        int x;
        int y;

        coord(int x, int y){
            this->x = x;
            this->y = y;
        }

        bool operator==(const coord& other) const {
            return x == other.x && y == other.y;
        }
    };

    struct coord_hash {
        std::size_t operator()(const coord& c) const {
            auto h1 = std::hash<int>{}(c.x);
            auto h2 = std::hash<int>{}(c.y);
            return h1 ^ (h2 << 1); // Combine hashes
        }
    };

public:

    char landval = '1';

    bool is_land(vector<vector<char>>& grid, int x, int y){

        if( y < 0 || x < 0){
            return false;
        }
    
        if( y >= grid.size() ){
            return false;
        }

        vector<char> yvec = grid[y];

        if( x >= yvec.size() ){
            return false;
        }

        char island = yvec[x];

        if (island == landval){
            return true;
        } else {
            return false;
        }

    }


    vector<coord> find_land_nearby(vector<vector<char>>& grid, coord& c, unordered_set<coord, coord_hash>& visited_coords){

        vector<coord> nearland;
        //cout << "calling find_land_nearby()" << endl;

        if(is_land(grid, c.x, c.y-1)){

            coord near1 = coord(c.x, c.y-1);
            if(!visited_coords.count(near1)){
                visited_coords.insert(near1);
                nearland.push_back(near1);

                vector<coord> other_near = find_land_nearby(grid, near1, visited_coords);
                for(coord c1 : other_near){
                    nearland.push_back(c1);
                }

            }

            
            
        }

        if(is_land(grid, c.x, c.y+1)){

            coord near2 =  coord(c.x, c.y+1);

            if(!visited_coords.count(near2)){
                visited_coords.insert(near2);
                nearland.push_back(near2);

                vector<coord> other_near2 = find_land_nearby(grid, near2, visited_coords);
                for(coord c1 : other_near2){
                    nearland.push_back(c1);
                }
            }

           
        }

        if(is_land(grid, c.x-1, c.y)){

            coord near3 =  coord(c.x-1,c.y);

            if(!visited_coords.count(near3)){
                visited_coords.insert(near3);
                nearland.push_back(near3);

                vector<coord> other_near2 = find_land_nearby(grid, near3, visited_coords);
                for(coord c1 : other_near2){
                    nearland.push_back(c1);
                }

            }

          
        }

        if(is_land(grid, c.x+1, c.y)){
            coord near4 =  coord(c.x+1, c.y);
             if(!visited_coords.count(near4)){
                visited_coords.insert(near4);
                nearland.push_back(near4);
                vector<coord> other_near2 = find_land_nearby(grid, near4, visited_coords);
                for(coord c1 : other_near2){
                    nearland.push_back(c1);
                }
            }

           
        }

        return nearland;
    }


    unordered_set<coord, coord_hash> visited_coords;

    int numIslands(vector<vector<char>>& grid) {
        
        vector<vector<coord>> islands;

        for(int y = 0; y < grid.size(); y++){

            vector<char> yvec = grid[y];
            for(int x = 0; x < yvec.size(); x++){

                coord new_coord = coord(x,y);

                // if not visited coord...
                if (!visited_coords.count(new_coord) ){

                    // cout << "loop new coord: " << x << ", " << y << endl;
                    // cout << "already visited coords: ";
                    // for(coord n : visited_coords){
                    //     cout << " { " << n.x << "," << n.y << "} ";
                    // }

                    // cout << endl;

                    visited_coords.insert(new_coord);

                    if (is_land(grid, x, y)){

                        vector<coord> new_island;
                        new_island.push_back(new_coord);
                        
                        vector<coord> nearby_land = find_land_nearby(grid, new_coord, visited_coords);
                        // cout << "nearby land: ";
                        // for(coord n : nearby_land){
                        //     cout << " { " << n.x << "," << n.y << "} ";
                        // }

                        // cout << endl;

                        islands.push_back(new_island);
                    }
                }


            }

        }


        return islands.size();
    }

};