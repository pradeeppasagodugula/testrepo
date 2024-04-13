class student():
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a,b)
    def printing(self,a,b):
        print(a,b)
    '''
    def printing(self,a,b):
        print(self.a,self.b)
        o/p:2 3'''
    
s=student(2,3)
s.printing(4,5)