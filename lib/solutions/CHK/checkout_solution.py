
class CheckoutSolution:

    def __init__(self):
        self.items = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
        }

    # skus = unicode string
    def checkout(self, skus):
        if skus not in items:
            return -1
        else:
            return items[skus]

