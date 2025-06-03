import numpy as np
import matplotlib.pylab as plt

class investment:
     
    def __init__(self):
        v=0
        self.agenda=[]
        self.annuite=0
        self.type=1


        
    def borrow(self,amount ,time, rate,types=1): #type==1 --> anuités constantes, type==0 --> anuités variables 
        self.agenda=[]
        remaining_amount=amount
        r=rate/100

        self.type=types

        if type==1 :
            self.annuite=amount*r/(1-(1+r)**(-time))
        
        for month in range(time):
            interest=r*remaining_amount
            refund=self.annuite-interest
            remaining_amount-=refund

            self.agenda.append({"mois":month+1,"annuite":self.annuite,"interets":round(interest,2) ,"capital_remboursé":round(refund,2), "capital_restant":round(remaining_amount,2)})

        
    def print_borrow(self):
        for month in (self.agenda):
            print(month)


    def plot_borrow(self):
        month=[]
        interets=[]
        capital_rembourse=[]
        capital_restant=[]
        for months in (self.agenda):
            month.append(months["mois"])
            interets.append(months["interets"])
            capital_rembourse.append(months["capital_remboursé"])
            capital_restant.append(months["capital_restant"])
        
        plt.plot(month,interets,label="interets")
        plt.plot(month,capital_rembourse,label="capital remboursé ce mois")
        plt.plot(month,capital_restant,label="restant à rembourser")

        if self.type==1:
            plt.title(f"Schéma emprunt bancaire avec annuités constantes")

        else:
            plt.title(f"Schéma emprunt bancaire avec annuités variables")
        plt.grid()
        plt.legend()
        plt.show()  



def test():
    I=investment()
    I.borrow(10000,5,5)
    I.print_borrow()
    I.plot_borrow()


test()
        