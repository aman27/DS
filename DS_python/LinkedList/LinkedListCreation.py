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

