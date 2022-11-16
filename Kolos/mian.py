class ListaWpis:
    def __init__(self,wart: str):
        self.nast = None
        self.poprz = None
        self.wart = wart

class Lista_2k_k:
    def __init__(self):        
        self.head = None
        self.tail = None

    def dodaj_po_nim(self,new_data): # dodaje za nim element
        new_node = ListaWpis(new_data) # tworzenie węzła
        new_node.nast = self.head # nowa głowa jako nowa głowa

        if self.head != None: # sprawdza czy głowa jest pusta czy nie
            self.head.poprz = new_node # stara glowa jako nowa glowa 
            self.head = new_node # nowy węzeł jako nowa głowa
            new_node.poprz = None # poprzednik jako None

        else: # jezeli lista jest pusta tworzy nowy ogon i głowe 
            self.head = new_node 
            self.tail = new_node
            new_node.poprz = None # oba wskaźniki są nullami 
    
    def dodaj_przed_nim(self,new_data):
        new_node = ListaWpis(new_data)
        new_node.poprz = self.tail

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.nast = None

        else:
            self.tail.nast = new_node
            new_node.poprz = None
            self.tail = new_node

    def peek_front(self): # returns first element
        if self.head == None: # checks whether list is empty or not
            print("List is empty")
        else:
            return self.head.wart

w = Lista_2k_k()
print(w.dodaj_przed_nim(1))
print(w.dodaj_po_nim(2))
print(w.peek_front)