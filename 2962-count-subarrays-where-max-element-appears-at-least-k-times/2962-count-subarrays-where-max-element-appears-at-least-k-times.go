func countSubarrays(nums []int, k int) int64 {
    n := len(nums)
    max := 0
    count_max := 0
    var count_sub int64 = 0

    // Loop for finding the max in the array
    for i, _ := range nums {
        if nums[i] > max {
            max = nums[i]
        }
    }
    
    //Sliding Window
    var i int64 = 0
    for j := 0; j < n; j++ {
        if nums[j] == max {
            count_max++
        }
        for count_max >= k {
            if(nums[i] == max){
                count_max--
            }
            i++
        }
        count_sub += i
    }

    return count_sub
}