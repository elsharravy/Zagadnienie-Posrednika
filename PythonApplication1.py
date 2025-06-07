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


print("\n\n\n " +str(dat.profit_total))


print("profit:\n " +str(dat.profit_total))


x = 3    #horizontal size
y= 2     #vertical size
popyt = [16,12,24]    #x
podaz= [20,40]   #y
sell = [18,16,15]  #x
buy = [7,8]#y
cost_matrix = [[4,8],[7,10],[2,4]]   # x / y

dat = data.data(popyt,podaz,sell,buy,cost_matrix,x,y)

dat = calculator.calculator.calculator_enter(dat)

print("p_m:\n " +str(dat.profit_matrix))

#dat.opt_matrix = [[0,25],[30,0]]

dat = calculator.calculator.calculator_optimalization(dat)

print("o_m:\n " +str(dat.opt_matrix))

dat = calculator.calculator.calculator_exit(dat)


print("profit:\n " +str(dat.profit_total))


print("\n\n\n " +str(dat.profit_total))


print("profit:\n " +str(dat.profit_total))


x = 2    #horizontal size
y= 3     #vertical size
popyt = [20,30]    #x
podaz= [18,32,20]   #y
sell = [30,20]  #x
buy = [7,8,6]#y
cost_matrix = [[4,5,2],[-3,3,3]]   # x / y


dat = data.data(popyt,podaz,sell,buy,cost_matrix,x,y)

dat = calculator.calculator.calculator_enter(dat)

print("p_m:\n " +str(dat.profit_matrix))

#dat.opt_matrix = [[0,25],[30,0]]

dat = calculator.calculator.calculator_optimalization(dat)

print("o_m:\n " +str(dat.opt_matrix))

dat = calculator.calculator.calculator_exit(dat)


print("profit:\n " +str(dat.profit_total))