from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

player_visited_rooms = {}

def players_path(player):
    #declearing the path I am going to return as the traversal_path
    my_path = []
    #adding starting room to my visited table so I can look up the id of the room and know what rooms have been visited and which are connected
    player_visited_rooms[player.current_room.id] = {}
    #continously looping until my player_visited_rooms has a length equal to the number of rooms in the world class
    while len(player_visited_rooms) < len(world.rooms):
        #retrieving the path, which is a list of rooms to the nearest unexplored room
        for room in find_path_for_shortest_unexplored_room_bfs(player.current_room):
            #getting the direction of the returned room from visited rooms based on current room/desired room, which will return my direction
            direction_to_travel = player_visited_rooms[player.current_room.id][room.id]
            player.travel(direction_to_travel)
            #adding those directions to the path array 
            my_path += [direction_to_travel]
            #checking to see if the current room is in the player_visited_rooms and if not, then adding it to visited_rooms
            if player.current_room.id not in player_visited_rooms:
                player_visited_rooms[player.current_room.id] = {}  
    return my_path

def best_route(room, direction, path, my_queue, visited):
    for exit in room.get_exits():
        if exit is direction:
            #checking to see if current room is already in my visited, so I dont revisit a room
            if room.get_room_in_direction(exit).id not in visited and room.get_room_in_direction(exit).id not in player_visited_rooms:     
                #getting next room I am going to visit
                next_room = room.get_room_in_direction(exit)
                #setting the room id to the direction of the current rooms exit point, so I know which room is connected in which direction
                player_visited_rooms[room.id][next_room.id] = exit
                new_path = path + [next_room]
                return my_queue.enqueue(new_path)
        
def find_path_for_shortest_unexplored_room_bfs(starting_room):
    my_queue = Queue()
    #added my current room in an array, which will serve as a path to use as directions to the next closest unvisited room
    my_queue.enqueue([starting_room])
    visited = set()

    while my_queue.size() > 0:

        current_room_path = my_queue.dequeue()
        #getting the current room to leverage its methods and attributes
        current_room = current_room_path[-1]
        #getting the current rooms id of the latest queued room to add into my visited set
        room_number = current_room.id

        #checking see if the current room is in player_visited_rooms and if it is, then just adding it to my queue because its already been explored
        if room_number in player_visited_rooms:
            #checking to see if room has been visited in my current path
            if room_number not in visited:
                visited.add(room_number)
                #checking the paths in this order because this is the most efficient combination for checking exits
                if best_route(current_room, "s", current_room_path, my_queue, visited) != None:
                    best_route(current_room, "s", current_room_path, my_queue, visited)
                elif best_route(current_room, "w", current_room_path, my_queue, visited) != None:
                    best_route(current_room, "w", current_room_path, my_queue, visited)
                elif best_route(current_room, "n", current_room_path, my_queue, visited) != None:
                    best_route(current_room, "n", current_room_path, my_queue, visited)
                elif best_route(current_room, "e", current_room_path, my_queue, visited) != None:
                    best_route(current_room, "e", current_room_path, my_queue, visited)
                else:
                    #back up incase first for senarios fail 
                    for exit in current_room.get_exits():
                        if current_room.get_room_in_direction(exit).id not in visited:
                            #getting next room I am going to visit
                            next_room = current_room.get_room_in_direction(exit)
                            #setting the room id to the direction of the current rooms exit point, so I know which room is connected in which direction
                            player_visited_rooms[current_room.id][next_room.id] = exit
                            new_path = current_room_path + [next_room]
                            my_queue.enqueue(new_path)            
        else:
            #returning the path to the desired unvisited room, but leaving out the current room
            return current_room_path[1:]

traversal_path = players_path(player)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")