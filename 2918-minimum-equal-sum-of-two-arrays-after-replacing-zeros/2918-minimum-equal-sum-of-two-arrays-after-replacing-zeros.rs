impl Solution {
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let mut sum_1 : i64 = 0;
        let mut sum_2 : i64 = 0;
        let mut zeros_1 = 0;
        let mut zeros_2 = 0;

        for &num in &nums1 {
            sum_1 += num as i64;
            if (num == 0){
                zeros_1 += 1;
                sum_1 += 1;
            }
        }
        for &num in &nums2 {
            sum_2 += num as i64;
            if (num == 0){
                zeros_2 += 1;
                sum_2 += 1;
            }
        }
        if ((zeros_1 == 0 && sum_2 > sum_1) || (zeros_2 == 0 && sum_1 > sum_2)){
            return -1;
        }
        return sum_1.max(sum_2);
    }
}