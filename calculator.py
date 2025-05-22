from re import A
import data

class calculator(object):
    def __init__(self):
        a=0
    @staticmethod
    def calculator_enter(dat):
        
        for i in range(dat.x):
            for j in range(dat.y):
                dat.profit_matrix[i][j] = dat.sell[i] -dat.buy[j] - dat.cost_matrix[i][j] 
        return dat
    
    @staticmethod
    def calculator_exit(dat):
        
        for i in range(dat.x):
            for j in range(dat.y):
                dat.income_total += dat.opt_matrix[i][j] * dat.sell[i]
                dat.buy_cost_total += dat.opt_matrix[i][j] * dat.buy[j]
                dat.transport_cost_total += dat.opt_matrix[i][j] * dat.cost_matrix[i][j]
        dat.profit_total =  dat.income_total - dat.buy_cost_total - dat.transport_cost_total
        return dat
    
    @staticmethod
    def calculator_optimalization(dat):
        
        alpha =[]
        alpha_s =[]
        beta =[]
        beta_s =[]
        for k in range(dat.y):
            alpha.append(0.0)
            alpha_s.append(False)
        for k in range(dat.x):
            beta.append(0.0)
            beta_s.append(False)
           
        dummy =[]
        dummy.append(alpha)
        sign = [dummy[0][:] for _ in range(dat.x)]
        delta = [dummy[0][:] for _ in range(dat.x)]
        
        i=0
        j=0
        suma_x = 0.0
        suma_y = 0.0
        a = dat.opt_matrix[0][1]
        while True:
            suma_x = 0.0
            suma_y = 0.0
            delta[i][j] = 1
            for k in range(dat.x):
                suma_x += dat.opt_matrix[k][j]
            for k in range(dat.x):
                suma_y += dat.opt_matrix[i][k]
            dif_x = dat.popyt[i] - suma_x
            dif_y = dat.podaz[j] - suma_y
            if dif_x < dif_y:
                dif = dif_x
            else:
                dif = dif_y
            if dif <=0:
                dif =0.0
                delta[i][j] = 0
            dat.opt_matrix[i][j] = dif
            
            j += 1
            if j == dat.y:
                j=0
                i +=1
                
            if i == dat.x:
                break
        
        for k in range(dat.y):
            alpha[k] = 0.0
            alpha_s[k] = False
        for k in range(dat.x):
            delta[k] = 0.0
            alpha_s[k] = False

        alpha_s[dat.y-1] = 1

        while True:

            


            j += 1
            if j == dat.y:
                j=0
                i +=1
                
            if i == dat.x:
                break
        
        return dat


