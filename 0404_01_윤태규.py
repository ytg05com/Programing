'''
    작성일 : 2024년 4월 4일
    작성자 : 컴퓨터공학부 202495011 윤태규
    설명 : 학점계산기1
            
    [문제분석]
        필요한 변수 : score (점수)
        점수가 90점에서 100 점 사이다
            =>  1) 90 <= score <=100
            =>  2) (score >= )
            F 학점은 나머지 (else) 로 처리한다
                
    [알고리즘]
        1. 점수를 입력받는다.
        2. 만약 점수가 90~100 점 사이라면 A를 표시한다
        3. 

'''
score = int(input("점수를 입력하세요 : "))

if 90 <= score <= 100 :
    print(f"{score}점은 A학점 입니다.")

elif 80 <= score <= 89 :
    print(f"{score}점은 B학점 입니다.")
    
elif 70 <= score <= 79:
    print(f"{score}점은 C학점 입니다.")
    
elif 60 <= score <= 69 :
    print(f"{score}점은 D학점 입니다.")
    
elif 50 <= score <= 59 :
    print(f"{score}점은 F학점 입니다.")

else :
    print("잘못된 점수를 입력하셨습니다.")