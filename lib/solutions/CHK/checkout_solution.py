
class CheckoutSolution:
        
    # skus = unicode string
    def checkout(self, skus):
        items = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
        }

        if skus not in items:
            return -1
        else:
            return items[skus]


