class Solution {
public:
    int t[21][21];
    bool solve(int i, int j, string s, string p){
        if(j == p.length()){
            return i == s.length();
        }
        if(t[i][j] != -1){
            return t[i][j];
        }
        bool firstmatch = false;
        if(i < s.length() && (s[i] == p[j] || p[j] == '.')){
            firstmatch = true;
        }
        if(j+1 < p.length() && p[j+1] == '*'){
            bool not_take = solve(i, j+2, s, p);
            bool take = firstmatch && solve(i+1, j, s, p);

            return t[i][j] = not_take || take;
        }
        return t[i][j] = firstmatch && solve(i+1, j+1, s, p);
    }
    bool isMatch(string s, string p) {
        memset(t, -1, sizeof(t));
        return solve(0, 0, s, p);
    }
};