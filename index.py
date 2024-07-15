class Node:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertWithoutPriority(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insertWithPriority(self, node):
        if self.head is None:
            self.head = node
        elif self.head.color == "V":
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next is not None and current.next.color == "A":
                current = current.next
            node.next = current.next
            current.next = node

    def insert(self):
        color = input("Enter the card color (A or V): ")
        number = int(input("Enter the card number: "))
        node = Node(number, color)
        
        if self.head is None:
            self.head = node
        elif color == "V":
            self.insertWithoutPriority(node)
        elif color == "A":
            self.insertWithPriority(node)

    def printWaitingList(self):
        current = self.head
        while current is not None:
            print(f"Card {current.number} - Color {current.color}")
            current = current.next

    def attendPatient(self):
        if self.head is None:
            print("There are no patients in the queue.")
        else:
            print(f"Calling patient with card {self.head.number}")
            self.head = self.head.next

    def menu(self):
        while True:
            print("\nMenu")
            print("1 – Add patient to the queue")
            print("2 – Show patients in the queue")
            print("3 – Call patient")
            print("4 – Exit")
            option = int(input("Choose an option: "))
            
            if option == 1:
                self.insert()
            elif option == 2:
                self.printWaitingList()
            elif option == 3:
                self.attendPatient()
            elif option == 4:
                break
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    queue = LinkedList()
    queue.menu()
