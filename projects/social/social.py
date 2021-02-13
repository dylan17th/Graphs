import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(num_users):
            self.add_user(User(i))

        friendship_array = []

        for user in self.users:
            for user2 in self.users:
                if user < user2:
                    friendship_array.append((user, user2))

        number_of_made_friends = 0
        while number_of_made_friends < (num_users * 2):
            random.shuffle(friendship_array)
            friendship = friendship_array[-1]
            friendship_array.pop()
            number_of_made_friends += 1
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        visited = {}
        my_queue = Queue()
        my_queue.enqueue([user_id])

        while my_queue.size() > 0:

            node = my_queue.dequeue()
            new_path = node[-1]

            if new_path not in visited:
                visited[new_path] = node
                for friend in self.friendships[new_path]:
                    path = node + [friend]
                    my_queue.enqueue(path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
