class Solution {
    char str[];

    public int removeSubstring(String pair, int score){
        int totalScore = 0;
        char firstTargetchar = pair.charAt(0);
        char secTargetchar = pair.charAt(1);
        int writeIndex = 0;
        for(int readIndex=0;str[readIndex]!='$'; readIndex++){
            str[writeIndex]=str[readIndex];
            writeIndex++;
            if(writeIndex>1){
                char firstchar = str[writeIndex-2];
                char secchar = str[writeIndex-1];
                if(firstchar==firstTargetchar && secchar==secTargetchar){
                    writeIndex-=2;
                    totalScore +=score;
                }
            }
        }
        str[writeIndex]='$';
        return totalScore;
    }

    public int maximumGain(String s, int x, int y) {
        int n = s.length();
        str = new char[n+1]; //n+1 to use marker in the array
        for(int i=0;i<n;i++){
            str[i]=s.charAt(i);
        }
        str[n] = '$';//Fr Marker
        String firstPair = (x>y)?"ab":"ba";
        String secPair = (firstPair.equals("ab"))?"ba":"ab";
        int score = 0;

        score = removeSubstring(firstPair, Math.max(x,y));
        System.out.println(str);

        score += removeSubstring(secPair, Math.min(x,y));
        return score;
    }
}