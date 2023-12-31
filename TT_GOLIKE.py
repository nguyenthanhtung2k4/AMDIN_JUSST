#  VISION  GOLIKE 2.1(UPLOAD BO QUA JOB  CMT vs CHECK MANG)
import requests
from colorama import Fore, Style
import json
import random
import re
import os, sys
import platform
from time import sleep
from pystyle import System

# Color codes
do = Fore.RED
xanh_lam = Fore.GREEN
vang = Fore.YELLOW
xn = Fore.BLUE
tim = Fore.MAGENTA
blue = Fore.CYAN
trang = Fore.WHITE
nenden = "\033[40m"
nendo = "\033[41m"
nenxanhla = "\033[42m"
nencam = "\033[43m"
nenxanhduong = "\033[44m"
nentim = "\033[45m"
nenxanhduongnhat = "\033[46m"
s = Style.RESET_ALL
######################## CHECK MANG###########################
def check_mang():
     re=requests.get('https://www.youtube.com/@HoangSonTungJusst',timeout=5)
     if re.status_code==200:
          return
     else:
          print(vang,"Vui Long Ket  noi  mang")
          print(do,":((")
          exit(); 
############################################### THUAT TOAN###############################################

def get_tiktok(au):
    he_golike = {
        'authority': 'gateway.golike.net',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': au,
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://app.golike.net',
    }
    try:
        re_golike = requests.get('https://gateway.golike.net/api/users/me', headers=he_golike).json()
        if re_golike['status'] != 200:
            print(f'{do}[!] Error: Invalid token')
            System.Clear()
            exit();
        else:
            print("ID:", re_golike['data']['id'])
            print("USER NAME:", re_golike['data']['username'])
            print("EMAIL:", re_golike['data']['email'])
            print(f'{vang}$$$:', re_golike['data']['coin'], " đồng")
    except Exception as e:
        print(f'{do}Error fetching user information:', str(e))

def job_tiktok(au, id_tiktok, delay):
    he_golike = {
        'authority': 'gateway.golike.net',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': au,
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://app.golike.net',   
    }
    try:
        data_job = {'account_id': id_tiktok}
        re_job = requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={id_tiktok}&data=null', headers=he_golike, data=data_job).json()

        if re_job['status'] != 200:
            print(f'{do}Error: Invalid account ID')
            print("Vui  long nhap lai Authorization")
            return

        if 'data' not in re_job or 'type' not in re_job['data']:
            print(f'{do}Unexpected response format. Check API compatibility.')
            return
        job_type = re_job['data']['type']
        link = re_job['data']['link']
        id_job = re_job['data']['id']
        object_id = re_job['data']['object_id']
        print(f'ID: {id_job} | {job_type.capitalize()}')
        data_bao_cao = {'ads_id': id_job, 'account_id': id_tiktok, 'async': 'true'}
        data_skip = {'ads_id': id_job, 'object_id': object_id, 'account_id': id_tiktok, 'type': job_type}
        if job_type not in ['follow', 'like']:
            print(f'{do}Unsupported job type: {job_type}')
            sleep(1)
            print(f'{xanh_lam}Đang chuyển job khác')
            sleep(1)
            re_skip = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs', json=data_skip, headers=he_golike).json()
            print(re_skip['message']) 
            return
        sleep(3)
        # Check HE THONG
        if platform.system() == "Android" or platform.system() == "Linux":
            os.system(f'xdg-open {link}')
        elif platform.system() == "Windows":
            os.system(f'cmd /c start {link}')
        else:
            print(f'{do}Hệ điều hành của bạn vẫn chưa được hỗ trợ\nLiên hệ ngay với Admin nhé!\n')
            exit();
        for x in range(delay, -1, -1):
            print("Delay: ", x, end=' \r')
            sleep(1)
        sleep(2)
        re_bao_cao = requests.post('https://dev.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=he_golike, json=data_bao_cao).json()

        if 'status' not in re_bao_cao:
            print(f'{do}Unexpected response format. Check API compatibility.')
            return

        if re_bao_cao['status'] == 400:
            print(re_bao_cao['message'])

            if 'message' in re_bao_cao and 'not enough coin' in re_bao_cao['message'].lower():
                print(f'{do}Not enough coins. Skipping job.')
                return

            sleep(4)
            re_skip = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs', json=data_skip, headers=he_golike).json()
            print(re_skip['message'])
        elif re_bao_cao['status'] == 200:
            print(f'{vang}SUCCESS +{re_bao_cao["data"]["prices"]} đ')
        else:
            print(f'{do}Error: {re_bao_cao.get("message", "Unknown error")}')
            print(f'{xanh_lam}Đang chuyển job khác')
            sleep(1)
            re_skip = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs', json=data_skip, headers=he_golike).json()
            print(re_skip['message'])  
    except Exception as e:
        print(f'{do}Error processing TikTok job:', str(e))
# ######################################## XU  LY FILE ##############################################################
def check_file_exist(file_path):
         return os.path.exists(file_path)

#  NAME  CAC FILE
file_au = 'authorization.txt'
file_acc = 'acc_golike.txt'
check_file_au = check_file_exist(file_au)
check_file_acc = check_file_exist(file_acc)

def read_file(file_path): # DOC FILE
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f'{do}Error reading file {file_path}:', str(e))
        return None

def write_file(file_path, data):# VIET FILE
    try:
        with open(file_path, 'w+') as file:
            file.write(data)
    except Exception as e:
        print(f'{do}Error writing to file {file_path}:', str(e))
def acc_tiktok(au):
        # au="Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3MDM0NzcxNjUsImV4cCI6MTczNTAxMzE2NSwibmJmIjoxNzAzNDc3MTY1LCJqdGkiOiJUMEZkOTBSUmZlV2RoQW16Iiwic3ViIjoyMDUyMjU0LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.dL6XV_a-TcnSFRFDgyetcmBmbq4DMBF41_JkpVnbR8Y"
        #user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        he_golike = {
                'authority': 'gateway.golike.net',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'Authorization': au,
                'T':'VFZSamQwMTZWVFZOUkUxNVRrRTlQUT09',
                'Content-Type': 'application/json;charset=utf-8',
                'Origin': 'https://app.golike.net',
        }
        check_mang();
        re=requests.get('https://gateway.golike.net/api/tiktok-account', headers=he_golike).json()
        id=[entry['id']for entry in re['data']]
        name=[entry2['nickname']for entry2 in re['data']]
        print(f'\n{tim}All  Account-TikTok')
        for x in  range (len(id)):
                print(f'{vang}Nhap[{x+1}]')
                print(f'{vang}ID: {id[x]}{trang}| Name: {name[x]}')
def tiktok(au,  id_tiktok):
        he_golike = {
                'authority': 'gateway.golike.net',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'Authorization': au,
                'T':'VFZSamQwMTZWVFZOUkUxNVRrRTlQUT09',
                'Content-Type': 'application/json;charset=utf-8',
                'Origin': 'https://app.golike.net',
        }
        check_mang();
        re=requests.get('https://gateway.golike.net/api/tiktok-account', headers=he_golike).json()
        id=[entry['id']for entry in re['data']]
        name=[entry2['nickname']for entry2 in re['data']]
        print(f'\n{tim}Account-TikTok')
        so=id_tiktok-1
        print(f'ID chay la: {id[so]}|{name[so]}')
        write_file(file_acc,str(id[so]))
if not (check_file_au  and check_file_acc):
    check_mang();
    au = input(f'{do}Nhap Authorization: ')
    write_file(file_au, au)
    print(f'{trang}====================================')
    acc_tiktok(au)
    id_tiktok = int(input(f'{xanh_lam}Nhap Lua Chon ID-TikTok: '))
    tiktok(au,id_tiktok)
else:
    print(s)
    System.Clear()
    check_mang();
    chon = input("[Y/N] Nhap lai Authorization\n>> ").upper()
    if chon == 'Y':
        au = input(f'{do}Nhap Authorization: ')
        write_file(file_au, au)
    doc_user = read_file(file_acc)
    print("\nID Tiktok Hien tai la:", doc_user)
    print("===========ACC TIKTOK KHAC===========")
    au=read_file(file_au)
    acc_tiktok(au)
    chon2 = input("\n[Y/N] Nhap lai ID_Tiktok\n>> ").upper()
    if chon2 == 'Y':
        id_tiktok = input(f'{xanh_lam}Nhap Lua Chon ID-TikTok: ')
        write_file(file_acc, id_tiktok)

# DOC DU LIEU FILE
read_au = read_file(file_au)
read_acc = read_file(file_acc)
while(True):
     try:
          nhiem_vu = int(input(f'{tim}Nhap so job: '))
          break;
     except :
          print('Nhap khong hop le(Nhap  lai)'.upper())
          nhiem_vu = int(input(f'{tim}Nhap so job: '))
################################################################### RUN NHIEM VU
while True:
    print(s)
    System.Clear()
    chon = int(input("[1]Delay co dinh\n[2]Delay random\n>> "))
    if chon == 1:
        System.Clear()
        delay = int(input("Nhap Delay co dinh\n>> "))
        # chay toool DELAY CO DINH
        System.Clear()
        print('\n\n')
        get_tiktok(read_au)
        print('\n')
        for i in range(nhiem_vu):
            print("Job ", i + 1)
          #    RUN NHIME VU
            job_tiktok(read_au, read_acc, delay)
        break
    elif chon == 2:
        System.Clear()
        try:
            delay_input = input("Nhap Dalay random(vd:10-20)\n>> ")
            xu_ly = re.match(r'(\d+)-(\d+)', delay_input)
        except:
            print("Vui lòng nhập không dấu cách (vd:20-30)")
            delay_input = input("Nhap Dalay random(vd:10-20)\n>> ")
            xu_ly = re.match(r'(\d+)-(\d+)', delay_input)
        # chay toool DELAY RANDOM
        System.Clear()
        print('\n\n')
        get_tiktok(read_au)
        print('\n')
        for i in range(nhiem_vu):
            print("Job ", i + 1)
            if xu_ly:
                so1, so2 = map(int, xu_ly.groups())
                ran = random.randint(so1, so2)
                delay = ran
            else:
                print(f'{do}So khong hop le'.upper())
                break
          #  RUN NHIEM VU
            job_tiktok(read_au, read_acc, delay)  
