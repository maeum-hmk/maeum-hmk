text1=input('복사할 텍스트 파일의 주소:')
text1_name=input('복사할 텍스트 파일의 이름:')
text2=input('붙여넣을 텍스트 파일의 주소:')
text2_name=input('붙여넣을 텍스트 파일의 이름:')

copyfile=text1+'/'+text1_name+'.txt'
pastefile=text2+'/'+text2_name+'.txt'


import shutil

shutil.copy(copyfile,pastefile) #사용자값을 받은 변수는 그냥. ''없이
print('복사가 완료 되었습니다.')
print('복사한 내용을 확인하겠습니까?')
check=input('예/아니요:')
str=[]

if check=='예':
    file=open(copyfile,'r',encoding='utf-8') #마찬가지로 사용자값을 받은변수는 그냥. ''없이
    str=file.readlines()
    print(str)
else:
    print('프로그램을 종료합니다.')

