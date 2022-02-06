#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    revised=llist
    prev=llist
    llist=llist.next
    while llist:
        if llist.data==prev.data:
            prev.next=llist.next
        else:
            prev=prev.next
        llist=llist.next
    return revised
        
