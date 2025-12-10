
class CheckoutSolution:
        
    # skus = unicode string
    def checkout(self, skus):
        items = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
        }

        
        total = 0
        for char in skus:
            if skus not in items:
                return -1
            else:
                total += items[skus]

        return total



