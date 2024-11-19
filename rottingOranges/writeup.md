# Rotting Oranges

This problem asks you find the number of time steps required for all fresh oranges to become rotten.
A fresh orange becomes rotten if it is next to cardinally adjacent to a rotten orange.
If not all oranges become rotten, i.e., isolated, return -1

This can be solved using a multi-start BFS.
At each time step, we perform a BFS on all oranges in our queue.
Our queue consists of all rotten oranges not yet considered.

To determine if all oranges have become rotten, we first count the number of fresh oranges.
During this process, we can also add all existing rotten oranges to our queue.
