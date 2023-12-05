#!/usr/bin/env python3

class ListNode:
  def __init__(self,val=0,next=None):
      self.val = val
      self.next = next

  def output(self):
      if (self.val is None):
        print("[]")
        return 0

      print(f'{self.val}',end=" ")
      if (self.next is not None):
        self.next.output()
      else:
        print("")


class Solution:
  def mergeTwoLists(self,list1,list2):
      """
      :type list1: Optional[ListNode]
      :type list2: Optional[ListNode]
      :rtype: Optional[ListNode]
      """
      # spliced list
      list3 = ListNode()

      # ends of linked list
      if (list1 is None and list2 is None):
         return None
      if (list1 is None):
        list3.val = list2.val
        list3.next = self.mergeTwoLists(list1,list2.next)
        return list3
      if (list2 is None):
        list3.val = list1.val
        list3.next = self.mergeTwoLists(list1.next,list2)
        return list3

      # empty linked lists
      if (list1.val is None and list2.val is None):
         return ListNode(None,None)
      if (list1.val is None):
         return list2
      if (list2.val is None):
         return list1

      # follow the linked list
      if (list1.val<=list2.val):
        list3.val = list1.val
        list3.next = self.mergeTwoLists(list1.next,list2)
        return list3
      else:
        list3.val = list2.val
        list3.next = self.mergeTwoLists(list1,list2.next)
        return list3


alist = ListNode(1)
alist.next = ListNode(2)
alist.next.next = ListNode(4)

blist = ListNode(1)
blist.next = ListNode(3)
blist.next.next = ListNode(4)

alist.output()
blist.output()

merge = Solution()
clist = merge.mergeTwoLists(alist,blist)
clist.output()


alist = ListNode(None,None)
blist = ListNode(None,None)

alist.output()
blist.output()

merge = Solution()
clist = merge.mergeTwoLists(alist,blist)
clist.output()


alist = ListNode(None,None)
blist = ListNode()

alist.output()
blist.output()

merge = Solution()
clist = merge.mergeTwoLists(alist,blist)
clist.output()
