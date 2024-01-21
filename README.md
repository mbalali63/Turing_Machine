# Turing_Machine
Implement a simple Turing Machine in python


Here I have implemented a very simple Turing Machine, using Python.
The class Turning, is where the instructions are defined. the instructions are defined 
in a pandas dataframe called rulesSet.
The instructions fields are: 
* 'Current State'
* 'Current Tape'
* 'Write to Tape'
* 'Move'
* 'Update State'

modifying the tape is implemented using a function called runInstruction(), with state, tapeVal and index
as arguments. these arguments specify the current state, value and index.
The main function of the Turning class is runMachine().
it marches the blocks of tape and modify them according to the instructions.

The instructions are for incrementing the input number by 1.
