sample_DB1 = ['벚꽃', '개나리', '단풍나무']
sample_DB2 = {'벚꽃':['축제1','축제2'], '개나리':['축제3','축제4'], '단풍나무':['축제5','축제6']}

func = int(input("개화 지도 제공 서비스를 원하시면 1번 축제 정보 제공 서비스를 원하시면 2번을 눌러주세요.>>>"))
if func == 1:
    while True:
        flower = input('서비스를 제공받길 원하는 꽃을 입력해주세요>>>')
        if flower in sample_DB1:
            #개화 지도 데이터 제공
            break
        else:
            print('DB에 해당 꽃이 없습니다')
if func == 2:
    while True:
        flower = input('서비스를 제공받길 원하는 꽃을 입력해주세요>>>')
        if flower in sample_DB1:
            print(sample_DB2[flower])   #축제 관련 세부 데이터도 함께 제공
            break
        else:
            print('DB에 해당 꽃이 없습니다')