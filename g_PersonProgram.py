import g_Person as p

regular_person = p.Person('Mark', "110 South", 123456789)

customer = p.Customer("Ty", "111 South", 987654321, "001", True)

regular_person.print_person()
customer.print_person()
