#Node Class
class Node:

	#Function to initilize the node object
	def __init__(self, data):
		self.data = data  #Assign data to node
		self.next = None  #Initialize next 
						  #node as null
	
#LinkedList Class
class LinkedList:

	#Function to initialize the LinkedList
	#object
	def __init__(self):
		self.head = None

	#Funtion to print content of Linked List
	#starting from head
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			#print(temp.data, end=" ")
			temp = temp.next

	#Function to insert new node at the bignening
	def push(self, new_data):

		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	
	def insertAfter(self, prev_node, new_data):
		
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

		
	def append(self, new_data):

		new_node = Node(new_data)

		if self.head is None:
			self.head = new_node
			return

		temp = self.head
		while (temp.next):
			temp = temp.next

		temp.next = new_node
			


#Code execution start here
if __name__=='__main__':

	#start with emty Linked List
	llist = LinkedList()

	llist.head = Node(1)
	seconed = Node(2)
	third = Node(3)

	llist.head.next = seconed
	seconed.next = third

	llist.printList()
	#print()

	llist.push(0)

	llist.printList()

	llist.insertAfter(seconed, 5)

	llist.printList()

	llist.append(6)

	llist.printList()



