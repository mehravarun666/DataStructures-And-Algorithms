# LINKED LIST

class Node:
    def __init__(self,item = None,next= None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self,start = None) -> None:
        self.start = start
    
    def isempty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n

    def insert_at_last(self,data):
        n = Node(data)
        if not self.isempty():
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self,value)->Node:
        if not self.isempty():
            temp = self.start
            while temp.next != None:
                temp = temp.next
                if temp.item == value:
                    return temp
        else:
            return self.start
    
    def insert_after(self,item,data):
        temp = self.start
        while temp is not None:
            if temp.item == item:
                n = Node(data,temp.next)
                temp.next = n
                return 
            else:
                temp = temp.next
        return None
    def print_list(self):
        temp=self.start
        while temp is not None:
            print (temp.item, end=' ')
            temp = temp.next

    def delete_at_first(self):
        if self.start is not None:
            self.start = self.start.next
    
    def delete_at_last(self):
        if self.start is not None:
            pass
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    
    def delete_item(self,item):
        if self.start is not None:
            pass
        if self.start.item == item:  
            self.start = self.start.next
            return
        temp = self.start
        while temp.next.next is not None:
            if(temp.next.item == item):
                temp.next = temp.next.next
                return
            temp = temp.next



mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
print(mylist.search(50))
mylist.insert_after(20,25)
mylist.insert_at_last(40)
mylist.insert_at_last(50)
mylist.delete_item(40)
mylist.print_list()
print()
mylist.delete_item(30)
mylist.print_list()
print()