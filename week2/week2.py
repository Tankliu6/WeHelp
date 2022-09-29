print("第一題")
# 第一題
def calculate(min, max, step):
# 請用你的程式補完這個函式的區塊
    WTP=min
    while WTP<max:
        WTP+=step
        min+=WTP
    if WTP>max:
        min-=WTP
        print("計算結果:",min)
    else:
        print("計算結果:",min)
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0
print("第二題")
# 第二題
def avg(data):
# 請用你的程式補完這個函式的區塊
    total=0
    deflator=0
    for i in range(len(data["employees"])):
        if data["employees"][i]["manager"]==False:
            total+=data["employees"][i]["salary"]
            deflator+=1          
    result=int(total/deflator) # int()去除小數點
    print("計算結果:", result)
avg({
    "employees":[
    {
        "name":"John",
        "salary":30000,
        "manager":False
    },
    {
        "name":"Bob",
        "salary":60000,
        "manager":True
    },
    {
        "name":"Jenny",
        "salary":50000,
        "manager":False
    },
    {
        "name":"Tony",
        "salary":40000,
        "manager":False
    }
    ]
}) # 呼叫 avg 函式
print("第三題")
# 第三題
def func(a):
# 請用你的程式補完這個函式的區塊
    def func1(b, c):
        result=a+(b*c)
        print("計算結果：", result)
    return func1

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果
print("第四題")
#第四題
def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    # 都取最大(會遺漏負負得正可能會最大的情形，可以用都取最小補足!) 
    # 原本想說可以創造一個 nums2 串列來當作都取最小的原始陣列，但會發現 nums2 的資料會受到 nums 的任何修改影響
    nums2 = nums.copy() # 複製一個原始陣列給都取最小使用(如果使用 nums2=nums 會變成將 nums assign 給 nums2，會造成任何修改都只是修改 nums 原始資料)
    maxValue1 = max(nums) # 從 [5, 20, 2, 6] 中拿出20
    nums.remove(maxValue1) #大關鍵!!因為 Python 會把原來陣列直接改變成 [5, 2, 6] 不會產生 JS 的 shallow array
    maxValue2 = max(nums) #從 [5, 2, 6] 中拿出6
    result_max = maxValue1*maxValue2
    # 都取最小(修正負負得正被遺漏的問題)
    minValue1 = min(nums2)
    nums2.remove(minValue1) 
    minValue2 = min(nums2)
    result_min = minValue1*minValue2
    if result_max > result_min:
        print("計算結果:", result_max)
    else:
        print("計算結果:", result_min)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10
print("第五題")
#第五題
def twoSum(nums, target):
    # your code here
    # enviorment elememt
    i=0
    j=1
    def nextRound(i, j): # 靈感來源：https://stackoverflow.com/questions/14829640/how-to-continue-in-nested-loops-in-python
        for j in range(j, len(nums)):
            total=nums[i]+nums[j] 
        if total==target:
            show=[]
            show.extend((i, j))
            return show
        elif j+1 == len(nums):
            i=i+1
            j=i
            #print([i, j])
            #print(len(nums))
            return nextRound(i, j)   
    for j in range(j, len(nums)):
        total=nums[i]+nums[j]
        if total==target:
            show=[]
            show.extend((i, j))
            return show
        elif j+1 == len(nums):
            i=i+1
            j=i
            return nextRound(i, j)
# 底下是解題過程中遇到的盲點紀錄!!
        # if total==target:
        #     show=[]
        #     show.extend((i,j))
        #     return show
        # elif check == nums_len: # !!問題在這裡，無法進入此判斷式(已解決，被 JS 的解法誤導，elif 進去後並不會自動跑回 outer loop 再跑一次而是要向上方解法一樣 return 一個 function 再進去跑一次)
        #     i+=1
        #     j=i
result=twoSum([2, 11, 7, 15], 9)
print("計算結果:",result) # show [0, 2] because nums[0]+nums[2] is 9
