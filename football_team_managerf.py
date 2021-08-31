import mysql.connector
import csv
import os

list_of_skills = ['Shooting','Heading','Speed','Physical','Defending','Passing']

headings = ['Name','Age','Gender','Height','Weight','Mobile Number','Shooting','Heading','Speed','Physical','Defending','Passing']


def check_headings():
    inner_csv_file = open('player_index.csv', 'r', newline='')
    reader = csv.reader(inner_csv_file)
    records = []
    for row in reader:
        records.append(row)
    if len(records) == 0:
        write_csv_file = open('player_index.csv', 'w', newline='')
        writer = csv.writer(write_csv_file)
        writer.writerow(headings)
        write_csv_file.close()
    inner_csv_file.close()


def apply_for_team():

    name = input("Enter Full Name : ")
    age = int(input("Enter Age : "))
    gender = input("Enter Gender : ")
    height = input("Enter Height : ")
    weight = input("Enter Weight : ")
    phone_no = input("Enter Mobile Number : ")

    player_data = [name, age, gender, height, weight, phone_no]

    for i in range(0, len(list_of_skills)):
        skill = print("Rate Yourself out of 10 for the Skill : ", list_of_skills[i])
        point_for_skill = int(input("Enter Points : "))
        player_data.append(point_for_skill)

    try:
        csv_file = open('player_index.csv', 'a+', newline='')
        writer = csv.writer(csv_file)
        try:
            check_headings()
            writer.writerow(player_data)
            csv_file.close()
            print("Player Added, You will be Called if selected \n Thank you for Applying ")
        except:
            print("Error! couldn't add Player!\n Please try later!")
    except:
        print("Error! Couldn't find file!")



def team_member_add(name , age ,gender,height,weight,phone_no):
    try:
        db_connect = mysql.connector.connect(user='root', passwd='toor', host='localhost', database='football_team_manager')
        cursor = db_connect.cursor()
        try:
            cursor.execute('insert into football_team(Name,Age,Gender,Height,Weight,Phone_no) values("{}",{},"{}","{}",{},{});'.format(name,age,gender,height,weight,phone_no))
            db_connect.commit()
            print('Player added!!')
        except :
            print('!!!Member could  not be added!!!')
    except:
        print('!!!Connection Error!!!')


def team_member_view():
    try:
        db_connect = mysql.connector.connect(user='root', passwd='toor', host='localhost', database='football_team_manager')
        cursor = db_connect.cursor()
        cursor.execute('SELECT * FROM football_team;')
        res=cursor.fetchall()
        if res:
            print("TEAM")
            print('(Name,Age,Gender,Height,Weight,Phone Number)')
            for player in res:
                print (player)
        else:
            db_connect.rollback()
            print('No Player Added yet!')
            db_connect.close()
    except:
        print('!!!Connection Error!!!')

def team_member_remove(name):
    try:
        db_connect = mysql.connector.connect(user='root', passwd='toor', host='localhost', database='football_team_manager')
        cursor = db_connect.cursor()
        try:
            cursor.execute('delete from football_team where name = "{}";'.format(name))
            db_connect.commit()
            print( 'Player',name,'Removed From team')
        except:
            db_connect.rollback()
            print('!!!Member could  not be added!!!')
            db_connect.close()
    except:
        print('!!!Connection Error!!!')

#main
print(r'''
  ______                       __      __                  __  __          __                                       
 /      \                     |  \    |  \                |  \|  \        |  \                                      
|  $$$$$$\ ______    ______  _| $$_   | $$____    ______  | $$| $$       _| $$_     ______    ______   ______ ____  
| $$_  \$$/      \  /      \|   $$ \  | $$    \  |      \ | $$| $$      |   $$ \   /      \  |      \ |      \    \ 
| $$ \   |  $$$$$$\|  $$$$$$\\$$$$$$  | $$$$$$$\  \$$$$$$\| $$| $$       \$$$$$$  |  $$$$$$\  \$$$$$$\| $$$$$$\$$$$\
| $$$$   | $$  | $$| $$  | $$ | $$ __ | $$  | $$ /      $$| $$| $$        | $$ __ | $$    $$ /      $$| $$ | $$ | $$
| $$     | $$__/ $$| $$__/ $$ | $$|  \| $$__/ $$|  $$$$$$$| $$| $$        | $$|  \| $$$$$$$$|  $$$$$$$| $$ | $$ | $$
| $$      \$$    $$ \$$    $$  \$$  $$| $$    $$ \$$    $$| $$| $$         \$$  $$ \$$     \ \$$    $$| $$ | $$ | $$
 \$$       \$$$$$$   \$$$$$$    \$$$$  \$$$$$$$   \$$$$$$$ \$$ \$$          \$$$$   \$$$$$$$  \$$$$$$$ \$$  \$$  \$$''')

user = int(input('Enter code to select user type : \n 1 >> Apply for Team \n 2 >> Team Manager \n'))
if user == 1:
    apply_for_team()
if user == 2:
    password = input('Enter Team password : ')
    if password == 'football':
        try:
            os.startfile('player_index.csv')
        except:
            print('NO players Registered!!!')
        while True:
            op_num = int(input('Enter code to perform operation :\n 1 >> Add members to the Team \n 2 >> View Team '
                            'members \n 3 >> Delete Team Member details \n 4 >> Exit \n'))
            if op_num == 1:
                nam = input('Enter the name of the team member :')
                age = int(input('Enter the age of the team member :'))
                gender = input('Enter the gender of the team member :')
                height = input('Enter the height of the team member :')
                weight = int(input('Enter the weight of the team member :'))
                phone_no = int(input('Enter the Phone Number of the team member :'))
                team_member_add(nam, age, gender,height, weight, phone_no)
            elif op_num == 2:
                team_member_view()
            elif op_num == 3:
                nam = input('Enter the name of the team member to delete:')
                team_member_remove(nam)
            elif op_num == 4:
                break
        else:
            print('!!!Wrong Code Entered!!!')
    else:
        print('!!!Wrong credentials entered!!!')
else:
    exit()


