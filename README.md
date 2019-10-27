Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
 
Question B
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

Question C
At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:
 
    1 - Simplicity. Integration needs to be dead simple.
    2 - Resilient to network failures or crashes.
    3 - Near real time replication of data across Geolocation. Writes need to be in real time.
    4 - Data consistency across regions
    5 - Locality of reference, data should almost always be available from the closest region
    6 - Flexible Schema

The solution presented implements an LRU cache, with its maximum capacity being determined by the number of items being cached. The items are saved in an ordered dictionary, so that the searching and deleting time will be O(1) and the elements will be ordered as they have been cached, so it is also O(1) to pop the least recently used item when the cache is full.
Whenever the get method is called, the program verifies if the item's time limit has expired, removing it from the cache if so. Otherwise, the item will be moved to the beggining of the ordered dictionary. It is worth noting that the time stored for the item will not change, since its value has not been updated. This will ensure that a frequently looked item will eventually expire.
The solution is generic, and the items being stored could be of any type.

The missing features are the ones involving the geo distribution, since the solution was implemented as a simple class to be called elsewhere. It would be appropriate to implement a RestFul API to deal with data replication and closest region availability.