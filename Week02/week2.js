console.log("第一題");
// 第一題
function calculate(min, max, step){
    // 請用你的程式補完這個函式的區塊
    let WTP=min; // WTP=want to plus (每一 run 想加上去的數字)
    while(WTP<max){ // 判斷WTP是否超過 max
        WTP+=step;
        min+=WTP;
    };
    if(WTP>max){ // 運算時如果 WTP 是個大於 max 的數會被多加一次，所以輸出前再把多加的 WTP 減回來，就像最下面那個題目!!
        min-=WTP;
        console.log("計算結果:", min);
    }else{
        console.log("計算結果:", min);
    };
    }
    calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6
    calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18
    calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0
console.log("第二題");
// 第二題
function avg(data){
// 請用你的程式補完這個函式的區塊
    //console.log(data.employees[0].manager); // 像顆洋蔥一樣慢慢剝開，data 物件裡有 employees 陣列，employees 陣列中有4個物件，4個物件中各有3個屬性
    let total=0;
    let deflator=0
    for(let i=0; i<data.employees.length;i++){
        if(data.employees[i].manager==false){
            total=total+data.employees[i].salary;
            deflator++;
        };
    };
    let result=total/deflator;
    console.log("計算結果:", result);
};
 avg({
    "employees":[
    {
        "name":"John",
        "salary":30000,
        "manager":false
    },
    {
        "name":"Bob",
        "salary":60000,
        "manager":true
    },
    {
        "name":"Jenny",
        "salary":50000,
        "manager":false
    },
    {
        "name":"Tony",
        "salary":40000,
        "manager":false
    }
    ]
    }); // 呼叫 avg 函式
console.log("第三題");
// 第三題
function func(a){
// 請用你的程式補完這個函式的區塊
    return function func1(b, c){
        console.log("計算結果:", a+(b*c));
    }
};
func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
// 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果
console.log("第四題");
//第四題
function maxProduct(nums){ // 把最大(最小)數字拉出來放進一個 array 並刪除原陣列中此最大(最小)數字，再從原陣列找出最大(最小)數字放進 array 中，再將 array 中數字進行相乘得到解答。
    // 請用你的程式補完這個函式的區塊
        // 都取最大
        let max=Math.max(...nums); // 原陣列最大數字
        let result_arr_max=[];
        result_arr_max.push(max);
        let num_nomax=nums.filter(number => number!=max); // 得到一個不含 max 的複製陣列 deep copy
        let max2=Math.max(...num_nomax);
        result_arr_max.push(max2);
        // 都取最小
        let min=Math.min(...nums); // 原陣列最小數字
        let result_arr_min=[];
        result_arr_min.push(min);
        let num_nomin=nums.filter(number => number!=min); // 得到一個不含 min 的複製陣列 deep copy
        let min2=Math.min(...num_nomin);
        result_arr_min.push(min2);
        if(result_arr_max[0]*result_arr_max[1] > result_arr_min[0]*result_arr_min[1]){
            console.log("計算結果:", result_arr_max[0]*result_arr_max[1]);
        }else{
            console.log("計算結果:", result_arr_min[0]*result_arr_min[1]);
        };    
    };
maxProduct([5, 20, 2, 6]); // 得到 120
maxProduct([10, -20, 0, 3]); // 得到 30
maxProduct([10, -20, 0, -3]); // 得到 60
maxProduct([-1, 2]); // 得到 -2
maxProduct([-1, 0, 2]);// 得到 0 或 -0
maxProduct([5, -1, -2, 0]); // 得到 2
maxProduct([-5, -2]); // 得到 10
// 自我檢測組
//maxProduct([-5, -2, -20, -10]); // 應該要200 
console.log("第五題");
// 第五題
function twoSum(nums, target){
    // your code here
    for(let i=0, j=1, total=0, show=[]; j<nums.length; j++){
        total=nums[i]+nums[j];
        if(total==target){ // 這裡要注意不能用 total=target!! 
            show.push(i);
            show.push(j);
            return show;
        }else if(j+1==nums.length){
            i++;
            j=i; // 進到下一次迴圈時 j++ 就可以達到每一輪 i 時 j 比 i 多一單位
        };
    }; 
};
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
console.log("第六題")
// 第六題
function maxZeros(nums){
    // 請用你的程式補完這個函式的區塊
    let i = 0;
    let counter = 0; // 計數器
    let storeArray=[];
    while(i < nums.length){
        if(nums[i] == 0){
            counter++;
            storeArray.push(counter);
            i++;
        }else if(nums[i] == 1){
            storeArray.push(counter);
            counter=0; // 碰到 1 代表 counter 要歸零
            i++;
        }
        storeArray.sort(function(a, b){return b - a}); // .sort() 會將串列轉成 "string" 並利用 UTF-16 code nuits 進行比較，故要利用 comapre function 去比較 "int" 大小!!
    };
    console.log("計算結果:", storeArray[0]);
    }

maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3for (const key in object) {
