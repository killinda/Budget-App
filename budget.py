class Category(object):
    def __init__(self, category):   
        self.category = category 
        self.ledger =[]   
        self.deposit_number = 0
        self.withdraw_number = 0
        self.dic = {}
    def deposit(self,amount,description = None):
        self.deposit_number += amount 
        if description:
            self.dic = {}
            self.dic["amount"] = amount
            self.dic["description"] =description
            self.ledger.append(self.dic)
        else:
            self.dic = {}
            self.dic["amount"] = amount
            self.dic["description"] =""
            self.ledger.append(self.dic)
    def withdraw(self,amount,description = None):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw_number += amount 
            if description:
                self.dic = {}
                self.dic["amount"] = -amount
                self.dic["description"] =description
                self.ledger.append(self.dic)
            else:
                self.dic = {}
                self.dic["amount"] = -amount
                self.dic["description"] =""
                self.ledger.append(self.dic)
            return True
    def get_balance(self):
        return self.deposit_number-self.withdraw_number
    def transfer(self,amount,object):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount,"Transfer to "+ object.category)
            object.deposit(amount,"Transfer from "+self.category )
            return True
    def check_funds(self,amount):
        if amount >(self.deposit_number-self.withdraw_number):
            return False
        else:
            return True
    def __str__(self):
        first_line = str(self.category).center(30,"*")
        other_lines = self.ledger
        final_result = []
        final_result.append(first_line)
        for line in other_lines:
            price = line["amount"]
            price = "%7.2f"%float(price)
            description = str(line["description"])[0:23].ljust(23," ")
            final_result.append(description+price)
        final_result.append("Total: "+str(self.deposit_number-self.withdraw_number))
        return "\n".join(final_result)




def create_spend_chart(object):
    name_list = [] 
    total_spending = 0
    total_array = "Percentage spent by category\n"
    for i in object:
        name_list.append(i.category)
        total_spending += i.withdraw_number
    max_column = len(max(name_list,key = len))
    

    for number in reversed(range(0,110,10)):
        total_array +=("%3d"%number+"|")
        for category in object:
             category_spending_precentage = int((category.withdraw_number/total_spending)*100)
             if number >  category_spending_precentage:
                 total_array +=("   ")
             else:
                 total_array +=(" o ")
        total_array +=(" \n")
    total_array += ("    "+"-"*(3*len(name_list)+1)+"\n")   
    for length in range(max_column):
        total_array +=("    ")
        for category in object:
            if length<len(category.category):
                total_array +=(" "+category.category[length]+" ")
                
            else:
                total_array +=("   ")
        total_array +=(" \n")     
    return total_array.rstrip()+ '  '
  
