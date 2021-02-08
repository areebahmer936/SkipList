import random
class Node:
    def __init__( self, data, height=0):
        # initializing a node with two attributes
        # i.e. data and an array
        self.data = data
        self.next = [None]*(height+1) # this array will be used for pointers, pointing next node in its level


class skipList:
    def __init__(self):
        #starting with a None Node for the sentinel, as a head
        self.sentinel = Node(None)
        #the size of base linked list
        self.lenght=0

    # returns the height of the given object's next array
    def height(self, x):
        return len(x.next)

    # this private function finds node before the desired node, that we wanna find
    def _find_pred_node(self,x):
        u=self.sentinel
        r=self.height(self.sentinel)-1
        while r>=0: # until it reaches level 0

            # checks at all levels, starting from the highest.
            # if a node exist after it, and its value is less than x, go forward
            while u.next[r]!=None and u.next[r].data<x:
                u=u.next[r]
                 #if next node is None or the next node value is bigger, the loop terminates
            r-=1 #then go down the sentinel
        return u

    def find(self, x):
        #takes the node returned from fin_pred to return the value for the next node
        u=self._find_pred_node(x)
        if u.next[0]==None: return None
        return u.next[0].data

    def pick_height(self):
        # a simultaion to flipping coins scenario
        import random
        z = random.getrandbits(32) #get random integer as binary form
        k = 0
        while z & 1: # uses a bitwise AND operator, that runs until it gets 0
            k = k + 1
            z = z // 2
        return k

    def add(self, x):
        u=self.sentinel
        r=self.height(self.sentinel)-1
        # initializing a stack, which keeps the record of the nodes
        # from where we moved to add the value
        stack = [None] * 30
        while r>=0:
            while u.next[r]!=None and u.next[r].data<x:
                u=u.next[r] # go Forward
            if u.next[r]!=None  and u.next[r].data==x: return False
            stack[r]=u
            r=r-1 # go Downward
        w=Node(x,self.pick_height()) # initializing a node with a random height
        h=self.height(self.sentinel)-1

        #if the node picked height greater than sentinel's, sentinel also increases height
        while h<(self.height(w))-1:
            h+=1
            self.sentinel.next.append(None) # sentinel's Height Increased.
            stack[h]=self.sentinel

        # making sentinel's array point towards the next node on the level
        # by stack, that we used for temporarily holding the nodes,
        # the loop below make the sentinel or nodes point towards the next node
        for i in range(self.height(w)):
            w.next[i]=stack[i].next[i] #
            stack[i].next[i]=w

        self.lenght+=1 #total size increased of the base linked list
        return True

    def remove(self, x):
        # setting an identifier to False to check later if the node is removed or not
        removed=False
        u=self.sentinel
        r=self.height(self.sentinel)-1

        # until it reaches level 0, do
        while r>=0:
            # checks at all levels, starting from the highest.
            # if a node exist after it, and its value is less than x, go forward
            while u.next[r]!=None and u.next[r].data<x:
                u=u.next[r] # Go Forward

            if u.next[r]!=None and u.next[r].data==x: # if value found
                removed=True
                #setting the previous node's next pointer to next(the node that is to remove) to next node
                u.next[r]=u.next[r].next[r]

                if u==self.sentinel and u.next[r]==None:
                    # sentinel's Height decreased, if the removed node had the highest height
                    self.sentinel.next.pop()
            r=r-1
        if removed: self.lenght-=1
        return removed

    # a method to visually represent the skiplist
    def displayList(self):
        x=10
        print("\n---------------Skip List----------------")
        head = self.sentinel
        for lvl in reversed(range(len(head.next))):
            print("Level {}: ▯⟶ ".format(lvl), end="")
            node = head.next[lvl]
            while (node != None):
                print(node.data, end=" ")
                node = node.next[lvl]
            print("")

# dirver codes
if __name__=="__main__":
    s=skipList()
    w=[1, 2 ,3, 4, 6, 7, 8, 9, 11, 12, 14, 15, 17, 18, 22, 23, 24, 25 ,26, 27, 29 ,31, 32, 36, 37, 41 ,44 ,46, 48, 49]
    for i in range(len(w)):
        s.add(w[i])
    s.remove(15)
    s.displayList()

