class Node(object):
  def __init__(self, v):
    self.val = v
    self.next = None

head = Node(3)
node2 = Node(4)
node3 = Node(5)
node4 = Node(6)
node5 = Node(7)

head.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

head2 = Node(1)
head2.next = Node(3)
head2.next.next = Node(5)
head2.next.next.next = Node(7)

def printList(head):
  print("PRINTING FINAL LIST:")
  current = head
  while(current):
    print(current.val)
    current = current.next

def mergeLists(head1, head2):
  #Two pointers
  p1 = head1
  p2 = head2
  #Determine the new head of list
  if p1.val < p2.val:
    #p1 is head
    p1 = p1.next
    mergeHelper(p1,p2,head1)
  else:
    #p2 is head
    p2 = p2.next
    mergeHelper(p1,p2,head2)

def mergeHelper(a,b,c):
  while
  if a.val < b.val:
    c.next = a
    a = a.next
  else:
    c.next = b
    b = b.next
  c = c.next
  if a.val == None and b.val == None:
    return 1
  mergeHelper(a,b,c)

printList(head)
printList(head2)

mergeLists(head, head2)

printList(head)
printList(head2)
