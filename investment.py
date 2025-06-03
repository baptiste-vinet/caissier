import numpy as np
import matplotlib.pylab as plt

class investment:
     
    def __init__(self):
        self.agenda=[]
        self.annuite=0
        self.type=1


        
    def borrow(self,amount ,time, rate,types=1): #type==1 --> anuités constantes, type==0 --> anuités variables 
        self.agenda=[]
        remaining_amount=amount
        r=rate/100

        self.type=types

        if types==1 :
            self.annuite=amount*r/(1-(1+r)**(-time))
            self.annuite=round(self.annuite,2)

            for month in range(time):
                interest=r*remaining_amount
                refund=self.annuite-interest
                remaining_amount-=refund
                self.agenda.append({"mois":month+1,"annuite":self.annuite,"interets":round(interest,2) ,"capital_remboursé":round(refund,2), "capital_restant":round(remaining_amount,2)})
            
        else:
            refund=amount/time

            for month in range(time):
                interest=r*remaining_amount
                self.annuite=r*remaining_amount+refund
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
        annuite=[]
        for months in (self.agenda):
            month.append(months["mois"])
            interets.append(months["interets"])
            capital_rembourse.append(months["capital_remboursé"])
            annuite.append(months["annuite"])
            capital_restant.append(months["capital_restant"])
        
        plt.plot(month,interets,label="interets")
        if self.type==0:
            plt.plot(month,annuite,label="annuite")

        plt.plot(month,capital_rembourse,label="capital remboursé ce mois")
        plt.plot(month,capital_restant,label="restant à rembourser")

        if self.type==1:
            plt.title(f"Schéma emprunt bancaire avec annuités constantes de {self.annuite} €")
        else:
            plt.title(f"Schéma emprunt bancaire avec annuités variables")
        
        
        plt.grid()
        plt.legend()
        plt.show()  


    def comparaison(self, amount, time,rate):

        sim1=investment()
        sim2=investment()

        sim1.borrow(amount,time,rate,1)
        sim2.borrow(amount,time,rate,0)

        sim1_total={"Methode annuités constantes":0,"debourse":0, "total interets":0}
        sim2_total={"Methode annuités variables":0,"debourse":0, "total interets":0}

        for month in range (len(sim1.agenda)):

            sim1_total["debourse"]+=sim1.agenda[month]["annuite"]
            sim2_total["debourse"]+=sim2.agenda[month]["annuite"]

            sim1_total["total interets"]+=sim1.agenda[month]["interets"]
            sim2_total["total interets"]+=sim2.agenda[month]["interets"]
        
        print(sim1_total)
        print(sim2_total)





def test():
    I=investment()
    #I.borrow(10000,5,5,0)
    #I.print_borrow()
    #I.plot_borrow()

    I.comparaison(10000,5,5)


test()
        