def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    count = 1  # 記錄數字幾次連續出現
    maxN = 0  # 紀錄最大數字
    pre_n = None  # 紀錄前一個數字
    for n in nums:
        if n == pre_n and n == 0:
            count = count+1
            # maxN = max((count, maxN))  # max裡面要放list, 這裡意思是放入前一個數字跟新的數字作比較
            maxN = max((count, maxN))  # 因為if成立的時候才要計算最大值，所以max要放在這
        else:
            pre_n = n  # 因為原本數字為none所以直接會跳入else裡, 當ｎ＝＝ｎ的時候就會進入if 迴圈
            # 這是取代前一個數字的方法
            count = 1  # 這裏count已經計算過一次，所以必須=1

    print(maxN)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3
