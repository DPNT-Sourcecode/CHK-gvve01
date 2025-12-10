
class CheckoutSolution:
        
    # skus = unicode string
    def checkout(self, skus):
        items = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
        }

        v = skus
        
        # get offers
        a_count = skus.count("A")
        if a_count % 3 == 0:
            print("Discount")   

        # remove the applied offers

        # do rest

        for i, char in enumerate(skus):
            # print(char)
            if char not in items:
                return -1
            else:
                total += items[char]

        return total


c = CheckoutSolution()

print(c.checkout("AAABX"))