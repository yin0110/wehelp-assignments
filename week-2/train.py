# # 題目一
def calculate(min, max):
    sum = 0
    for x in range(min, max+1):
        sum = sum+x
    result = sum
    print(result)


calculate(1, 3)
calculate(4, 8)

# # 題目二


def avg(data):
    a = data["count"]
    sum = 0
    for n in data["employees"]:
        n = n["salary"]
        # print(n)
        sum = sum+n
    print(sum/a)


avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000},
        {
            "name": "Bob",
            "salary": 60000},
        {
            "name": "Jenny",
            "salary": 50000}
    ]
})

# 要求三:演算法
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。 提醒:請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。
# Python


def maxProduct(nums):
    resultarr = []
    for i in nums:
        # print(i)
        for j in nums:
            # 兩個for 可以讓i跟j相乘
            if j == i:
                continue
            # 因為自己會乘到自己，需要跳過這個答案
            y = i*j
            # print(y)
            # 把得到的答案放在list裡
            resultarr.append(y)
# 放print在最外面來跑出最終答案
    # print(resultarr)
    print(max(resultarr))


# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([-1, -2, 0])  # 得到 2


# 要求四 ( 請閱讀英文 ):演算法
# Given an array of integers, show indices of the two numbers such that they add up to a specific target.
# You can assume that each input would have exactly one solution, and you can not use the same element twice.

def twoSum(nums, target):
    # your code here
    arr = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target:
                arr.append(i)
    return arr


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9
