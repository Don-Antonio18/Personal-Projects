class frac:
    def __unnit__(self, n, d):
        self.data = [n,d]

    def num(self):
        return self.data[0]
    
    def denum(self):
        return self.data[1]
    
    def __add__(self,f ):
        n1 = self.num()
        d1 = self.denum()
        n2 = f.num()
        d2 = f.denum()
        return frac( n1*d2 + n2*d1, d1 +d2)
