from collections import deque

print("[+] Breadth first search running")

graph = dict()

graph["me"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    """
    :param name:
    :return:

    Checks if the persons name ends with m , if they are then they are the seller!
    """
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        print("Searching:\n\t", person)
        print("Current Queue\n\t", search_queue)
        print("Searched\n\t", searched, "\n")

        if person not in searched:
            if person_is_seller(person):
                print("We got a seller: ", person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False


print(search("me"))