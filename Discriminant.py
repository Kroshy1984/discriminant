class Discriminant ():
    def __init__(self,a,b,c):
        self.a=int(a)
        self.b=int(b)
        self.c=int(c)
        self.equal=str(a)+'x'+chr(178)+'+'+str(b)+'x'+'+'+str(c)+'=0'
        self.equal=self.equal.replace('-1x','-')
        self.equal=self.equal.replace('+1x','+')
        self.equal=self.equal.replace('1'+'x'+chr(178),'x'+chr(178))
        self.equal=self.equal.replace('0'+'x'+chr(178)+'+','')
        self.equal=self.equal.replace('x+0','x')
        self.equal=self.equal.replace('+0x','+')
        self.equal=self.equal.replace('++','+')
        self.equal=self.equal.replace('+-','-')
        self.Discriminant=self.b**2-4*self.a*self.c