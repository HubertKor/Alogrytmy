class ListaWpis:
    def __init__(self, wart, poprzedni=None, nastepny=None):
        self.nast = nastepny
        self.poprz = poprzedni
        self.wart = wart
        if self.nast is None and self.poprz is None:
            self.nast = self
            self.poprz = self
        else:
            self.poprz.nast = self
            self.nast.poprz = self

    def dodaj_po_nim(self, wart):
        temp = self.nast
        self.nast = ListaWpis(wart, self, temp)

    def dodaj_przed_nim(self, wart):
        temp = self.poprz
        self.poprz = ListaWpis(wart, temp, self)

    def zamien(self, el_inny): # 1->2->3->    /  ->2->1->3
        tempp = self.poprz #1
        tempn = self.nast #3
        self.poprz = el_inny #2
        self.nast = el_inny #1
        el_inny.poprz = tempp #2 /1
        el_inny.nast = self #1 /3
        self.nast = el_inny

    def zamienn(self, el_inny):
        temp = None
        temp = self.nast
        self.nast = el_inny.nast
        el_inny.nast = temp

        if self.nast != None:
            self.nast.poprz = self
        if el_inny.nast != None:
            el_inny.nast.poprz = el_inny

        temp = self.poprz
        self.poprz = el_inny.poprz
        el_inny.poprz = temp

        if self.poprz != None:
            self.poprz.nast = self
        if el_inny.poprz != None:
            el_inny.poprz.nast = el_inny

class Lista_2k_k:
    def __init__(self):
        self.element = None

    def print_w_tyl(self):
        current = self.element
        while current.poprz != self.element:
            print(f'{current.poprz.wart}<>', end='')
            current = current.poprz
        print(f'{current.poprz.wart}<>', end='')

    def pobierz_el(self, idx:int):
        if idx == 0:
            return self.element


l1 = Lista_2k_k()
w1 = ListaWpis('jeden')
l1.element = w1
w2 = ListaWpis('dwa',w1,w1)
w3 = ListaWpis('trzy',w2,w1)
w4 = ListaWpis('cztery',w3,w1)
l1.pobierz_el(0)
(w1.zamienn(w3))
l1.print_w_tyl()
