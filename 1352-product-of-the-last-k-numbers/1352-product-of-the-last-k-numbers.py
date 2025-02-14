class ProductOfNumbers:

    def __init__(self):
        self.pre_products = []

    def add(self, num: int) -> None:
        if num == 0:
            self.pre_products.clear()
        else:
            last_num = self.pre_products[-1] if self.pre_products else 1
            self.pre_products.append(last_num * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.pre_products):
            return 0
        elif k == len(self.pre_products):
            return self.pre_products[-1]
        else:
            return self.pre_products[-1] // self.pre_products[-k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)