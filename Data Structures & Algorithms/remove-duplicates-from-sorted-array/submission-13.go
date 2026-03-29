func removeDuplicates(nums []int) int {
    leftp := 1
    rightp := 1

    for rightp<len(nums) {
        if nums[rightp] == nums[rightp - 1] {
            rightp++
        } else {
            nums[leftp] = nums[rightp]
            rightp++
            leftp++
        }
    }
    return leftp
}
