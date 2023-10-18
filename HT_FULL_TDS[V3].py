import requests,base64,os,sys
from time import strftime,sleep
from pystyle import System
try:
	import requests
except:
	os.system("pip install requests")
	import requests
try:
	from pystyle import Colors, Colorate, Write, Center, Add, Box
except:
	os.system("pip install pystyle")
	from pystyle import Colors, Colorate, Write, Center, Add, Box
do="\033[1;31m"
xanh_lam="\033[1;32m"
vang="\033[1;33m"
xn="\033[1;34m"
tim="\033[1;35m"
blue="\033[1;36m"
trang="\033[1;97m"
nenden = "\033[40m"
nendo  = "\033[41m"
nenxanhla = "\033[42m"
nencam = "\033[43m"
nenxanhduong = "\033[44m"
nentim = "\033[45m"
nenxanhduongnhat = "\033[46m" 
################################ quan ly 24/h
time=int(strftime("%d%m"))
name=requests.get('https://hoangsontung.000webhostapp.com/admin-tool/QUAN_LY_KEY24').text
key1=str(time*10*14+2024)
key24 =f'{name+key1}2023'
##############quang cao 
exec(requests.get('https://hoangsontung.000webhostapp.com/admin-tool/chen_quang_cao[v3]').text)
System.Clear();
########################################### logo 
exec(requests.get('https://hoangsontung.000webhostapp.com/admin-tool/ADMIN_LOGO_JUSST').text)
#########################key vip
name_file_key='Key_tool_tds.txt' ## TEN FILE  CUA  KEY  
url = f'https://hoangsontung.000webhostapp.com/jusst/key.html?key='+key24
token_web1s = '7ff9cc84-0711-4b47-ad79-3dc34fa8308c'
web1s = requests.get(f'https://web1s.com/api?token={token_web1s}&url={url}').json()
if web1s['status']=="error": 
        print(web1s['message'])
        quit()       
else:
        link_key=web1s['shortenedUrl']      
###################################################################################### CODE THUAT TOAN ################################
def key_vip(key,link24):
     data={'key':key}
     url='https://hoangsontung.000webhostapp.com/CHECK.php'
     re=requests.post(url=url,data=data).json()
     if re['status']==False: 
        System.Clear();
        print(re['message'])
        print()
        sleep(3)
        print(blue,'Vui long Vuot Link:',trang,link24)
        key=input(xanh_lam+'Nhap_Key:')
        luu=open(name_file_key,'w')
        luu.write(key)
        luu.close();
        sleep(2)
        print(do,'Vui long chay lai:()')
        quit();
     else:
        sleep(2)
        print(re['message'])
        luu=open(name_file_key,'w')
        luu.write(key)
        luu.close()   
        
file_key=name_file_key
check_file_key=os.path.exists(file_key)
#file chua ton tai 
if check_file_key == False:
    print(blue,'Link Để Vượt Key Là: ',trang,link_key)
    key=input(xanh_lam+'Nhap key:')
    if key == key24:
        print(vang,'Key Đúng Mời Bạn Dùng Tool')
        ##tao file
        luu=open(file_key,'w')
        luu.write(key)
        luu.close()
    elif key != key24:
        
        key_vip(key,link_key);    
    else:
        print(do,"Key Sai Vui Lòng Vượt Link Lại",trang,link_key)
        quit();
#file ton tai       
if check_file_key == True:
    check_file_key=os.path.exists(file_key)
    mo=open(file_key,'r')
    doc=mo.read()
    mo.close() 
    if doc == key24:
        print(vang,'Key Đúng Mời Bạn Dùng Tool')
    elif doc!=key24:
        key_vip(doc,link_key);
        #exec(requests.get('https://hoangsontung.000webhostapp.com/admin-tool/ADMIN_TDS[02]').text)
    else:
        print(do,"Key Sai Vui Lòng Vượt Link Lại",link_key)
        quit();    
################################################################ START TOOL#####################################################

System.Clear();
print(trang,'LOADING....')
sleep(2)
exec(requests.get('https://hoangsontung.000webhostapp.com/admin-tool/gop_ADMIN_TDS[3]').text)