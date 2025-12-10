
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


        a_count = v.count("A")
        if a_count % 3 == 0:
            for i in range(a_count//3):
                total += 150

                # Remove 3 As
                for i in range(3):
                    s = "".join(v)
                    ind = s.find("A")
                    del v[ind]
                    print(v)



                

        # remove the applied offers

        # do rest

        # for i, char in enumerate(skus):
        #     # print(char)
        #     if char not in items:
        #         return -1
        #     else:
        #         total += items[char]

        # return total


c = CheckoutSolution()

print(c.checkout("AAABX"))


