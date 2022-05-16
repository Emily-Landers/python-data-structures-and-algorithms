# Stack and Queue Pseudo

# Challenge Summary

Create a new class called pseudo queue.
Do not use an existing Queue.
Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
Internally, utilize 2 Stack instances to create and manage the queue
Methods:
enqueue
Arguments: value
Inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue
Arguments: none
Extracts a value from the PseudoQueue, using a first-in, first-out approach.

## Whiteboard Process

![challenge11](whiteBoard.png)

## Approach & Efficiency

.enqueue is only concerned with the first in value so used .push from the Stack class, then a second stack to reverse original stack to .dequeue the first item pushed into original stack.

## Solution

type pytest into terminal