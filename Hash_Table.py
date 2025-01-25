class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    #Constructor for HAshtable class
    def __init__(self, size):
        #Initialized size of the hash table
        self.size = size  
        #Create the link list of size same as hash table with no elements
        self.table = [None] * self.size  
    
    def hash_function(self, key):
        #hash function using modulus of key with the size
        return hash(key) % self.size
    
    def insert(self, key, value):
        #find the index by using hash function and send the key
        index = self.hash_function(key)
        #object to create a new node with the key and value
        new_node = Node(key, value)
        # If the slot is empty, insert the node directly
        if not self.table[index]:
            self.table[index] = new_node
        else:
            # Chaining: Append to the linked list at this index
            current = self.table[index]
            #keep going to next until reached the end
            while current.next:
                current = current.next
            #add the new node at the end
            current.next = new_node
    
    def search(self, key):
        #find the index by using hash function and send the key
        index = self.hash_function(key)
        #variable to keep track of current node
        current = self.table[index]
        
        #Keep going until key found or reached end
        while current:
            if current.key == key:
                return f"Found the value {current.value} at key {current.key}" 
            current = current.next
        return 'Not Found'
    
    def delete(self, key):
        #find the index by using hash function and send the key
        index = self.hash_function(key)
        #variable to keep track of current node
        current = self.table[index]
        #variable to keep track of prev so prev could be added next to the one being deleted
        prev = None
        
        #Keep going until key found or reached end
        while current:
            if current.key == key:
                #if found take prev node and make it point to current's next node
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            #move to the following node for next iteration
            prev = current
            current = current.next
        return False 
    
    def print_table(self):
        # Print the hash table with key-value pairs
        for index, node in enumerate(self.table):
            #keep going until reached end
            if node is not None:
                print(f"Index {index}: ", end="")
                current = node
                # Traverse the linked list at this index and print key-value pairs
                while current:
                    print(f"({current.key}: {current.value})", end=" -> ")
                    current = current.next
                print("End")  #End of the linked list at this index
            else:
                print(f"Index {index}: End")  # Empty slot
#user input for size of hash table               
size = int(input("Enter the size of the hash table: "))
#Object for hash table with the entered size
hash_table = HashTable(size)

# Inserting key-value pairs
hash_table.insert(20, 10)
hash_table.insert(30, 20)

# Searching for a key
print(hash_table.search(20))
print(hash_table.search(30))  
hash_table.print_table()


# Deleting a key
hash_table.delete(20)
print(hash_table.search(20 ))

