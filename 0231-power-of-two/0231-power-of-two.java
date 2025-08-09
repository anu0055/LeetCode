public class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n == 0) return false;
        
        while (n > 0) {
            if (n == 1) return true;
            if (n % 2 != 0) break;
            n /= 2;
        }
        return false;
    }
}

//log method
/*public class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n == 0) return false;
        return Math.floor(Math.log(n) / Math.log(2)) == Math.ceil(Math.log(n) / Math.log(2));
    }
}*/