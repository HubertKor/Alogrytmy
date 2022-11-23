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

        if self.nast is None:
            self.nast.poprz = self
        if el_inny.nast is None:
            el_inny.nast.poprz = el_inny

        temp = self.poprz
        self.poprz = el_inny.poprz
        el_inny.poprz = temp

        if self.poprz is None:
            self.poprz.nast = self
        if el_inny.poprz is None:
            el_inny.poprz.nast = el_inny


class Lista_2k_k:
    def __init__(self):
        self.element = None

    def print_w_tyl(self):
        if self.element is not None:
            current = self.element
            while current.poprz != self.element:
                print(f'{current.poprz.wart}<>', end='')
                current = current.poprz
            print(f'{current.poprz.wart}<>')

    def pobierz_el(self, idx: int):
        current = self.element
        i = 0
        if idx == 0:
            return self.element
        while i < idx:
            i += 1
            current = current.nast
        return current

    def usun_wsztystkie_pasujace(self, wart: str):
        i = 0
        current = self.element
        while current.poprz != self.element:
            current = current.poprz
            i += 1
        if self.element is None:
            return 0
        if i == 0:
            self.element = None
            return 1
        res = 0
        current = self.element
        j = 0
        while j != i:
            if current.wart == wart:
                current.poprz.nast = current.nast
                current.nast.poprz = current.poprz
                res += 1
            j += 1
            current = current.nast
        self.element = current.nast
        return res

    def odwroc2(self):
        i = 1
        current = self.element
        while current.nast != self.element:
            current = current.nast
            i += 1
        if i != 1:
            j = 0
            current1 = self.element
            while j < i:
                self.element = self.element.poprz
                current2 = current1.poprz
                temp = current1.poprz
                current1.poprz = current1.nast
                current1.nast = temp
                current1 = current2
                j += 1
            self.element = self.element.nast

    def pobierz_el2(self, idx):
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

    def obrob_wartosc(self, funkcja):
        if self.element is not None:
            currnet = self.element
            while currnet.nast != self.element:
                funkcja(currnet.wart, currnet.nast.wart)
                currnet = currnet.nast
            funkcja(currnet.wart, currnet.nast.wart)


def fun_wypisz(str1: str, str2: str):
    print(str1, str2)


l1 = Lista_2k_k()
w1 = ListaWpis('jeden')
l1.element = w1
w2 = ListaWpis('dwa', w1, w1)
w3 = ListaWpis('trzy', w2, w1)
w4 = ListaWpis('jeden', w3, w1)
w5 = ListaWpis('piec', w4, w1)
l1.print_w_tyl()
print(l1.pobierz_el(5).wart)
print(l1.usun_wsztystkie_pasujace('jeden'))
l1.obrob_wartosc(fun_wypisz)
l1.print_w_tyl()
l1.odwroc2()
l1.print_w_tyl()
l2 = Lista_2k_k()
l2.obrob_wartosc(fun_wypisz)
m1 = ListaWpis('jeden')
m2 = ListaWpis('jeden', m1, m1)
m3 = ListaWpis('jeden', m2, m1)
l2.element = m1
print(l2.usun_wsztystkie_pasujace('jeden'))
l2.print_w_tyl()
