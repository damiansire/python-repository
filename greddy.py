# Problema de las monedas
def greddyMoney():
   money = [ 1 , 5 , 10 , 20 , 50 ]
   residualPay = 96
   selectedMoney = []
   index = len(money) - 1
   while(residualPay > 0):
      pay = residualPay - money[index]
      if(pay >= 0):
         residualPay = pay
         selectedMoney.append(money[index])
      else:
         index = index - 1
   return selectedMoney