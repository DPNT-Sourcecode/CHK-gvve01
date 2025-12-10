
class CheckoutSolution:
        
    # skus = unicode string
    def checkout(self, skus):
        items = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40,
            'F': 10,
            "G": 20,
            "H": 10,
            "I": 35,
            "J": 60,
            "K": 70,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 20,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 17,
            "Y": 20,
            "Z": 21
        }

        v = list(skus)
        
        total = 0
        group1 = ('S', 'T', 'X', 'Y', 'Z')

        def applyGroupDiscount(group, require_amount, cost):
            current_amount = 0
            items_list = []
            for item in group1:
                if item in v:
                    current_amount += 1
                    items_list.append(item)
            
            if current_amount >= require_amount:
                print(items_list)
                sorted_r = sorted(items_list, key=lambda x: items[x])
        
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

        applyGroupDiscount(group1, 3, 45)
        applyDiscount("A", 5, 200)
        applyDiscount("A", 3, 130)
        applyFree("E", 2, "B")
        applyDiscount("B", 2, 45)
        applyFree("F", 2, "F")
        applyDiscount("H", 10, 80)
        applyDiscount("H", 5, 45)
        applyDiscount("K", 2, 120)
        applyFree("N", 3, "M")
        applyDiscount("P", 5, 200)
        applyFree("R", 3, "Q")
        applyDiscount("Q", 3, 80)
        
        applyFree("U", 3, "U")
        applyDiscount("V", 3, 130)
        applyDiscount("V", 2, 90)

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

print(c.checkout("ZTX"))




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







