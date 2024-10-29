import time
print("\n--- 人事資料管理系統 ---\n1. 新增資料\n2. 查詢資料\n3. 修改資料\n4. 刪除資料\n5. 顯示所有資料\n6. 退出系統\n------------------------")

data_list = []

def functions_1():
    while True:
        dpt = input("請輸入部門 : ")
        nm = input("請輸入姓名 : ")
        ages = input("請輸入年齡 : ")
        phnum = input("請輸入手機號碼 : ")

        data = {
            "department": dpt,    # 部門資料
            "name": nm, # 姓名資料
            "age": ages,    # 年齡資料
            "phone_number": phnum   # 電話資料
        }
        data_list.append(data)  #存入

        yorn = input("是否繼續輸入資料? (y/n) ")

        if yorn == "y" or yorn == "Y":
            continue
        elif yorn == "n" or yorn == "N":
            break

def function_2():
    srhnm =input("請輸入要查詢的姓名 : ")

    for i in data_list:
        if i["name"] == srhnm:
            print("\n----- 查詢結果 -----\n部門\t\t姓名\t年齡\t號碼")
            print(f"{i['department']:<5} {i['name']:<5} {i['age']:<5} {i['phone_number']}")
        elif i["name"] != srhnm:
            print("查無此人\n")

def function_3():
    srh = input("輸入要修改的名字 : ")
    #尋找要求修改的名字
    for i in data_list:
        if i["name"] == srh:
            #原資料
            print("\t 當前資料\n部門\t姓名\t年齡\t號碼\n----------------------------")
            print(f"{i['department']:<5} {i['name']:<5} {i['age']:<5} {i['phone_number']}")  #當前資料
            print("1. 修改部門\n2. 修改姓名\n3. 修改年齡\n4. 修改號碼")
            rve = input("請選則要修改的欄位 : ")
            #修改資料
            if  rve == '1':
                i["department"] = input("請輸入新的部門: ")
            elif rve == '2':
                i["name"] = input("請輸入新的姓名: ")
            elif rve == '3':
                i["age"] = input("請輸入新的年齡: ")
            elif rve == '4':
                i["phone_number"] = input("請輸入新的手機: ")
            else:
                print("無效選項。")

            #更新資料
            print("-----更新後的資料-----\n部門\t姓名\t年齡\t號碼\n---------------------------------------\n")
            print(f"{i['department']:<5} {i['name']:<5} {i['age']:<5} {i['phone_number']}")
        else :
            print("查無此人")

def function_4():
    dltnm = input("請輸入要刪除的姓名 : ")

    for i in data_list:
        if i["name"] == dltnm:
            data_list.remove(i)
            print("已刪除\t" + dltnm)
        else:
            print("查無此人")

#main
while True :
    fns = input("請選擇功能 : ")
    if fns == '1':  #input data___ 1    ok
        functions_1()
        continue
    elif fns == '2':    #search specify___2 ok
        function_2()
    elif fns == '3':    #revise data___3    ok
        function_3()
    elif fns == '4':    #delete data___4
        function_4()
    elif fns == '5':    #print all data____ 5   ok
        if not data_list:
            print("目前無任何資料")
        else:
            print("部門\t姓名\t年齡\t號碼\n-----------------------------------")
            for i in data_list:
                print(f"{i['department']:<5}  {i['name']:<5} {i['age']:<5} {i['phone_number']}")

    elif fns == '6':    #exit____6  ok
        print("\n退出中...")
        time.sleep(1)
        print("\n已退出")
        break
#11