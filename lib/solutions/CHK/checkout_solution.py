
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
        total = 0
        # get offers
        a_count = skus.count("A")
        if a_count % 3 == 0:
            for i in range(a_count//3):
                total += 150

                # find an A
                indexs = v.find("A")
                print(indexs)

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
