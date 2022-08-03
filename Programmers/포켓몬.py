def solution(nums):
    max_get = int(len(nums)/2)
    n_list = list(set(nums))

    if len(n_list) > max_get:
        return max_get
    else:
        return len(n_list)

nums = [3,1,2,3]
print(solution(nums))