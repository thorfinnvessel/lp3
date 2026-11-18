import heapq

class node:
    def __init__(self,char,freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def huffman_encoding(chars):
    heap = []

    for char,freq in chars:
        heapq.heappush(heap,(freq,len(heap),node(char,freq)))

    while len(heap)>1:
        f1,_,left = heapq.heappop(heap)
        f2,_,right = heapq.heappop(heap)

        new_node = node('$',f1+f2)
        new_node.left = left
        new_node.right = right

        heapq.heappush(heap,(new_node.freq,len(heap),new_node))

    def print_codes(root,code=""):
        if root is None:
            return

        if root.char!='$':
            print(root.char,":",code)

        print_codes(root.left, code+"0")
        print_codes(root.right, code+"1")

    print("huffman codes:")
    print_codes(heap[0][2])

n = int(input("enter number of characters:"))
chars = []

for i in range(n):
    ch = input("enter charaters:")
    freq = int(input("enter frequency:"))
    chars.append((ch,freq))

huffman_encoding(chars)