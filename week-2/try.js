//題目一

function calculate(min,max){
    let sum=0
    for(let i=min; i<=max; i++){
        sum=sum+i
    }
    let result=sum;
    console.log(result);
}
calculate(1, 3)
calculate(4, 8)

// 題目二
function avg(data){
    let sum=0
    //利用.來抓取employees的array, employee取為此array名稱
    data.employees.forEach((employee, index, array) => {
        //抓到employees的arrat之後，再抓取salary的值
    // console.log(employee.salary)
    //把sum放在foreach裡才會重複加總
    sum=employee.salary+sum
    });
    console.log(sum/data["count"]);
}
avg({
    "count":3,
    "employees":[{
                    "name":"John",
                    "salary":30000 
                },
                {
                "name":"Bob",
                "salary":60000
                },
                {
                "name":"Jenny",
                "salary":50000 
            }
    ]
    }); 

//題目三
function maxProduct(nums){
    // 請用你的程式補完這個函式的區塊 
    let resultarr = []
    for(let i=0;i<nums.length; i++){
        for(let j=0; j<nums.length; j++){
            if (j==i){
            continue
        }
    y=nums[i]*nums[j]
    resultarr.push(y)

    }
}
// console.log(resultarr);
let Z= Math.max.apply(null, resultarr)
console.log(Z);

}
        maxProduct([5, 20, 2, 6]) // 得到 120 
        maxProduct([10, -20, 0, 3]) // 得到 30 
        maxProduct([-1, 2]) // 得到 -2 
        maxProduct([-1, 0, 2]) // 得到 0 
        maxProduct([-1, -2, 0]) // 得到 2


//要求四 ( 請閱讀英文 ):演算法
//Given an array of integers, show indices of the two numbers such that they add up to a specific target.
//You can assume that each input would have exactly one solution, and you can not use the same element twice.
function twoSum(nums, target){
    let arr=[]; 
    // let b=[]
        for(let i=0;i<nums.length;i++){
            for(let j=0; j<nums.length; j++){
                if(nums[i]+nums[j]==target){
                    arr.push(i, j);
                }
            }
        }
        let newlist= new Set(arr);
        return newlist;
    }
let result=(twoSum([2, 11, 7, 15], 9));
console.log(result);