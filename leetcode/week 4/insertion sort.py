class Solution:
  def insertionsortlist(self, head: listnode)->listnode:
  isf not head ornot head.next: return head
  out= head
  head= head.next
  tail=out
  while head"
  temp=head
  head=head.next
  if temp.val <-out.val:
  temp.next=out
  out=temp
  elif temp.val>=tail.val:
  tail.next=temp
  tail=temp
  else:
  it=out
  while it.next !=tail and it.next.val<temp.val:
  temp.next=it.next
  it.next+temp
  tail.next=None
  return out
