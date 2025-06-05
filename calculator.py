from re import A, T
import data

class calculator(object):
    def __init__(self):
        a=0
    @staticmethod
    def calculator_enter(dat):
        
        for i in range(dat.x):
            for j in range(dat.y):
                #print("cord:\n " +str(i) + " " + str(j))
                #print("cord:\n "  + " " + str( dat.cost_matrix) + str(dat.profit_matrix))
                dat.profit_matrix[i][j] = dat.sell[i] -dat.buy[j] - dat.cost_matrix[i][j] 
        return dat
    
    @staticmethod
    def calculator_exit(dat):
        dat.income_total = 0
        dat.buy_cost_total = 0
        dat.transport_cost_total = 0
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
        for k in range(dat.y+1):
            alpha.append(0.0)
            alpha_s.append(False)
        for k in range(dat.x+1):
            beta.append(0.0)
            beta_s.append(False)
           
            
        dummy =[]
        dummy.append(alpha)
        

        dummy_b =[]
        dummy_b.append(alpha_s)
        
        sign = [dummy_b[0][:] for _ in range(dat.x+1)]
        sign_p = [dummy_b[0][:] for _ in range(dat.x+1)]
        delta = [dummy[0][:] for _ in range(dat.x+1)]
        
        progres = False
        i=0
        j=0
        prof_max = dat.profit_matrix[0][0]
        maxi_i = 0
        maxi_j = 0
        temp = True
        while True:
            #print("o_mmmmmm:\n " +str(dat.opt_matrix))
            i=0
            j=0
            while True:
                if sign_p[i][j] == False:
                    progres = True
                    if prof_max < dat.profit_matrix[i][j] or temp:
                        temp = False
                        maxi_i = i
                        maxi_j = j
                        prof_max = dat.profit_matrix[i][j]
            
                    
                j += 1
                if j >= dat.y:
                    j=0
                    i +=1
                
                if i == dat.x:
                    i=0
                    break
                
            if progres == False:
                break
            progres = False
            #print("cord:\n " +str(maxi_i) + " " + str(maxi_j))
            temp = True
            sign_p[maxi_i][maxi_j] = True
            suma_x = 0.0
            suma_y = 0.0
            a = dat.opt_matrix[0][1]
            
            delta[maxi_i][maxi_j] = 1
            for k in range(dat.x):
                #print("cordx:\n " +str(k) + " " + str(dat.opt_matrix[k][maxi_j]))
                suma_x += dat.opt_matrix[k][maxi_j]
            for k in range(dat.y):
                #print("cordy:\n " +str(k) + " " + str(dat.opt_matrix[maxi_i][k]))
                suma_y += dat.opt_matrix[maxi_i][k]
            #print("sums:\n " +str(suma_x) + " " + str(suma_y))
            #print("pop:\n " +str(dat.popyt) + " " + str(dat.podaz))
            dif_y = dat.popyt[maxi_i] - suma_y
            dif_x = dat.podaz[maxi_j] - suma_x
            if dif_x < dif_y:
                dif = dif_x
            else:
                dif = dif_y
            if dif <=0:
                dif =0.0
                delta[maxi_i][maxi_j] = 0
            dat.opt_matrix[maxi_i][maxi_j] = dif
            if dat.profit_matrix[maxi_i][maxi_j] < 0:
                dat.opt_matrix[maxi_i][maxi_j]  = 0
            #print("o_mmmmmm:\n " +str(dat.opt_matrix))
        j = 0
        i = 0
        
        #print("o_m:\n " +str(dat.opt_matrix))
        
        while True:
            
            
                if dat.opt_matrix[i][j] == 0.0:
                    sign[i][j] = False
                    #delta[i][j] = dat.profit_matrix[i][j]
                else:
                    sign[i][j] = True
                    delta[i][j] = 0
                #print("cord:\n " +str(i) + " " + str(j))
                #print("o_m:\n " +str(dat.opt_matrix))
               
                #print("popyt/pod:\n " +str(dat.popyt[i]) +"/"+ str(dat.podaz[j]))
                suma_obej =0
                for k in range(dat.x):
                    suma_obej += dat.opt_matrix[k][j]
                    #print("sumxx\n " +str(dat.opt_matrix[k][j]))
                if suma_obej - dat.podaz[j]== 0.0:
                    sign[dat.x][j] = False
                else:
                    sign[dat.x][j] = True
                dat.opt_matrix[dat.x][j] = dat.podaz[j]- suma_obej
                
                #print("pop-------:\n " +str(dat.popyt[i])+ "-" +str(suma_obej))
                suma_obej =0
                for k in range(dat.y):
                    suma_obej += dat.opt_matrix[i][k]
                    #print("sum\n " +str(dat.opt_matrix[i][dat.y]))
                if suma_obej - dat.popyt[i]== 0.0:
                    sign[i][dat.y] = False
                else:
                    sign[i][dat.y] = True
                dat.opt_matrix[i][dat.y] = dat.popyt[i] - suma_obej
                #print("podaz-------:\n " +str(dat.podaz[i])+ "-" +str(suma_obej))
                    
                #print("o_m:\n " +str(dat.opt_matrix))
                j += 1
                if j == dat.y:
                    j=0
                    i +=1
                
                if i == dat.x:
                    break
        j = 0
        i = 0
        
        #print("o_m:\n " +str(dat.opt_matrix))
        
       
        while True:
            for k in range(dat.y):
                alpha[k] = 0.0
                alpha_s[k] = False
            for k in range(dat.x):
                beta[k] = 0.0
                beta_s[k] = False
                #print("c_aaaaaaaaaaaaaa:\n " +str(delta))
            while True:
            
                if dat.opt_matrix[i][j] == 0.0:
                    sign[i][j] = False
                    #delta[i][j] = dat.profit_matrix[i][j]
                else:
                    sign[i][j] = True
                    delta[i][j] = 0
                 
                """
                print("o_m:\n " +str(dat.opt_matrix))
                suma_obej =0
                for k in range(dat.x):
                    suma_obej += dat.opt_matrix[k][j]
                if suma_obej - dat.popyt[j]== 0.0:
                    sign[dat.x][j] = False
                else:
                    sign[dat.x][j] = True
                dat.opt_matrix[dat.x][j] = dat.popyt[j]- suma_obej
                suma_obej =0
                for k in range(dat.y):
                    suma_obej += dat.opt_matrix[i][dat.y]
                if suma_obej - dat.podaz[i]== 0.0:
                    sign[i][dat.y] = False
                else:
                    sign[i][dat.y] = True
                dat.opt_matrix[i][dat.y] = dat.podaz[i] - suma_obej
                """ 
                j += 1
                if j == dat.y:
                    j=0
                    i +=1
                
                if i == dat.x:
                    break
            i = 0
            j = 0
            progres = False
            while True:
                #print("aaaaaaaaaaaaaaaaaaaaaa:\n " +str(i) + " " + str(j))
                while True:
                    
                    #print("a_m:\n " +str(beta))
                    if alpha_s[j] == True and beta_s[i] == False and sign[i][j] == True:
                        #print("cordaaaaaaaa:\n " +str(i) + " " + str(j))
                        beta[i] = dat.profit_matrix[i][j] - alpha[j]
                        beta_s[i] = True
                        progres = True
                    elif alpha_s[j] == False and beta_s[i] == True and sign[i][j] == True:
                        #3print("cord:\n " +str(i) + " " + str(j))
                        alpha[j] = dat.profit_matrix[i][j] - beta[i]
                        alpha_s[j] = True
                        progres = True
                

                    j += 1
                    if j == dat.y:
                        j=0
                        i +=1
                
                    if i == dat.x:
                        break
            
                i = dat.x-1
                j = dat.y-1
                if progres == False:
                    while True:
                        if alpha_s[j] == False:
                            alpha[j] = 0.0
                            alpha_s[j] = True
                            progres = True
                            break
                
               
                        j -= 1
                        if j == -1:
                            break
            
                i = 0
                j = 0
                if progres == False:
                    break
                progres = False
        
            i = 0
            j = 0
            progres = False
            maxi = 0
            maxi_i = 0
            maxi_j = 0
            
            while True:
            
            
                delta[i][j] = dat.profit_matrix[i][j] - alpha[j] - beta[i]
                if delta[i][j] and sign[i][j] == False > 0.0:
                    #print("cods delta:\n " +str(i) + " " + str(j) + " delta: " + str(delta[i][j]))
                    
                    progres = True
                if delta[i][j]and sign[i][j] == False  > maxi:
                    maxi = delta[i][j]
                    maxi_i = i
                    maxi_j = j
                    #progres = True
                j += 1
                if j == dat.y+1:
                    j=0
                    i +=1
                
                if i == dat.x+1:
                    break
            print("o_m:\n " +str(dat.opt_matrix))
            print("a_m:\n " +str(alpha))
            print("b_m:\n " +str(beta))
            print("delta:\n " +str(delta))
            i = 0
            j = 0
            for k in range(dat.y):
                for l in range(dat.x):
                    dat.opt_matrix_tmp[l][k] = dat.opt_matrix[l][k] 
            #print("s_mmmmmmmmmmmm:\n " +str(sign))
            if progres == False:
                break
            high = -1
            leng = -1
            max_prof = 0.0
            max_h = 0
            max_l = 0
            max_change = 0.0
            p_h = 1
            #print("s_mmmmmmmmmmmm:\n " +str(sign))
            #print("delta:\n " +str(delta))
            #print("cord:\n " +str(maxi_i) + " " + str(maxi_j))
            while True:
                #print("t_cords:\n " +str(high) + " " + str(leng))
                if((maxi_i + high) < dat.x +1 and (maxi_j + leng) < dat.y +1 and (maxi_i + high) >= 0 and (maxi_j + leng) >= 0) and ((maxi_i - high) < dat.x +1 and (maxi_j - leng) < dat.y +1 and (maxi_i - high) >= 0 and (maxi_j - leng) >= 0):
                    progres = True
                    if sign[maxi_i + high][maxi_j] and sign[maxi_i][maxi_j + leng]:
                        max_change = dat.opt_matrix[maxi_i + high][maxi_j]
                        if dat.opt_matrix[maxi_i][maxi_j+leng] < max_change:
                            max_change = dat.opt_matrix[maxi_i][maxi_j+leng]
                    
                
                        dat.opt_matrix[maxi_i][maxi_j] += max_change
                        dat.opt_matrix[maxi_i + high][maxi_j] -= max_change
                        dat.opt_matrix[maxi_i][maxi_j + leng] -= max_change
                        dat.opt_matrix[maxi_i + high][maxi_j + leng] += max_change
                        dat = calculator.calculator_exit(dat)
                        
                        #print("o_m:\n " +str(dat.opt_matrix))
                        
                        #print("profit:\n " +str(dat.profit_total))
                        if max_prof < dat.profit_total:
                            max_prof = dat.profit_total
                            max_h = high
                            max_l = leng
                        dat.opt_matrix[maxi_i][maxi_j] -= max_change
                        dat.opt_matrix[maxi_i + high][maxi_j] += max_change
                        dat.opt_matrix[maxi_i][maxi_j + leng] += max_change
                        dat.opt_matrix[maxi_i + high][maxi_j + leng] -= max_change
            
                if high > 0: 
                    if leng > 0: 
                        if leng >= dat.y:
                            high = 1 + p_h
                            p_h +=1
                            leng = 1
                            if high > dat.x:
                                break
                        else:
                            leng += 1
                        leng = -leng
                        high = -high
                    else:
                        leng = - leng
                    
                elif leng > 0:
                    high = -high
                    leng = -leng
                else:
                    leng = - leng

                
            
            if max_change == dat.opt_matrix[maxi_i + max_h][maxi_j]:
                sign[maxi_i + max_h][maxi_j] = False
            elif max_change == dat.opt_matrix[maxi_i][maxi_j + max_l]:
                sign[maxi_i][maxi_j + max_l] = False
            dat.opt_matrix[maxi_i][maxi_j] += max_change
            dat.opt_matrix[maxi_i + max_h][maxi_j] -= max_change
            dat.opt_matrix[maxi_i][maxi_j + max_l] -= max_change
            dat.opt_matrix[maxi_i + max_h][maxi_j + max_l] += max_change
        return dat


