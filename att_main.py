"""
Author :Shivang
Date:12/4/20
Purpose:Attendance management program
Completed  on :13/4/20
"""

import mysql.connector

mydb = mysql.connector.connect(user='shivangbagri', password='hivang26', database='wisdom',
                               auth_plugin="mysql_native_password", autocommit=True)

cur = mydb.cursor()
pwd = "welcome"

in_pwd = input("Enter password to access the records ")
while in_pwd != pwd:
    in_pwd = input("Enter correct password please! ")
if in_pwd == pwd:
    print("Logined Successfully! ")
    while True:
        print("1: Show attendance table\n2: Show details of particular student\n3: Update records\n"
              "4: Exit\n")
        choice = int(input("Enter your choice "))
        if choice == 1:
            cmd = "select* from attendance"
            cur.execute(cmd)
            result = cur.fetchall()
            print("|     Name   |", 'Roll_no|', 'Father_name|', 'Phone_no|', 'Monday|', 'Tuesday|', 'Wednesday|')
            for name in result:
                print(name)
        elif choice == 2:
            name = input("Enter student's name ")
            roll = input("Enter student's roll no. ")
            cmd = "select* from attendance where Name='" + name + "' and Roll_no='" + roll + "'"
            cur.execute(cmd)
            pot = cur.fetchone()
            if pot is not None:  # or cur.rowcount==1
                cmd = "select* from attendance where Name='" + name + "' and Roll_no='" + roll + "'"
                cur.execute(cmd)

                result = cur.fetchall()
                print("Name |", 'Roll_no |', 'Father_name |', 'Phone_no |', 'Monday |', 'Tuesday |', 'Wednesday |')
                for i in result:
                    print(i)
            else:
                print("No such Student ")
        elif choice == 3:
            # name = input("Enter student's name ")
            # roll = input("Enter student's roll no. ")
            while True:
                change = int(input(
                    "What do you want to update? \n1:Students_Name\n2:Roll_No\n3:Father_Name\n4:Phone_no\n"
                    "5:Add Details\n6: Exit from upgrade menu\n"))
                if change == 1:
                    roll = input("Enter student's roll no. ")
                    prv_name = input("Enter student's existing name ")
                    new_name = input("Enter student's new name ")
                    cmd = "update Attendance set  Name= '" + new_name + "' where Roll_no='" + roll + "' and Name='" \
                          + prv_name + "'"
                    cur.execute(cmd)
                    pot = cur.fetchone()
                    if cur.rowcount == 1:
                        cmd = "update Attendance set  Name= '" + new_name + "' where Roll_no='" + roll + "' and Name='" \
                              + prv_name + "'"
                        cur.execute(cmd)
                        print("Upgraded successfully")
                    else:
                        print("No such student ")
                elif change == 2:
                    name = input("Enter student's name ")
                    prv_rollno = int(input("Enter student's existing roll_no "))
                    new_rollno = int(input("Enter student's new roll_no "))
                    cmd = "update Attendance set Roll_No= '" + str(new_rollno) + "' where Roll_no='" + str(
                        prv_rollno) + "' and Name='" + name + "'"
                    cur.execute(cmd)
                    pot = cur.fetchone()
                    if cur.rowcount == 1:
                        cmd = "update Attendance set Roll_No= '" + str(new_rollno) + "' where Roll_no='" + str(
                            prv_rollno) + "' and Name='" + name + "'"
                        cur.execute(cmd)
                        print("Upgraded successfully")
                    else:
                        print("No such student  ")

                elif change == 3:
                    name = input("Enter student's name ")
                    prv_fname = input("Enter student's existing Fathers Name ")
                    new_fname = input("Enter student's new Fathers name ")
                    cmd = "update Attendance set Fathers_Name= '" + str(new_fname) + "' where Fathers_Name='" + str(
                        prv_fname) + "' and Name='" + name + "'"
                    cur.execute(cmd)
                    pot = cur.fetchone()
                    if cur.rowcount == 1:
                        cmd = "update Attendance set Fathers_Name= '" + new_fname + "' where Fathers_Name='" + prv_fname \
                              + "' and Name='" + name + "'"
                        cur.execute(cmd)
                        print("Upgraded successfully")
                    else:
                        print("No such student  ")
                elif change == 4:
                    name = input("Enter student's name ")
                    prv_pno = int(input("Enter student's existing Phone no. "))
                    new_pno = int(input("Enter student's new Phone No. "))
                    cmd = "update Attendance set Phone_no= '" + str(new_pno) + "' where Phone_no='" + str(
                        prv_pno) + "' and Name='" + name + "'"
                    cur.execute(cmd)
                    pot = cur.fetchone()
                    if cur.rowcount == 1:
                        cmd = "update Attendance set Phone_no= '" + str(new_pno) + "' where Phone_no='" + str(prv_pno) \
                              + "' and Name='" + name + "'"
                        cur.execute(cmd)
                        print("Upgraded successfully")
                    else:
                        print("No such student  ")

                elif change == 5:
                    print("You are about to add new details... ")
                    name = input("Enter student's name ")
                    roll = int(input("Enter student's roll no. "))
                    fname = input("Enter student's Fathers name  ")
                    pno = int(input("Enter student's Phone no. "))
                    mon = input("Enter student's Monday Attendance ")
                    tue = input("Enter student's Tuesday Attendance ")
                    wed = input("Enter student's  Wednesday Attendance ")
                    cmd = "insert into attendance values('" + name + "','" + str(roll) + "','" + fname + "','" + str(
                        pno) + "','" + mon + "','" + tue + "','" + wed + "')"
                    cur.execute(cmd)
                    print("Successfully added , Do you want to see details?(y/n)  ")
                    temp = input("Enter your choice (y/n) ")
                    if temp == 'y':
                        cmd = "select* from attendance"
                        cur.execute(cmd)
                        result = cur.fetchall()
                        print("Name |", 'Roll_no |', 'Father_name |', 'Phone_no |', 'Monday |', 'Tuesday |',
                              'Wednesday |')
                        for name in result:
                            print(name)
                    else:
                        print("Logged out ")
                elif change == 6:
                    print("Upgrade menu closed!")
                    break
        elif choice == 4:
            print("Logged out!, Thanks for visiting ")
            break
