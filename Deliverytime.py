class DeliveryTime(object):

    def __init__(self) -> None:

        self.adj_lst = {"Hu Dukaan": [("Cafeteria", 2), ("Dhaaba", 2), ("East Street", 3)],
                        "East Street": [("Central Street 2", 4), ("Hu Dukaan", 3)],
                        "Cafeteria": [("Central Lower Ground", 2), ("Gym", 4), ("Swimming Pool", 4), ("Amphitheater", 2), ("Hu Dukaan", 2), ("Central Street 2", 3)],
                        "Central Lower Ground": [("Circuits and Electronic Lab 1", 3), ("Music Room", 2), ("Library", 4), ("Cafeteria", 2)],
                        "Circuits and Electronic Lab 1": [("Music Room", 2), ("Central Street 1", 3), ("Central Lower Ground", 3)],
                        "Music Room": [("Linux And Networking Lab", 2), ("Central Lower Ground", 2), ("Circuits and Electronic Lab 1", 2)],
                        "Linux And Networking Lab": [("Visualization And Graphics Lab", 2), ("Music Room", 2)],
                        "Visualization And Graphics Lab": [("Linux And Networking Lab", 2)],
                        "Swimming Pool": [("Cafeteria", 4)],
                        "Gym": [("Cafeteria", 4)],
                        "Dhaaba": [("Zen Garden", 3), ("Multipurpose Sports Courts 1", 3), ("Hu Dukaan", 2)],
                        "Zen Garden": [("Multipurpose Sports Courts 1", 2), ("Dhaaba", 3)],
                        "Central Street 1": [("Circuits and Electronic Lab 1", 3), ("Wellness Courtyard", 2), ("Office Of Student Life", 2), ("Reception", 3), ("Library", 3), ("Central Street 2", 2)],
                        "Wellness Courtyard": [("Central Street 1", 2), ("Office Of Student Life", 1)],
                        "Office Of Student Life": [("Central Street 1", 2), ("Wellness Courtyard", 1)],
                        "Central Street 2": [("Earth Courtyard", 3), ("Student Lounge", 4), ("Central Street 1", 2), ("Soorty Hall", 3), ("East Street", 4), ("East Zone", 2), ("Cafeteria", 3)],
                        "Earth Courtyard": [("Central Street 2", 3), ("Learn Courtyard", 2), ("Arif Habib Classroom", 1), ("Air Courtyard", 1), ("Water Courtyard", 1)],
                        "Air Courtyard": [("Earth Courtyard", 1), ("Arif Habib Classroom", 2), ("Water Courtyard", 1)],
                        "Water Courtyard": [("Earth Courtyard", 1), ("Fire Courtyard", 1), ("Air Courtyard", 1)],
                        "Fire Courtyard": [("Water Courtyard", 1), ("Chemistry Lab", 1), ("Digital Systems and Instrumentation Lab", 1), ("Student Lounge", 4)],
                        "Chemistry Lab": [("Fire Courtyard", 1), ("Digital Systems and Instrumentation Lab", 1)],
                        "Digital Systems and Instrumentation Lab": [("Fire Courtyard", 1), ("Chemistry Lab", 1)],
                        "Arif Habib Classroom": [("Earth Courtyard", 1), ("Air Courtyard", 2)],
                        "Learn Courtyard": [("Earth Courtyard", 2)],
                        "Student Lounge": [("Amphitheater", 2), ("Central Street 2", 4), ("Multipurpose Sports Courts 1", 3), ("Soorty Hall", 2), ("Fire Courtyard", 4)],
                        "Multipurpose Sports Courts 1": [("Student Lounge", 2), ("Zen Garden", 2), ("Dhaaba", 3)],
                        "Amphitheater": [("Student Lounge", 2), ("Engineering Workshop", 2), ("Cafeteria", 2)],
                        "Engineering Workshop": [("Amphitheater", 2)],
                        "Soorty Hall": [("Student Lounge", 2), ("Central Street 2", 3), ],
                        "Library": [("Central Lower Ground", 3), ("Central Street 1", 3), ("Reception", 1)],
                        "Reception": [("Central Street 1", 3), ("Student Center", 1), ("Library", 1), ("Elevator", 1)],
                        "Student Center": [("Reception", 1), ("Elevator", 1)],
                        "Elevator": [("Student Center", 1), ("Reception", 1), ("West Zone 1", 3), ("Auditorium Hall", 3), ("Playground", 4), ("Prayer Area", 5)],
                        "East Zone": [("West Zone 1", 3), ("Tariq Rafi Lecture Theater", 2), ("Film Studio", 4), ("West Zone 2", 2), ("Central Street 2", 2)],
                        "Tariq Rafi Lecture Theater": [("Film Studio", 2), ("East Zone", 4), ("Mehfil", 4)],
                        "Film Studio": [("Tariq Rafi Lecture Theater", 2), ("East Zone", 4)],
                        "Mehfil": [("Tariq Rafi Lecture Theater", 4)],
                        "West Zone 1": [("East Zone", 3), ("Faulty Pod", 4), ("Playground", 2), ("West Zone 2", 2), ("Elevator", 3)],
                        "West Zone 2": [("East Zone", 2), ("West Zone 1", 2), ("Baithak", 3), ("Amin Issa Tai Classroom", 3), ("Design Studio", 3)],
                        "Amin Issa Tai Classroom": [("Design Studio", 1), ("West Zone 2", 3), ("Baithak", 2)],
                        "Design Studio": [("West Zone 2", 3), ("Amin Issa Tai Classroom", 1)],
                        "Baithak": [("Amin Issa Tai Classroom", 2), ("West Zone 2", 3)],
                        "Auditorium Hall": [("Elevator", 3)],
                        "Playground": [("Elevator", 4), ("West Zone 1", 2)],
                        "Faulty Pod": [("West Zone 1", 4)],
                        "Prayer Area": [("Elevator", 5), ("Faculty Cafeteria", 2), ("Day Care", 1)],
                        "Faculty Cafeteria": [("Prayer Area", 2)],
                        "Day Care": [("Prayer Area", 1)]}

    def place(self, previous_node, lst):
        for i in range(len(lst)):
            if previous_node[1] == lst[i][1]:
                x = i
        return x

    def addnodes(self):
        node = []
        for i in self.adj_lst:
            node.append(i)
        return node

    def Initilize(self, lst, start):
        for i in range(len(lst)):
            if lst[i][1] == start:
                lst[i][0] = start
                lst[i][2] = 0
        return lst

    def minimumdistance(self, lst, visited_node):
        shortest_time_get = float('inf')
        pair_lst = []

        for i in range(len(lst)):
            place = lst[i][1]
            time = lst[i][2]
        # shortest distance not in visted_node.
            if place not in visited_node and time < shortest_time_get:
                shortest_time_get = time
                pair_lst = lst[i]
        return pair_lst

    def weight(self, previous_node, s):
        first = previous_node[1]
        weigh = 0
        u = self.adj_lst[first]
        for i in range(len(u)):
            if u[i][0] == s[0]:
                weigh = u[i][1]

        return weigh

    def getneighbours(self, m, visited_node):
        # m is the node!
        lst = []
        for i in range(len(self.adj_lst[m[1]])):
            # Append the entire neighbour ('gym', 3) to the list if the location has not yet been visited node.
            if self.adj_lst[m[1]][i][0] not in visited_node:
                # tuple----> ('Gym', 3) addition.
                lst.append(self.adj_lst[m[1]][i])
        return lst

    def getShortestPath(self, start, Des):  # Dijkstra
        lst = []

    # Getting a list of nodes in a graph/Map starts with then appending nodes to a list.
        nodes = self.addnodes()

# Nodes other than the starting node are initialised to infinity.
        for i in nodes:
            l = ['', i,  float('inf')]
            lst.append(l)

        lst = self.Initilize(lst, start)

# Right now, the queue contains all nodes with inf time.
        visited_node = []
        q = nodes
        while len(q) != 0:
            # obtaining the pair with the shortest distance
            m = self.minimumdistance(lst, visited_node)
        # getting tuple of neighbours
            node = self.getneighbours(m, visited_node)
        # adding the visited node place/node to the visited node list
            visited_node.append(m[1])
        # After extraction, remove it from the queue.
            q.remove(m[1])

            previous_node = m
        # Starting with the neighbours in lst, update if less weight is detected.

            x = self.place(previous_node, lst)

            while len(node) != 0:
                s = node[0]
                popping = node.pop(0)

                for n in range(len(lst)):
                    if s[0] == lst[n][1]:
                        r = n  # getting the indexes of neheighbours

                weight_n = lst[x][2] + self.weight(previous_node, s)

            # we update the weight if new weight that is path is found in the list.
                if lst[r][2] > weight_n:
                    # node update.
                    lst[r][2] = weight_n
                    lst[r][0] = previous_node[1]

    # put all edges time in lst.
# Now we work on getting the smallest/shortest path from destination to cafeteria/restaurant.
        lst_it = []
        for i in range(len(lst)):

            places = lst[i][1]
            times = lst[i][0]
            if places == Des and times != start:
                lst_it.append(lst[i])

                while lst[i][0] != start:

                    for j in range(len(lst)):
                        # comparsions from the values.
                        if lst[j][1] == lst[i][0]:
                            if lst[j][0] != start:
                                lst_it.append(lst[j])
                                lst[i] = lst[j]
                            else:
                                lst.append(lst[j])
                                path = lst_it[::-1]
                                return path
# for getting the time of directly connected nodes from the cafetreia.
            elif lst[i][1] == Des and lst[i][0] == start:
                return [lst[i]]
        path = lst_it[::-1]

        return path

    def minDeliveryTime(self, area):
        result = (self.getShortestPath("Cafeteria", area))
        print(result)  # the path
        minutes = 0
        for i in result:
            minutes = minutes+i[2]
        return(minutes)
