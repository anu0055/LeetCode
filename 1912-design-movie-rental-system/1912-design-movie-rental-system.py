class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented = defaultdict(SortedList)
        self.priceMap = {}
        self.rentall = SortedList()

        for s, m, p in entries:
            self.unrented[m].add((p, s))
            self.priceMap[(s, m)] = p

    def search(self, movie: int) -> List[int]:
        res = []
        lst = self.unrented.get(movie, [])
        for p, s in lst[:5]:
            res.append(s)
        return res

    def rent(self, shop: int, movie: int) -> None:
        p = self.priceMap[(shop, movie)]
        self.unrented[movie].remove((p, shop))
        self.rentall.add((p, shop, movie))        

    def drop(self, shop: int, movie: int) -> None:
        p = self.priceMap[(shop, movie)]
        self.unrented[movie].add((p, shop))
        self.rentall.remove((p, shop, movie))    

    def report(self) -> List[List[int]]:
        res = []
        for p, s, m in self.rentall[:5]:
            res.append([s, m])
        return res


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()