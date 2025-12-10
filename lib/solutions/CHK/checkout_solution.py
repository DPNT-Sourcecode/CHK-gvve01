
class CheckoutSolution:
        
    # skus = unicode string
    def checkout(self, skus):
        items = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
        }

        v = list(skus)
        
        total = 0
        # get offers

        # Getting A offer
        a_count = v.count("A")
        a_discounts = 0
        if a_count > 3:
            # number of discounts
            a_discounts = a_count // 3
        if a_discounts > 0:
            for i in range(a_discounts):
                total += 130

                # Remove 3 As
                for i in range(3):
                    s = "".join(v)
                    ind = s.find("A")
                    del v[ind]
        
        print(v)

        # Getting B offer
        b_count = v.count("B")
        b_discounts = 0
        if b_count > 
        if (b_count % 2 == 0) and (b_count > 0):
            for i in range(a_count//2):
                total += 45

                # Remove 3 As
                for i in range(2):
                    s = "".join(v)
                    ind = s.find("B")
                    del v[ind]

        if len(v) == 0:
            return total
        # do rest
        for char in v:
            # print(char)
            if char not in items:
                return -1
            else:
                total += items[char]

        return total


c = CheckoutSolution()

print(c.checkout("AAA"))
