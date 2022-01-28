# WEEK-5 Assignment

### **要求三:SQL CRUD**

- 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午5.30.12.png)

- 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午5.30.37.png)


- 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午6.07.26.png)

- 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午8.15.36.png)

- 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
**注意** 為了顯示資料有別，會員資料的username跟password有重新刪改過，僅有mike跟john有包含"test", 其他成員皆無
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午11.08.47.png)
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午8.30.34.png)

- 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午8.31.04.png)

- 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位
改成 test2。
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午8.34.55.png)

### **要求四:SQL Aggregate Functions 利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令**
-  取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午8.41.19.png)
-  取得 member 資料表中，所有會員 follower_count 欄位的總和。
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午8.43.50.png)
-  取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午8.44.24.png)

### **要求五：SQL JOIN (Optional)**
- 在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定:
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午11.44.10.png)
- 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-27%20下午11.55.37.png)
- 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
![Alt text](https://raw.githubusercontent.com/yin0110/wehelp-assignments/week-5/截圖%202022-01-28%20上午11.34.52.png)
