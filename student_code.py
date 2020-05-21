
import math
from queue import PriorityQueue   

def Euclidean(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

def generatePath(prev, start, goal):
    curr = goal
    path = [curr]
    while curr != start:
        curr = prev[curr]
        path.append(curr)
    path.reverse()
    return path

def shortest_path(M,start,goal):
    intersections = M.intersections
    roads = M.roads
    pathQ = PriorityQueue()
    pathQ.put(start,0)
    
    prev = {start: None}
    score = {start: 0}
    updatescore = 0
    while not pathQ.empty():
        current = pathQ.get()
        
        if current == goal:
            generatePath(prev,start,goal)
        
        for node in roads[current]:
            updatescore = score[current] + Euclidean(intersections[current],intersections[node])
            
            if node not in score or updatescore < score[node]:
                score[node] = updatescore
                totalscore = updatescore + Euclidean(intersections[current],intersections[node])
                pathQ.put(node,totalscore)
                prev[node] = current
                
    print("shortest path called")
    return generatePath(prev,start,goal)
    

        
    
    
