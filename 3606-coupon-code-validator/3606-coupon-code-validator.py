class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        n = len(code)
        valid = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                 "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                 "0","1","2","3","4","5","6","7","8","9","_"]

        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        mp = {"electronics": [], "grocery": [], "pharmacy": [], "restaurant": []}

        for i in range(n):
            if isActive[i] == False:
                continue

            if businessLine[i] not in order:
                continue

            if code[i] == "" or code[i] == " ":
                continue

            is_valid = True
            for c in code[i]:
                if c not in valid:
                    is_valid = False
                    break

            if is_valid:
                mp[businessLine[i]].append(code[i])

        res = []
        for b in order:
            mp[b].sort()
            res.extend(mp[b])

        return res