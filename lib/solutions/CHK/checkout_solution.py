
class CheckoutSolution:
        
    # skus = unicode string
    def checkout(self, skus):
        items = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40,
            'F': 10
        }

        v = list(skus)
        
        total = 0
        
        def applyDiscount(letter, amount, cost):
            nonlocal total
            count = v.count(letter)
            discounts = 0
            if count >= amount:
                discounts = count // amount
            
            if discounts > 0:
                for i in range(discounts):
                    total += cost

                    for i in range(amount):
                        s = "".join(v)
                        ind = s.find(letter)
                        del v[ind]

        def applyFree(letter, amount, freeLetter, amountFree = 1):
            nonlocal total
            count = v.count(letter)
            discounts = 0
            if count >= amount:
                discounts = count // amount
            if discounts > 0:
                for i in range(discounts):
                    if (v.count(letter) < amount) or (v.count(freeLetter) < amountFree):
                        return
                    total += items[letter] * amount

                    # remove actual letter
                    for i in range(amount):
                        s = "".join(v)
                        ind = s.find(letter)
                        del v[ind]

                    for i in range(amountFree):
                        s = "".join(v)
                        ind = s.find(freeLetter)
                        if ind == -1:
                            continue
                        del v[ind]
                        print(v)
                    
                    print(v)
                    if (letter not in v) or (freeLetter not in v):
                        return

        # # Getting A offer
        # a_count = v.count("A")
        # a_discounts = 0
        # if a_count >= 3:
        #     # number of discounts
        #     a_discounts = a_count // 3
        # if a_discounts > 0:
        #     for i in range(a_discounts):
        #         total += 130

        #         # Remove 3 As
        #         for i in range(3):
        #             s = "".join(v)
        #             ind = s.find("A")
        #             del v[ind]
        
        # print(v)

        # # Getting B offer
        # b_count = v.count("B")
        # b_discounts = 0
        # if b_count >= 2:
        #     b_discounts = b_count // 2
        # if b_discounts > 0:
        #     for i in range(b_discounts):
        #         total += 45

        #         # Remove 3 As
        #         for i in range(2):
        #             s = "".join(v)
        #             ind = s.find("B")
        #             del v[ind]

        applyDiscount("A", 5, 200)
        print(total)
        applyDiscount("A", 3, 130)
        print(total)
        applyFree("E", 2, "B")
        print(total)
        applyDiscount("B", 2, 45)
        print(total)
        applyFree("F", 2, "F")
        print("F: ", total)

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


# c = CheckoutSolution()

# print(c.checkout("FFFFFF"))

