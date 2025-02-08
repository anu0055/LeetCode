class NumberContainers:

    def __init__(self):
        self.mp = {}
        self.nums_idx = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.mp[index] = number
        heappush(self.nums_idx[number], index)    

    def find(self, number: int) -> int:
        if number not in self.nums_idx:
            return -1
        while self.nums_idx[number]:
            i = self.nums_idx[number][0]
            if self.mp[i]==number:
                return i
            heappop(self.nums_idx[number])
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)