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
            # print(value)
            list1.append(value)
            current_node = current_node.next
        list1.append(current_node.val)
        # print("l1 = ", list1)

        list2 = []
        current_node_2 = l2
        # print(current_node_2)
        while current_node_2.next != None:
            value = current_node_2.val
            list2.append(value)
            current_node_2 = current_node_2.next
        list2.append(current_node_2.val)
        # print("l2 =", list2 )

        list1_str = [str(i) for i in list1]
        list2_str = [str(i) for i in list2]
        # print("l1 = ", list1_str, "l2 = ", list2_str)
        str1 = ""
        str2 = ""

        for i in list1_str:
            str1 += i
        
        for i in list2_str:
            str2+=i
        

        int1 = int(str1[::-1])
        int2 = int(str2[::-1])
        numb = (int1 + int2)
        print(numb)
        numb = str(numb)
        numb = numb[::-1]
        num_list = [int(i) for i in numb]
        print(num_list)

        ans = ListNode(val = num_list[0], next = None)
        print(ans.val, ans.next)
        prev_node = ans
        # current_node = None
        # for i in range(1, len(num_list)):
        #     prev_node.next =  ListNode(val = num_list[i], next = None)
        #     print(prev_node.next.val)
        #     current_node = prev_node.next
        #     # print(current_node.val)

        curr_node = ans
        j = 1
        while j < len(num_list):
            curr_node.next =  ListNode(val = num_list[j], next = None)
            curr_node = curr_node.next

            j+=1


    
        return ans

        
