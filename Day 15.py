    def insert(self,head,data): 
    #Complete this method
        new_node = Node(data)
        original_head = head
        # Empty list?
        if (head == None):
            head = Node(data)
        else:
            current_node = head
            while (current_node.next != None):
                # Move forward
                current_node = current_node.next
            current_node.next = Node(data)
        return head
            
        
    