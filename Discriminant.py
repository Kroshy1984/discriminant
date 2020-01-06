class Discriminant ():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.equal=str(a)+'x'+chr(178)+'+'+str(b)+'x'+'+'+str(c)+'=0'
        self.Discriminant=self.b**2-4*self.a*self.c
		