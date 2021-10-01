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
        tickets.sort(key=lambda x: x[1], reverse=True)
        nodes = {}
        for i, j in tickets:
            if i not in nodes:
                nodes[i] = []
            nodes[i].append(j)
        r = ["JFK",]
        while True:
            temp = r[-1]
            if temp not in nodes or not nodes[temp]:
                break
            r.append(nodes[temp][0])
            nodes[temp] = nodes[temp][1:]
        return r


if __name__ == "__main__":
    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    sol = Solution()
    r = sol.findItinerary(tickets)
    print(r)
