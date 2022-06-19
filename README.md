# Influence-Maximization
# Comparison between GREEDY and CELF
# Input-
    g[node=236,edges=2478],
    k=[2,4,6,8,10],
    p=0.5,
    mc=15
# Output-
    PS E:\COMPUTER\Projects\Influence-Maximization> python main.py
    Enter the number of iterations : 5
    Enter the values of k seperated by space : 
    2 4 6 8 10
    Enter the value of mc : 15

    Please wait for the next k output...

    Calculating...

    For the value of k =  2

    GREEDY

    Seed Nodes =  [135, 230]
    Spread of each seed =  [200.13333333333333, 201.6]    
    Time Taken =  [22.447924375534058, 52.67872858047485] 

    CELF

    Seed Nodes =  [135, 230]
    Spread of each seed =  [200.13333333333333, 201.6]    
    Time Taken =  [22.485652446746826, 48.719231605529785]
    Lookups =  [236, 205]

    Please wait for the next k output...

    Calculating...

    For the value of k =  4

    GREEDY

    Seed Nodes =  [135, 230, 229, 216]
    Spread of each seed =  [200.13333333333333, 201.6, 203.0, 204.13333333333333]
    Time Taken =  [22.630513191223145, 52.29546403884888, 82.11829686164856, 111.87852263450623]

    CELF

    Seed Nodes =  [135, 230, 229, 216]
    Spread of each seed =  [200.13333333333333, 201.6, 203.0, 204.13333333333333]
    Time Taken =  [22.3965847492218, 48.56204557418823, 48.68704438209534, 48.96828603744507]
    Lookups =  [236, 205, 1, 2]

    Please wait for the next k output...

    Calculating...

    For the value of k =  6

    GREEDY

    Seed Nodes =  [135, 230, 229, 216, 221, 0]
    Spread of each seed =  [200.13333333333333, 201.6, 203.0, 204.13333333333333, 205.2, 206.2]
    Time Taken =  [23.20569396018982, 53.86038613319397, 83.7484483718872, 113.60192728042603, 144.48971605300903, 174.40116024017334]

    CELF

    Seed Nodes =  [135, 230, 229, 216, 221, 190]
    Spread of each seed =  [200.13333333333333, 201.6, 203.0, 204.13333333333333, 205.2, 206.2]
    Time Taken =  [22.460404872894287, 49.42003607749939, 49.5450325012207, 49.81528282165527, 50.06303572654724, 50.188032150268555]
    Lookups =  [236, 205, 1, 2, 2, 1]

    Please wait for the next k output...

    Calculating...

    For the value of k =  8

    GREEDY

    Seed Nodes =  [135, 230, 229, 216, 221, 0, 190, 193]
    Spread of each seed =  [200.13333333333333, 201.6, 203.0, 204.13333333333333, 205.2, 206.2, 207.2, 208.2]
    Time Taken =  [22.196592569351196, 52.552900552749634, 83.52068829536438, 119.23164415359497, 151.88281631469727, 182.64863061904907, 212.6287977695465, 242.61372184753418]

    CELF

    Seed Nodes =  [135, 230, 229, 216, 221, 190, 226, 0]
    Spread of each seed =  [200.13333333333333, 201.6, 203.0, 204.13333333333333, 205.2, 206.2, 207.2, 208.2]
    Time Taken =  [22.0854172706604, 48.04782819747925, 48.164957761764526, 48.42895460128784, 48.682337045669556, 48.80733275413513, 48.936731815338135, 49.061731576919556]
    Lookups =  [236, 205, 1, 2, 2, 1, 1, 1]

    Please wait for the next k output...

    Calculating...

    For the value of k =  10

    GREEDY

    Seed Nodes =  [135, 230, 229, 216, 221, 0, 190, 193, 226, 95]
    Spread of each seed =  [200.13333333333333, 201.6, 203.0, 204.13333333333333, 205.2, 206.2, 207.2, 208.2, 209.2, 210.13333333333333]
    Time Taken =  [22.13971710205078, 52.29035401344299, 82.78978896141052, 113.27044701576233, 143.93634915351868, 173.85789585113525, 203.74836993217468, 233.65418767929077, 264.10199213027954, 294.01313757896423]

    CELF

    Seed Nodes =  [135, 230, 229, 216, 221, 190, 226, 0, 193, 95]
    Spread of each seed =  [200.13333333333333, 201.6, 203.0, 204.13333333333333, 205.2, 206.2, 207.2, 208.2, 209.2, 210.13333333333333]
    Time Taken =  [22.068960666656494, 48.005027770996094, 48.13002419471741, 48.39006328582764, 48.64702582359314, 48.772022008895874, 48.890459299087524, 49.02340865135193, 49.164029359817505, 53.374934673309326]
    Lookups =  [236, 205, 1, 2, 2, 1, 1, 1, 1, 31]