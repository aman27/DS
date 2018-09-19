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
			print(temp.data),
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

	def deleteNode(self, key):

		temp = self.head

		if temp is not None:
			if temp.data == key:
				self.head = temp.next
				temp = None

		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		if temp == None:
			return
		prev.next = temp.next
		temp = None	
		
	def deleteNodeFrmPostion(self, position):

		if self.head == None:
			return 

		temp = self.head

		if position == 0:
			self.head = temp.next
			temp == None
			return

		for i in range(position-1):
			temp = temp.next
			if temp == None:
				break

		if (temp or temp.next) is None:
			return		
   		
   		
		frwd_node = temp.next.next

		temp.next = None

		temp.next = frwd_node

	def deleteList(self):

		current = self.head
		while current:
			frwd_node = current.next
			del current.data
			current = frwd_node 


		 



			
			

		
			


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
	print()

	llist.push(0)

	llist.printList()
	print()

	llist.insertAfter(seconed, 5)

	llist.printList()
	print()

	llist.append(6)

	llist.printList()
	print()

	llist.deleteNode(5)

	llist.printList()
	print()

	llist.deleteNodeFrmPostion(3)

	llist.printList()
	print()

	llist.deleteList()

	



