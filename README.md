# Hospital Queue Management System

This program simulates a patient queue management system in a hospital, where patients are assigned cards with different colors to indicate their priority level.

## Features

- Patients with yellow cards (A) are prioritized over those with green cards (V).
- Among patients with the same color card, those with lower numbers are attended to first.
- The system supports adding patients, displaying the current queue, and calling the next patient in line.

## Classes and Methods

### `Node` Class
Represents a node in the linked list with the following attributes:
- `number`: The card number.
- `color`: The card color (A for yellow, V for green).
- `next`: Pointer to the next node.

### `LinkedList` Class
Represents the linked list and provides methods to manage the queue.

#### Methods

- `insertWithoutPriority(node)`: Inserts a node at the end of the list.
- `insertWithPriority(node)`: Inserts a node in the list maintaining priority for "A" cards.
- `insert()`: Prompts the user for the card's color and number, then inserts the node in the list accordingly.
- `printWaitingList()`: Prints all the nodes in the list.
- `attendPatient()`: Removes and announces the first patient in the list.
- `menu()`: Displays the menu and handles user input to call the appropriate functions.
