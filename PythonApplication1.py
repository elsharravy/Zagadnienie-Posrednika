import data
import calculator

x = 2    #horizontal size
y= 2     #vertical size
popyt = [30,30]    #x
podaz= [45,25]   #y
sell = [12,13]  #x
buy = [6,7]#y
cost_matrix = [[7.0,3.0],[4.0,5.0]]   # x / y


dat = data.data(popyt,podaz,sell,buy,cost_matrix,x,y)

dat = calculator.calculator.calculator_enter(dat)

print("p_m:\n " +str(dat.profit_matrix))

#dat.opt_matrix = [[0,25],[30,0]]

dat = calculator.calculator.calculator_optimalization(dat)

print("o_m:\n " +str(dat.opt_matrix))

dat = calculator.calculator.calculator_exit(dat)


print("profit:\n " +str(dat.profit_total))