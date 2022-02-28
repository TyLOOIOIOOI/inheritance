
class Person:
    def __init__(self,name,address,tn):
        self.__name=name
        self.__address=address
        self.__tn=tn

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_tn(self):
        return self.__tn

    def print_person(self):
        print("The name of the person is:",self.__name)
        print("The address of the person is:",self.__address)
        print("The telephone number of the person is:", self.__tn)



class Customer(Person):
    
    def __init__(self, name, address, tn, cn, ml):

        Person.__init__(self, name, address, tn)

        self.__cn = cn
        self.__ml = ml

    def get_cn(self):
        return self.__cn

    def get_ml(self):
        return self.__ml 

    def print_person(self):
        Person.print_person(self)
        print("The customer number is:", self.__cn)
        print("If the person wants to be on the mail list:",self.__ml)






