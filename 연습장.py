print('당신은 신입 모험가입니다. 이제 막 길드에 등록하여 마을에 도착했습니다. 이 마을에는 여관, 상점, 장비관리소가 있으며, 탐험을 위해 던전에도 들어갈 수 있습니다.')


import random

print(f'\n캐릭터 설정을 합니다. 이름을 정해주세요')
namae=input('이름:')
print(f'\n\n--캐릭터 소개--\n이름:{namae} \n소지금: 200\n힘: 20 \nhp: 200 \n경험치: 0 \n\n게임을 시작합니다.')
print('\n\n')


namae
power=2  #힘=power
hp=200
경험치=0
invent=[]
money=20000      #소지금 수정하기
buki=[]
bougyo=[]

#item{이름:종류:가격}
item={'회복약':{'종류':'소비품','가격':20,'power':0, 'hp':50},
      '단검':{'종류':'무기','가격':100,'power':5, 'hp':0},    
      '철검':{'종류':'무기','가격':200,'power':10, 'hp':0},
      '가죽 갑옷':{'종류':'방어구','가격':150,'power':0, 'hp':30},
      '강철 갑옷':{'종류':'방어구','가격':300,'power':0, 'hp':50} }
#몬스터{이름:hp:공격력:보상:아이템}
monster_slime={'레드 슬라임':{'hp':45,'공격력':10,'보상':5,'아이템':'회복약'},
               '그린 슬라임':{'hp':25,'공격력':5,'보상':3,'아이템':'가죽 갑옷'},
               '블랙 슬라임':{'hp':60,'공격력':15,'보상':8,'아이템':'강철 갑옷'},}
monster_goblin={'고블린 정철병':{'hp':60,'공격력':12,'보상':10,'아이템':'단검'},
               '고블린 도적':{'hp':55,'공격력':18,'보상':12,'아이템':'소지금 100g'},
               '고블린 대장':{'hp':80,'공격력':20,'보상':20,'아이템':'철검'},}
monster_ock={'오크 병사':{'hp':85,'공격력':18,'보상':18,'아이템':'가죽 갑옷'},
             '오크 궁수':{'hp':80,'공격력':22,'보상':20,'아이템':'철검'},
             '오크 병사':{'hp':85,'공격력':18,'보상':18,'아이템':'강철 갑옷'},}
                
             



while True:
    
    
    
    print(f'\n-- 메인 메뉴 --')
    print(f'1. 여관 \n2. 상점 \n3. 장비관리 \n4. 던전 탐험 \n5. 상태 보기 \n0. 종료 \n가고 싶은 곳의 번호를 입력해주세요.')
    main=int(input(f'번호:'))

    if main==0:
        print('게임을 종료합니다')
        break

    elif main==1:
        print(f'\n여관 입니다. 플레이어의 hp를 최대치로 회복합니다.')
        hp=200
        print(f'hp가 200으로 회복되었습니다. 메인 메뉴로 돌아갑니다.\n')
        continue
#여관 끝
    
    elif main==2:
   
        while True:
            print(f'\n상점 입니다. 번호를 선택 하십시요.\n1. 아이템 구매\n2. 아이템 판매\n0. 메인 메뉴')
            print(f'\n--현재 상태--\n인벤토리:{invent}\n소지금:{money}g\n힘:{power}\nhp:{hp}')
            store1=int(input('번호:'))

            if store1==1:
                while True:
                    print(f'\n구매 하실 아이템을 선택 하십시요.\n')
                    print(f'{'이름':^6}{'종류':^8}{'가격':^6}{'효과':^6}')
                    print(f'{'회복약':^6}{'소비품':^8}{'20g':^6} {'hp +50':^6}')
                    print(f'{'단검':^6}{'무기':^8} {'100g':^6} {'힘 +5':^6}')
                    print(f'{'철검':^6}{'무기':^8} {'200g':^6}  {'힘 +10':^6}')
                    print(f'{'가죽 갑옷':^4}{'방어구':^8}{'150g':^4}   {'hp +30':^6}')
                    print(f'{'강철 갑옷':^4}{'방어구':^8}{'300g':^4}   {'hp +50':^6}')
                    print('0 입력시 전 단계로 갑니다.')
                    store2=input('아이템 이름:')
                    if store2 in item:
                        if money>=item[store2]['가격']:       
                            invent.append(store2)
                            money-=item[store2]['가격']
                            
                            print(f"\n'{store2}'를 구매했습니다. \n인벤토리:{invent} \n소지금:{money}g")
                            continue
                        
                        elif money<item[store2]['가격']:
                            print('소지금이 부족합니다.\n현재 소지금:{money}g')
                            continue
                    elif store2=='0':
                        print('전 단계로 돌아갑니다.')
                        break
                    
                    else:
                        print('아이템 이름을 제대로 입력해 주세요.')
                        continue

                    
            elif store1==2:
                
                while True:
                    print(f'\n판매 하실 아이템을 선택 하십시요.')
                    print(f'인벤토리:{invent}')
                    print('0 입력시 전 단계로 갑니다.')
                    store3=input('아이템 이름:')
                    if store3 in invent:  
                        invent.remove(store3)
                        money+=item[store3]['가격']/2
                        print(f'{store3}을 판매하셨습니다. \n인벤토리:{invent} \n소지금:{money}g')
                        continue

                    elif store3=='0':
                        print('전 단계로 돌아갑니다.')
                        break

                    elif store3 not in invent:
                        print('해당 아이템은 소지 하고 있지 않습니다.')
                        continue
                    
                    
                    else:
                        print('아이템 이름을 제대로 입력해 주세요.')
                        continue
                    
            elif store1==0:
                print('메인 메뉴로 돌아갑니다.')
                break

            else:
                print('번호를 제대로 입력해 주세요.')
                continue
 #상점 끝
            
    elif main==3:
       
        while True:
            print('\n장비관리소 입니다. 무기/방어구 를 장착/해제 할 수 있습니다.')
            print(f'\n--현재 상태--\n인벤토리:{invent}\n착용 무기:{buki}\n착용 방어구:{bougyo}\n힘:{power}\nhp:{hp}')
            print(f'1. 장착\n2. 해제\n0. 메인 메뉴')
            kannri1=input('번호 입력:')
            if kannri1=='1':
                print(f'\n--현재 상태--\n인벤토리:{invent}\n착용 무기:{buki}\n착용 방어구:{bougyo}\n힘:{power}\nhp:{hp}')
                print('장착할 아이템의 이름을 입력해주세요. 0 입력시 전 단계로 갑니다.')
                kannri2=input('아이템 이름:')
                if  kannri2=='0':
                    print('전 단계로 돌아갑니다.')
                    break
                elif item[kannri2]['종류']=='무기': 
                    if len(buki)==0:
                        buki.append(kannri2)
                        hp+=item[kannri2]['hp']
                        power+=item[kannri2]['power']
                        print(f'무기가 장착 되었습니다.')
                        continue
                    else:
                        print('무기는 1개만 착용 가능 합니다.')
                        continue
                elif item[kannri2]['종류']=='방어구':
                    if len(bougyo)==0:
                        bougyo.append(kannri2)
                        hp+=item[kannri2]['hp']
                        power+=item[kannri2]['power']
                        print(f'방어구가 장착 되었습니다.')
                        continue
                    else:
                        print('방어구는 1개만 착용 가능 합니다.')
                        continue
                
                elif kannri2=='회복약':
                    print('회복약은 던전 탐험 중 사용 가능합니다.')
                    continue
                else:
                    print('아이템을 제대로 입력해 주세요.')
                    continue
                
            elif kannri1=='2':
                print(f'\n--현재 상태--\n인벤토리:{invent}\n착용 무기:{buki}\n착용 방어구:{bougyo}\n힘:{power}\nhp:{hp}')
                print('해제할 아이템의 이름을 입력해주세요. 0 입력시 전 단계로 갑니다.')
                kannri3=input('아이템 이름:')
                if kannri3 in buki:
                    buki.remove(kannri3)
                    hp-=item[kannri3]['hp']
                    power-=item[kannri3]['power']
                    print(f'무기가 해제 되었습니다.')
                    continue
                elif kannri3 in bougyo:
                    bougyo.remove(kannri3)
                    hp-=item[kannri3]['hp']
                    power-=item[kannri3]['power']
                    print(f'방어구가 해제 되었습니다.')
                    continue
                elif kannri3=='0':
                    print('전 단계로 돌아갑니다.')
                    break
                else:
                    print('착용 하고 있는 아이템을 입력해 주세요.')
                    continue
            elif kannri1=='0':
                print('메인 메뉴로 돌아갑니다.')
                break
            else:
                print('번호를 제대로 입력해 주세요.')
                continue
                
                    
                
#확인 해보고 4로 넘어가기 아뇨 그냥 넘어갈게요... 여긴 무조건 try 구문을 써야 하는 부분 인듯함.
            #그 조건 너무 다양한 폼으로 있어서 그러니 일단 넘어감

    elif main==4:
        print('\n던전입니다. 탐험할 던전을 선택해 주세요.')
        print('1. 슬라임 동굴\n2. 고블린 숲\n3. 오크 요새\n0. 메인 메뉴')
        stage=input('번호:')
        if stage=='0':
            print('메인 메뉴로 돌아갑니다.')
            break
        
        elif stage=='1':
            print('\n--슬라임 동굴--\n몬스터와 대전하여 승리시 경험치 10을 얻습니다.')
            
            monster_slime1=random.choice(list(monster_slime))
            print(f"{monster_slime1}이 등장했다! {monster_slime1}  hp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}") 
            print(f'전투를 시작합니다.')

            i=0
            while True:     
                i+=1   
              
                print(f'\n{i}번째 전투')

                if  monster_slime[monster_slime1]['hp']<=0:
                    경험치+=10
                    print(f'\n전투에서 승리하였습니다.\n경험치가 쌓였습니다. 현재 경험치:{경험치}' )
                    print('메인 화면으로 이동합니다.')
                    break
                elif hp<=0:
                    print('전투에서 패배하였습니다. 자동으로 메인화면으로 이동합니다.')
                    break
                else:
                    print(f'\n현재 {monster_slime1} \nhp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}')
                    print(f'현재 나\nhp:{hp}, 공격력:{power}')
                    print('\n전투를 계속 하시겠습니까?\n1. 네\n2. 아니요')
                    fight=input("번호:")
                    if fight=='1':
                        if monster_slime[monster_slime1]['공격력']-power>0:
                            print(f'\n현재 {monster_slime1} \nhp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}')
                            print(f'{monster_slime1})의 공격력이 나의 공격력보다 {monster_slime[monster_slime1]['공격력']-power}만큼 큽니다. 나는 {monster_slime[monster_slime1]['공격력']-power}만큼 데미지를 입습니다.')
                            hp-=monster_slime[monster_slime1]['공격력']-power
                            continue
                        elif monster_slime[monster_slime1]['공격력']-power<=0:
                            print(f'\n현재 {monster_slime1} \nhp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}')
                            print(f'{monster_slime1}의 공격력이 나의 공격력보다 {power-monster_slime[monster_slime1]['공격력']}만큼 작습니다. 몬스터는 {power-monster_slime[monster_slime1]['공격력']}만큼 데미지를 입습니다.')
                            monster_slime[monster_slime1]['hp']-=power-monster_slime[monster_slime1]['공격력']
                            continue
                    elif fight=='2':
                        print('\n전투를 종료합니다.')
                        break
                    else:
                        print('번호를 다시 입력해주세요.')
                        continue
        elif stage=='2':
            print('\n--고블린 숲--\n몬스터와 대전하여 승리시 경험치 10을 얻습니다.')
            
            monster_slime1=random.choice(list(monster_slime))
            print(f"{monster_slime1}이 등장했다! {monster_slime1}  hp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}") 
            print(f'전투를 시작합니다.')

            i=0
            while True:     
                i+=1   
              
                print(f'\n{i}번째 전투')

                if  monster_slime[monster_slime1]['hp']<=0:
                    경험치+=10
                    print(f'\n전투에서 승리하였습니다.\n경험치가 쌓였습니다. 현재 경험치:{경험치}' )
                    print('메인 화면으로 이동합니다.')
                    break
                elif hp<=0:
                    print('전투에서 패배하였습니다. 자동으로 메인화면으로 이동합니다.')
                    break
                else:
                    print(f'\n현재 {monster_slime1} \nhp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}')
                    print(f'현재 나\nhp:{hp}, 공격력:{power}')
                    print('\n전투를 계속 하시겠습니까?\n1. 네\n2. 아니요')
                    fight=input("번호:")
                    if fight=='1':
                        if monster_slime[monster_slime1]['공격력']-power>0:
                            print(f'\n현재 {monster_slime1} \nhp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}')
                            print(f'{monster_slime1})의 공격력이 나의 공격력보다 {monster_slime[monster_slime1]['공격력']-power}만큼 큽니다. 나는 {monster_slime[monster_slime1]['공격력']-power}만큼 데미지를 입습니다.')
                            hp-=monster_slime[monster_slime1]['공격력']-power
                            continue
                        elif monster_slime[monster_slime1]['공격력']-power<=0:
                            print(f'\n현재 {monster_slime1} \nhp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}')
                            print(f'{monster_slime1}의 공격력이 나의 공격력보다 {power-monster_slime[monster_slime1]['공격력']}만큼 작습니다. 몬스터는 {power-monster_slime[monster_slime1]['공격력']}만큼 데미지를 입습니다.')
                            monster_slime[monster_slime1]['hp']-=power-monster_slime[monster_slime1]['공격력']
                            continue
                    elif fight=='2':
                        print('\n전투를 종료합니다.')
                        break
                    else:
                        print('번호를 다시 입력해주세요.')
                        continue

        elif stage=='3':
            print('\n--오크 요새--\n몬스터와 대전하여 승리시 경험치 10을 얻습니다.')
            
            monster_slime1=random.choice(list(monster_slime))
            print(f"{monster_slime1}이 등장했다! {monster_slime1}  hp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}") 
            print(f'전투를 시작합니다.')

            i=0
            while True:     
                i+=1   
              
                print(f'\n{i}번째 전투')

                if  monster_slime[monster_slime1]['hp']<=0:
                    경험치+=10
                    print(f'\n전투에서 승리하였습니다.\n경험치가 쌓였습니다. 현재 경험치:{경험치}' )
                    print('메인 화면으로 이동합니다.')
                    break
                elif hp<=0:
                    print('전투에서 패배하였습니다. 자동으로 메인화면으로 이동합니다.')
                    break
                else:
                    print(f'\n현재 {monster_slime1} \nhp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}')
                    print(f'현재 나\nhp:{hp}, 공격력:{power}')
                    print('\n전투를 계속 하시겠습니까?\n1. 네\n2. 아니요')
                    fight=input("번호:")
                    if fight=='1':
                        if monster_slime[monster_slime1]['공격력']-power>0:
                            print(f'\n현재 {monster_slime1} \nhp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}')
                            print(f'{monster_slime1})의 공격력이 나의 공격력보다 {monster_slime[monster_slime1]['공격력']-power}만큼 큽니다. 나는 {monster_slime[monster_slime1]['공격력']-power}만큼 데미지를 입습니다.')
                            hp-=monster_slime[monster_slime1]['공격력']-power
                            continue
                        elif monster_slime[monster_slime1]['공격력']-power<=0:
                            print(f'\n현재 {monster_slime1} \nhp:{monster_slime[monster_slime1]['hp']}, 공격력:{monster_slime[monster_slime1]['공격력']}')
                            print(f'{monster_slime1}의 공격력이 나의 공격력보다 {power-monster_slime[monster_slime1]['공격력']}만큼 작습니다. 몬스터는 {power-monster_slime[monster_slime1]['공격력']}만큼 데미지를 입습니다.')
                            monster_slime[monster_slime1]['hp']-=power-monster_slime[monster_slime1]['공격력']
                            continue
                    elif fight=='2':
                        print('\n전투를 종료합니다.')
                        break
                    else:
                        print('번호를 다시 입력해주세요.')
                        continue


        elif stage=='0':
            print('메인 메뉴로 돌아갑니다.')
            break
        else:
            print('번호를 다시 입력해주세요.')
            continue
                    
                    #사실 뒤로가기에사 던전 선택이 아닌 아예 메인메뉴로 나가기는 해

    elif main==5:
        print('현재 상태를 확인합니다.')
        print('\n--',namae,"의 현재 상태--\n",'힘:',power,'\nhp:',hp,'\n경험치:',경험치,'\n인벤토리:',invent,'\n소지금:',money)
        print('\n자동으로 메인메뉴로 이동합니다.')
        break
    elif main==0:
        print('게임을 종료합니다.')
        

















                
            
            
            
            
            
            
 

 
        
            
        
            
                        

                        
                        
                        
                
                    
                    

                
                

            
