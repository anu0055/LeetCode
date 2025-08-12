class Solution {
public:
    int mod = 1000000007;
    int temp[301][301];
    long long powerLL(int base, int exp, int limit) {
        long long result = 1;
        for (int i = 0; i < exp; i++) {
            result *= base;
            if (result > limit) return result; // stop early to prevent overflow
        }
        return result;
    }

    int dp(int num, int k, int x) {
        if (num == 0) return 1;
        if (num < 0 || k > 300) return 0;

        long long p = powerLL(k, x, num);
        if (p > num) return 0;

        if (temp[num][k] != -1) return temp[num][k];

        int take = dp(num - (int)p, k + 1, x) % mod;
        int not_take = dp(num, k + 1, x) % mod;

        return temp[num][k] = (take + not_take)%mod;

    }
    int numberOfWays(int n, int x) {
        memset(temp, -1, sizeof(temp));
        return dp(n, 1, x);
    }
};