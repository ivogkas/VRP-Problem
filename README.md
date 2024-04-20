# VRP-Problems

Assignment for the course «Optimization Methods in Management Science» (2021). 
The purpose of the assignment is to solve a vehicle routing problem (using Python), which relates to the transportation of materials to various destinations. 
The design of the routes should minimize the completion time (hours) of delivering the products to the destinations. 
Initially, a solution was generated through a greedy algorithm. Then, the solution was optimized using local search algorithms.

The scenario is as follows:   
*  200 geographical destinations
*  Each destination has different supply needs.
*  For the transportation of supplies, 25 homogeneous trucks with a maximum load of 3 tons are used.
*  Each truck starts its route from the same central warehouse and sequentially visits some of the 200 points.
*  All trucks start simultaneously.
*  Each location is served by only one visit from a single vehicle. When a vehicle visits a service point, it delivers all the required supplies to it.
*  The vehicles travel at 35 km/hr.
*  Each service point belongs to a category depending on its needs: Category 1 (supplies unloading in 5 minutes), Category 2 (supplies unloading in 15 minutes), Category 3 (supplies unloading in 25 minutes).

Τhe solution includes the total time and the sets of locations that correspond to each vehicle.
   
Using the greedy algorithm, the total time was approximately 8 hours. The solution was imporved by using 1-0 and 1-1 exchanges among the locations in the vehicles' routes.. The total time was reduced to 5.8 hours.  
