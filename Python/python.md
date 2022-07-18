# Python 0718-

- 기타
    
    ![api](/Users/song-yuojin/Desktop/SSAFY/Python/Python.png)
    
    API: 기능 ex) url끝에 원하는 값 알려줘
    

## 프로그래밍

- 프로그램을 만드는 행위

- 특정 작업을 수행하는 일련의 명령어들의 모임

- 컴퓨터는 2진법(기계어)만 인식 가능

- 프로그래밍 언어 → 인터프리터 → 기계어

## 파이썬을 사용하는 이유

- 쉬움
- 인터프리터 언어
- 객체 지향 프로그래밍

## IDE (Integrated development environment)

- 통합 개발 환경
- ex. Visual Studio code, Pycharm, Jupyter Notebook

## 스타일 가이드

- 한줄에 79자까지
- ‘문자열’(o)  “문자열”(x)
- space 4번 > tab ; 혼용 금지
- #한줄 주석, ‘’’여러줄 주석’’’(””” 사용 가능)

## 변수

- 데이터를 받는 상자
- 코드의 가독성 증가
- 수정 용이
- 값 여러개를 동시 할당 가능
- 변수 값 바꿔서 저장
    
    ```python
    x, y = 10, 20
    tmp = x
    x = y
    y = tmp
    print(x, y) # 20, 10
    ```
    
    ```python
    x, y = 10, 20
    y, x = x, y
    print(x, y) # 20 10
    ```
    
- 식별자
    - 영어, _ , 숫자 구성
    - 첫글자 숫자 x
    - 길이 제한 x, 대소문자 구별
    - import keyword의 keywords는 사용 불가
    - 내장 함수, 모듈 이름 x
- 연산자
    - +, -, *, /, //, **
- 자료형
    - 수치형 - int, float, 진수, 부동 소수점(해결: import math)
    - 문자열 - str, ‘, ‘’, \n, \t, \r(캐리지 리턴), \0(Null), \\(\), \’, \”(인용부호)
    
    ```python
    print("문자열 안에 '작은따옴포'를 사용하려면 큰따옴표로 묶음")
    print('문자열 안에 "큰따옴포"를 사용하려면 작은따옴표로 묶음')
    print('''문자열 안에 '작은따옴표'나 "큰따옴표"를 사용할 수 있고
    여러줄을 사용할 때도 편리''')
    ```
    
    ```python
    name = 'Kim'
    score = 4.5
    
    # %-formatting
    print('Hello, %s' %name) # Hello, Kim
    print('성적은 %d' %score) # 성적은 4
    print('성적은 %f' %score) # 성적은 4.500000
    
    # str.format()
    print('Hello, {}! 성적은 {}'.format(name, score)) # Hello,Kim! 성적은 4.5
    
    # f-strings
    print(f'Hello, {name}! 성적은 {score}') # Hello,Kim! 성적은 4.5
    
    import datetime
    today = datetime.datetime.now()
    print(today) # 2022-07-18 11:30:15.200411
    print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일') #오늘은 22년 07월 18일
    
    pi = 3.141592
    print(f'원주율은 {pi:.3}, 반지름이 2인 원 넓이는 {pi*2*2}')
    # 원주율은 3.14, 반지름이 2인 원 넓이는 12.566368
    ```
    
    - None - 값이 없음을 표현, 반환 값이 없는 함수에서 사용
    - 불린형 - True, False/ 비교, 논리 연산에서 사용
        - 비교 연산자: <, >, < =, < =, ==, ! =, is, is not
        - 논리 연산자: and, nor, Not
            - Falsy: False는 아니지만 False로 취급되는 값 - 0, 0.0, (), [], {}, None, “”
            - 단축평가: and 연산 첫 값 False → False/ or 연산 첫 값 True → True
            
            ```python
            print(3 and 5) # 5
            print(0 and 3) # 0
            print(3 or 5) # 3
            print(0 or 5) # 5
            ```
            

## 컨테이너

- 여러 개의 값(데이터)을 담을 수 있는 것(객체)
- 서로 다른 자료형을 저장할 수 있음
- ex. List
- Ordered/ Unordered
- 순서가 있다 ≠ 정렬되어 있다
- 시퀀스형(ordered)
    - 리스트
        - [], list()
        - 리스트 안에 리스트 가능
        - 가변 자료형: 값 변경 가능
    - 튜플
        - (), tuple()
        - my_tuple[i] ; 인덱스로 접근 가능
        - 불변 자료형: 값 변경 불가
        - 단일 항목 - 생성 시 값 뒤에 ,(쉼표) 붙여야 함
        - 복수 항목 - 마지막 항목에 쉼표 없어도 되지만, **넣자**
    - 레인지(Range)
        - 숫자의 시퀀스를 나타내기 위해 사용
        - 주로 반복문과 함께 사용
        
        ```python
        print(list(range(3))) # [0, 1, 2]
        print(list(range(1, 5))) # [1, 2, 3, 4]
        # range(시작인덱스, 끝인텍스, 간격)
        print(list(range(1, 5, 2))) # [1, 3]
        print(list(range(6, 1, -1))) # [6, 5, 4, 3, 2]
        print(list(range(6, 1, -2))) # [6, 4, 2]
        print(list(range(6, 1, 1))) # []
        ```
        
        - 슬라이시 연산자: 문자열의 특정부분 자름 [인덱스 : 인덱스]
        
        ```python
        print([1, 2, 3, 5][1:4]) # [2,3,5]
        print((1, 2, 3)[:2]) # (1, 2)
        print(range(10)[5:7]) # range(5, 7)
        print('abcd'[2:4]) # cd
        print([1, 2, 3, 5][0:4:2]) # [1, 3]
        print(range(10)[1:5:3]) # range(1, 5, 3)
        print('abcdefg'[1:3:2]) # b
        print('abcd'[::-1]) # dcba 거꾸로 출력
        ```
        
- 비시퀀스형(unordered)
    - 셋(set)
        - {}, set()
        - 중복되는 요소 없는 데이터들의 묶음
        - 순서 없으므로 인덱스로 접근 불가능
        - 집합
        - 가변 자료형
        
        ```python
        print({1, 2, 3, 1, 2}) # {1, 2, 3}
        
        blank = {} # 빈 중괄호는 Dictionary
        print(type(blank)) # <class 'dict'>
        blank_set = set()
        print(type(blank_set)) # <class 'set'>
        ```
        
        - set 연산자 - |(합집합), &(교집합), -(차집합), ^(대칭차집합), 여집합 없음
        
        ```python
        a_set = {1, 2, 3, 4}
        b_set = {1, 2, 3, 'hello', (1, 2, 3)}
        print(a_set | b_set) # {1, 2, 3, 4, (1, 2, 3), 'hello')
        print(a_set & b_set) # {1, 2, 3}
        print(b_set - a_set) # {(1, 2, 3), 'hello'}
        print(a_set ^ b_set) # {'hello', 4, (1, 2, 3)} 합집합-교집합
        ```
        
    - 딕셔너리
        - {}, dict()
        - 키-값(key-value): key를 통해 value에 접근
        - 3.7ver. 부터 ordered
        - key: 변경 불가능한 데이터만 활용 가능(str, int, float, bool, tuple, range)
        - values: 어떤 형태는 상관 없음
        
        ```python
        dict_a = {}
        dict_b = dict()
        
        dict_a = {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
        print(dict_a) # {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
        print(dict_a['list']) # [1, 2, 3]
        
        dict_b = dict(a = 'apple', b = 'banana', list = [1, 2, 3])
        print(dict_b_ #{'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
        ```
        
    
- 형변환
    - 숫자 ↔ 문자
    - 암시적 형 변환(자동; 파이썬이 하면)
        - bool
        - Numeric type (int, float)
        
        ```python
        print(True + 3) # 4 True=1
        print(3 + 5.0) # 8.0
        ```
        
    - 명시적 형 변환(의도적; 개발자가 하면)
        - int
            - str, float ⇒ int (단, 형식에 맞는 문자열만 정수로 변환 가능)
            
            ```python
            print(int('3') + 4) # 7
            print('3' + str(4)) # 34
            ```
            
        - float
            - str, int ⇒ float
            
            ```python
            print(float('3')) # 3.0
            # float 형식이 아닌 경우 타입 변환 불가
            print(float('3/4') + 5.3) # ValueError: could not convert string to float: '3/4'
            ```
            
        - str
            - int, float, list, tuple, dict ⇒ str
            
            ```python
            print(str(1)) # 1
            print(str(1.0)) # 1.0
            print(str([1, 2, 3])) # [1, 2, 3]
            print(str((1, 2, 3))) # (1, 2, 3)
            print(str({1, 2, 3})) # {1, 2, 3}
            ```
            
        
        ![type.png](/Users/song-yuojin/Desktop/SSAFY/Python/Python)
