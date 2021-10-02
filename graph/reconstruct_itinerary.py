"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports
 of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are
multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single
string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
"""


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort(key=lambda x: x[1])
        nodes = {}
        for i, j in tickets:
            if i not in nodes:
                nodes[i] = []
            nodes[i].append(j)
        r = ['JFK',]
        self.dfs(nodes, len(tickets), r)

    def dfs(self, nodes, size, it):
        if size == 0:
            return True
        curr = it[-1]
        edges = nodes[curr]
        for e in edges:
            nodes[curr] = edges[:].remove(e)
            it.append(e)
            if self.dfs(nodes, size-1, it):
                return True
            nodes[curr] = edges
        return False





if __name__ == "__main__":
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    sol = Solution()
    r = sol.findItinerary(tickets)
    print(r)
