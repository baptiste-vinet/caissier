class Caissier :
    
    def __init__(self):
        self.account={}
        self.give={}
        self.total=0


    def create_acount(self, *args): #(value of cash , number of its)

        self.account={}
        
        for value,number in args:
            
            if value in self.account:
                self.account[value]+=number
            else:
                self.account[value]=number

    
    def print_account(self):

        self.total=0
        for cash in self.account:
            self.total+=self.account[cash]*cash
        
        print("\nEtat du compte")
        print(f"Montant total {self.total} € ")
        print("Détail :")

        for cash in self.account:
            print(f"    Nombre billets de {cash} : {self.account[cash]}")

    def print_render(self):
        
        self.render=0
        for cash in self.give:
            self.render+=self.give[cash]*cash
        
        print(f"\nMontant à rendre {self.render} €")
        print("Détail :")

        for cash in self.give:
            print(f"    Nombre billets de {cash} à rendre  : {self.give[cash]}")

    def add_money(self,*args):
        
        for value,number in args:
            
            self.total+=value*number
            if value in self.account:
                self.account[value]+=number
            else:
                self.account[value]=number


    def give_back(self,price,*args):
        
        give=0
        given=0
        
        for value,number in args:
            given+=value*number
  
        self.add_money(*args)
        
        account_modifiel={}
        account_modifiel=self.account.copy()
        self.give={}

        give=given-price

        if give<0:
            print("Pas assez de moula")

        while give!=0:

            
            cash=max(list(account_modifiel.keys()))
            
            self.still=False
           
            if give>=cash and account_modifiel[cash]>=1:
                self.still=True

            if give<cash or account_modifiel[cash]==0:
                del account_modifiel[cash]


            while self.still==True:
                
                give-=cash
                give=round(give,2)
                
                if cash in self.give:
                    self.give[cash]+=1

                else:
                    self.give[cash]=1

                
                account_modifiel[cash]-=1

                if give<cash or account_modifiel[cash]<1:
                    self.still=False

                if account_modifiel[cash]==0 or cash>give:
                    del account_modifiel[cash]

         
        for cash in self.give:
            self.account[cash]-=self.give[cash]




def test():

    C=Caissier()

    C.create_acount((0.01,30),(0.05,30),(0.1,30),(0.2,30),(0.5,30),(1,30),(2,30),(5,10),(10,20),(20,30),(50,5))
    C.print_account()
    
    C.give_back(1.75,(1,2),(0.5,1),(0.2,1),(0.05,1))

    C.print_render()

    C.print_account()


test()