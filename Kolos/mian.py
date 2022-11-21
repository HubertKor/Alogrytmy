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
        print(f'{current.poprz.wart}<>')

    def pobierz_el(self, idx:int):
        current = self.element
        i = 1
        if idx == 0:
                return self.element
        while current.poprz != self.element:
            i+=1
            if idx > 0:
                return print(f'element: {abs(i - idx)}')
            else:
                return print(f'element:{i - idx}')

    def usun_wsztystkie_pasujace(self,wart: str):
        current = self.element
        temp = None
        while self.element != wart:
            if (self.element.nast == self.element):
                print("nie ma takiego stringa")
                return self.element
            else:
                print('jest taki string')
            temp = current
            current = current.nast
            if current == self.element:
                temp = current.poprz
                current = current.nast
                temp.nast = current.poprz
                current.poprz = temp
            return self.element
            




    def odwroc(self):
        if self.element is not None:
            poprzEle = self.element #przypisany jako głowa
            tempEle = self.element #przypisany jako głowa
            currentEle = self.element.nast #następnik głowy

            poprzEle.nast = poprzEle  #pierwszy element jest ostatnim
            poprzEle.poprz = poprzEle #pierwszy element jest ostatnim

            while(currentEle != self.element):
                tempEle = currentEle.nast 

                currentEle.nast = poprzEle    # typowa zamiana miejscami 
                poprzEle.poprz = currentEle # typowa zamiana miejscami 
                self.element.nast = currentEle # typowa zamiana miejscami 
                currentEle.poprz = self.element # typowa zamiana miejscami 

                poprzEle = currentEle
                currentEle = tempEle

            self.element = poprzEle #zrobienie ostatniego elementu jako pierwszy


    def pobierz_el2(self,idx):
        i = 0
        if idx == 0:
            return self.element
        elif idx > 0:
            while self.element.nast != self.element:
                i += 1
                self.element.nast = self.element
                return i
        else:
            while self.element.poprz != self.element:
                i += 1
                self.element.poprz = self.element
                return i

          
        


l1 = Lista_2k_k()
w1 = ListaWpis('jeden')
l1.element = w1
w2 = ListaWpis('dwa',w1,w1)
w3 = ListaWpis('trzy',w2,w1)
w4 = ListaWpis('cztery',w3,w1)
l1.print_w_tyl()
#w1.zamienn(w3)
l1.odwroc()
l1.print_w_tyl()
l1.pobierz_el(-1)
print(l1.pobierz_el2(0))
l1.print_w_tyl()
l1.usun_wsztystkie_pasujace("cztery")
l1.print_w_tyl
