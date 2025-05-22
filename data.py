class data: # 7 pierwszych warosci odpowiada tym z 1 prezentacji
    def __init__(self,pop,pod,sell_price,buy_price,c_m,xa,ya):
        self.x = xa    #horizontal size
        self.y= ya     #vertical size
        self.popyt = pop    #x
        self.podaz= pod     #y
        self.sell = sell_price  #x
        self.buy = buy_price #y
        self.cost_matrix = c_m      # x / y
        

        # this sets up matrix with a dynamic size
        d =[]
        for k in range(self.y):
            d.append(0.0)
        dummy =[]
        dummy.append(d)
        self.profit_matrix = [dummy[0][:] for _ in range(self.x)]   # x / y  dummy
        self.opt_matrix = [dummy[0][:] for _ in range(self.x)]      # x / y  dummy
        
        self.income_total = 0.0
        self.buy_cost_total = 0.0
        self.transport_cost_total = 0.0
        self.profit_total = 0.0
        
        print("c_m:\n " +str(self.cost_matrix))
# gettery i settery na wszelki

    def get_es(self):
        return self.x
    
    def set_es(self, val):
        self.x = val
        
    def get_es(self):
        return self.y
    
    def set_es(self, val):
        self.y = val  
        
    def get_es(self):
        return self.popyt
    
    def set_es(self, val):
        self.popyt = val
        
    def get_es(self):
        return self.podaz
    
    def set_es(self, val):
        self.podaz = val  
        
    def get_es(self):
        return self.sell
    
    def set_es(self, val):
        self.sell = val
        
    def get_es(self):
        return self.buy
    
    def set_es(self, val):
        self.buy = val  
        
    def get_es(self):
        return self.cost_matrix
    
    def set_es(self, val):
        self.cost_matrix = val
        
    def get_es(self):
        return self.prifit_matrix
    
    def set_es(self, val):
        self.profit_matrix = val
        
    def get_es(self):
        return self.opt_matrix
    
    def set_es(self, val):
        self.opt_matrix = val
        
    def get_es(self):
        return self.income_total
    
    def set_es(self, val):
        self.income_total = val
        
    def get_es(self):
        return self.buy_cost_total
    
    def set_es(self, val):
        self.buy_cost_total = val
        
    def get_es(self):
        return self.transport_cost_total
    
    def set_es(self, val):
        self.transport_cost_total = val
        
    def get_es(self):
        return self.profit_total
    
    def set_es(self, val):
        self.profit_total = val  



