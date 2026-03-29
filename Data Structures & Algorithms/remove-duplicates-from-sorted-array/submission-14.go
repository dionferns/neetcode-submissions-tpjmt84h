func removeDuplicates(nums []int) int {
    leftp := 1

    for rightp:=1; rightp<len(nums);rightp++ {
        if nums[rightp] != nums[rightp - 1] {
            nums[leftp] = nums[rightp]
            leftp++
        }
    }
    return leftp
}
