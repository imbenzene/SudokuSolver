###Sudoku Solver Program-- Using Constraint Propagation Algorithm
=======================================================================

#####Description
The algorithm uses constraint propogation as a method to eliminate multiple entries from a given cell. Constraints are:
- If a square has only one possible value, then eliminate that value from that cell's neighbors
- When a cell has just one possible value, substitue that value there.

Constraint propogation only works on the easy-medium level sudokus. It doesn't converge for the hard sudokus (sample files given in the folder). Further discussed advanced algorithms and heuristics for solving hard sudokus, which I couldn't implement in current version of the program due to time constraints.

#####Instruction for use
On terminal, run the command
python Sudoku_test.py ./sampleFiles/Eg_sudoku2.csv res.csv

where solveSudoku.py is the script containing the algorithm and input.csv is sudoku inpute file (9x9 format, where 0 represents blank cell) and result.csv is the final solution to the sudoku

#####Dependencies
Python 2.7 or 3.4

#####Test Case Check
- All digits in the input matrix of Sudoku are in between 0-9
- Total number of elements in matrix are supposed to be 81


#####Algorithm (Pseduo-code)
-Iterate through list of unsolved cells
-Check dictionary for number possible values, if number is equal to 1
-Cell is solved
-else
-Check neighbors for the cell and remove the value currently being iterated the cell's neighbors
-Recursive call for the same function
-Exit when, all cells have been propagated.



#####Sample Files
- Eg_sudoku1.csv -- solution is obtained
- Eg_sudoku1.csv -- solution is obtained
- Eg_notSolve1.csv -- current program is unable to solve this
- Eg_notSolve1.csv -- current program is unable to solve this

#####Advanced Techniques from Literature
Sudoku solving is one of the hard problems that possess combinatarial explosion sin, while doing space search. Simple brute force is going to definitely very long time, creating need for heuristics.
- Norvig introduces backtracking search <http://norvig.com/sudoku.html>
- Dancing DLX method introduced by Donalt Knuth


#####References
- Peter Norvig's concise notation and initial ideas http://norvig.com/sudoku.html
- Sudoku research and datasets http://lipas.uwasa.fi/~timan/sudoku/
- TDD Algorithm is not right http://vladimirlevin.blogspot.com/2007/04/tdd-is-not-algorithm-generator.html
