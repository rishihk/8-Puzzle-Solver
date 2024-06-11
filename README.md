# 8-Puzzle-Solver

    In this project I implemented A*, BFS, and IDS algorithms.
    Utilized three heuristic functions (Ah1, Ah2, Ah3) for A* to explore their impact on search performance.
    Conducted tests across various problem depths to observe average run time and nodes explored.

## Overview

    Part 1: Algorithm Implementation
        Objective: Implement the A*, BFS, and IDS algorithms.
        Details: Each algorithm was coded and set up to function with predefined problem spaces. The A* algorithm was integrated with three distinct heuristics (Ah1, Ah2, Ah3) to test their effectiveness.

    Part 2: Performance Testing
        Objective: Conduct performance tests across varying problem depths (e.g., 8, 15, 24).
        Details: The algorithms were run against problems of different depths to collect data on average run time and nodes explored. This helped in understanding how each algorithm scales with increasing problem complexity.

    Part 3: Analysis and Comparison with differnt depths
        Objective: Analyze and compare the performance of the algorithms.
        Details: The collected data were analyzed to identify trends in algorithm efficiency, particularly focusing on the impact of heuristic choice for A* and comparing these results against the performances of BFS and IDS. Special attention was given to scalability issues at higher depths.

## Findings

    A* algorithms with heuristics outperformed BFS and IDS in efficiency.
    Ah2 emerged as the most effective heuristic for A*.
    Significant performance differences were noted at higher problem depths, emphasizing the choice of algorithm and heuristic.
    IDS faced scalability issues at depth 24, indicating its impracticality for deeper problems.

## How to compile the program.

    1. cd into the root (Lab 1 directory)

    2. run the command below
       python3 main.py –fPath <testcasefile.txt> –algo <algoname> 

    3. For <testcasefile.txt> you can enter any valid file path with a 8 puzzle test case.

    4. For <algoname> you can choose 1 from the five algorithms BFS, IDS, h1, h2, h3.

    5. The result will be printed into the terminal.

## Citations

    Aimacode, GitHub. https://github.com/aimacode 