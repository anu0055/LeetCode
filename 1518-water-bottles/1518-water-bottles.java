class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int drank = numBottles;
        while(numBottles >= numExchange){
            int extraEmpty = numBottles % numExchange;
            int exchanged = numBottles / numExchange;
            drank+=exchanged;
            numBottles = extraEmpty + exchanged;
        }
        return drank;
    }
}