#Definition for singly-linked list.
#Created by: Sebastián Felipe García Rojas

class ListNode:
    def __init__(self, val):
        self.val = val      # Assing the data to a particular node
        self.next = None    # Initialize the pointer of the first node to None

class LinkedList:
    def __init__(self):
        self.head = None    # Initialize the head of the first node as None 
    
    def insertAtBegining(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node
    
#    def printList(self):
#        temp = self.head
#        while temp:                   # If it's not equal to None
#            print(temp.val, end=' ')  # Print the node value
#            temp = temp.next          # Continue to the next node
#        print()                       # Print new line at the end of the linked list

def InsertNodeValues(Input):
    Input.reverse()

    #Create the linkedList
    ListNode = LinkedList()

    for Value in Input:
        ListNode.insertAtBegining(Value)

    return ListNode

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        previus = None
        current = head

        while current:
            if current.val == val: 
                if previus:  
                    previus.next = current.next
                else:  
                    head = current.next
                current = current.next  
            else:  
                previus, current = current, current.next

        return head 



if __name__ == "__main__":

    Input = [1,4,6,3,2,6,2,6]
    val = 6
    
    ListNode = InsertNodeValues(Input)
#   ListNode.printList()

    solution = Solution()
    result = solution.removeElements(ListNode.head,val)
    
#    NewListNode = LinkedList()
#    NewListNode.head = result
#    NewListNode.printList()