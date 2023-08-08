# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        current_node = l1
        
        while current_node.next != None:
            value = current_node.val
            list1.append(value)
            current_node = current_node.next
        list1.append(current_node.val)
        

        list2 = []
        current_node = l2
        
        while current_node.next != None:
            value = current_node.val
            list1.append(value)
            current_node = current_node.next
        list2.append(current_node.val)

        list1_str = [str(i) for i in list1]
        list2_str = [str(i) for i in list2]

        str1 = ""
        str2 = ""

        for i in list1_str:
            str1 += i
        
        for i in list2_str:
            str2+=i
        print("strings = ", str1, "   ", str2)

        int1 = int(str1[::-1])
        int2 = int(str2[::-1])
        numb = (int1 + int2)
        print(numb)
        numb = str(numb)
        numb = numb[::-1]
        num_list = [int(i) for i in numb]


        ans = ListNode(val = num_list[0], next = None)
        prev_node = ans
        current_node = prev_node.next
        
        for i in range(1, len(num_list)):
            current_node =  ListNode(val = num_list[i], next = None)
            print(current_node.val)
            current_node = current_node.next
            
        return ans

        
