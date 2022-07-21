# Python

# 데이터 저장

---

- 주소
    
    ![api](Python/API.png)
    
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

### 변수 값 바꿔서 저장

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

### 식별자

- 영어, _ , 숫자 구성
- 첫글자 숫자 x
- 길이 제한 x, 대소문자 구별
- import keyword의 keywords는 사용 불가
- 내장 함수, 모듈 이름 x

### 연산자

- +, -, *, /, //, **

```jsx
divmod(5, 2) # (2, 1) 5/2의 몫, 나머지
```

### 자료형

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
            - 단축평가가 되게 된 값을 반환함
        
        ```python
        print(3 and 5) # 5
        print(0 and 3) # 0
        print(3 or 5) # 3
        print(0 or 5) # 5
        ```
        

## 컨테이너

- 여러 개의 값(데이터)을 담을 수 있는 것(객체)
- 서로 다른 자료형을 저장할 수 있음
- Ordered/ Unordered
- 순서가 있다 ≠ 정렬되어 있다
- list>dict>range>tuple>set

![자료형](Python/type2.png)

➕ range: immutable

### 시퀀스형(ordered)

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
    - 불변 자료형
    
    ```python
    print(list(range(3))) # [0, 1, 2]
    print(list(range(1, 5))) # [1, 2, 3, 4]
    # range(start 시작인덱스, end 끝인덱스, step 간격)
    print(list(range(1, 5, 2))) # [1, 3]
    print(list(range(6, 1, -1))) # [6, 5, 4, 3, 2]
    print(list(range(6, 1, -2))) # [6, 4, 2]
    print(list(range(6, 1, 1))) # []
    ```
    
    - 슬라이스 연산자: 문자열의 특정부분 자름 [start 인덱스 : end 인덱스]
    
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
    

### 비시퀀스형(unordered)

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
    print(dict_b) # {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
    
    dict_a.keys() # key값만 가져옴
    dict_a.values() # value값만 가져옴
    ```
    

### 형변환

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
        
    
    ![type.png](Python/type.png)
    

# 데이터 처리

---

- 제어문
    - 조건문, 반복문
    - 순서도로 표현 가능
    - 기본적으로 위 → 아래로 명령 수행
    - 상황에 따라 선택적으로 실행(분기/조건/반복)하는 제어 필요

## 조건문

- 참/거짓을 판단할 수 있는 조건식 필요

```python
if num % 2: # if num % 2 == 1:
    print('홀수')
else:
    print('짝수')
```

### 복수 조건문

- elif 사용

### 중첩 조건문

- 조건문 안에 조건문 사용 가능
- 들여쓰기 유의

### 조건 표현식

- 조건에 따라 값을 정할 때 활용
- 삼항 연산자

```python
true인 경우 값 if 조건 else false인 경우 값

# 절댓값 저장
value = num if num >= 0 else -num
```

## 반복문

- 특정 조건을 만족할 때까지 같은 동작을 반복하고 싶을 때 사용
- while문: 종료 조건을 알 때
- for문: 반복할 범위를 알 때
- 반복 제어: break, continue, for-else

### while 문

- 조건식이 참인 경우 반복적으로 코드 실행
- 복합 연산자: 연산과 할당을 합쳐놓은 것 ex. 반목문 안에서 카운트하는 경우

```python
while 조건:
    # code block

# 복합 연산자
a = 0
while a < 5:
    print(a)
    a += 1
print('end')
```

### for 문

- 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체의 요소를 모두 순회
    - 순회 가능한 자료형: string, list, dict, tuple, range, set
    - 순회형 함수: range, enumerate
- 처음 → 끝까지 모두 순회하므로 종료 조건 필요 없음

```python
for 변수명 in iterable:
    # code block
```

- dictionary 순회: 기본적으로 key를 순회함
    - .keys(), .values(), .items() 활용 가능

```python
# dictionary 순회

grades = {'john': 80, 'eric': 90}

for i in grades:
    print(i)  # john  eric
    print(i, grades[i])  # john 80  eric 90

for student, grade in grades.items():
    print(student, grade)  # john 80  eric 90
```

- enumerate 순회: 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    - (index, value) 형태의 tuple로 구성된 열거 객체를 반환

```python
# enumerate 순회

members = ['a', 'b', 'c']

for idx, member in enumerate(members):
    print(idx, member)  # 0 a  1 b  2 c

print(list(enumerate(members)))  # [(0, a), (1, b), (2, c)]
print(list(enumerate(members, start = 1)))  # [(1, a), (2, b), (3, c)]
```

- list comprehension: 표현식과 제어문을 통해 리스트를 간결하게 생성
- dictionary comprehension: 표현식과 제어문을 통해 딕셔너리를 간결하게 생성

```python
# list comprehension

[code for 변수 in iterable]
[code for 변수 in iterable if 조건식]

# 1~3의 세제곱 리스트 출력
cubic_list = [number ** 3 for number in range(1, 4)]
print(cubit_list)  # [1, 8, 27]

# dictionary comprehension

{key: value for 변수 in iterable}
{key: value for 변수 in iterable if 조건식}

# 1~3의 세제곱 딕셔너리 출력
cubic_list = {number: number ** 3 for number in range(1, 4)}
print(cubit_list)  # {1: 1, 2: 8, 3: 27}
```

### 반복문 제어

- break: 반복문 종료

```python
for i in range(10):
    if  i > 1:
        print('0과 1만 필요해!')
        break
    print(i)

'''
0
1
0과 1만 필요해!
'''
```

- continue: continue 이후 코드 수행 안하고, 다음 반복 수행

```python
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
'''
1
3
5
'''
```

- pass: 아무것도 하지 않음, 이후 코드 수행 (그냥 지나쳐줘)

```python
# pass VS continue

# i가 2일때 pass
for i in range(4):
    if i == 2:
        pass
    print(i)  # 0  1  2  3

# i가 2일때 continue
for i in range(4):
    if i == 2:
        continue
    print(i)  # 0  1  3
```

- for-else: 반복문 끝까지 실행 후 else문 실행
    - break를 통해 중간에 종료되면 else문 실행 안함

```python
for char in 'apple':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.')  # b가 없습니다.

for char in 'banana':
    if char == 'b':
        print('b!')  # b!
        break        # break 작동 - else문 실행X
else:
    print('b가 없습니다.')
```

## 함수

### 함수

- 특성한 기능을 하는 코드의 묶음
- decomposition(분해): 기능 단위로 쪼개고 재사용 가능하게
    - ex. len, sum
- abstraction(추상화): 재사용성, 가독성, 생산성, 내용(내부구조)을 몰라도 사용 가능하게
    - ex. 스마트폰, print
- 내장 함수: 파이썬에 기본으로 포함된 함수
외장 함수: import문을 통해 사용, 외부 라이브러리
사용자 정의 함수
- 선언과 호출(define&call) → 입력(Input) → 문서화(Docstring) → 범위(Scope) → 결괏값(Output)
    1. 선언고 호출
    2. 입력
    3. 문서화
    4. 범위
    5. 결과

### 함수의 결과값 (output)

### 함수의 입력 (input)

- parameter: 매개변수 인수 인자
- argument: 인자?
- positional arguments: 자기 자리에 맞게 찾아 들어가는 것
- keyword arguments: 직접 변수 지정
    - keyword 와 positional 을 같이 적을 때는 무조건 positional이 먼저
- default arguments values: 기본값을 지정해 함수 호출 시 argument 값을 먼저 처리
    
    ⇒ 복잡한 값은 나중에 넣어주자!
    

### Python의 범위 (scope)

### 함수 응용

## 모듈

- 모듈 = 하나의 파이썬 파일 단위 (파일 하나하나가 모듈)
- 다양한 기능을 하나의 파일로

### 모듈과 패키지

```python
import module  # module.var
import module as md  # md.var
from module import var, function  # 필요한 기능만 import
from module import *  # 사용할 때 module. 안붙여도 됨 var()
```

### Python 표준 라이브러리

```bash
pip freeze > requirments.txt
pip install -r requirments.txt  # -r을 넣어주면 순서대로 다운받아줌
```

### 사용자 모듈과 패키지

- 패키지는 여러 모듈/하위 패키지로 구조화 ex. package.module
- 모든 폴더에 __init__.py를 만들어 패키지로 인식

```python
# calculator/tools.py
def add()

def minus()

from calculator import tools

print(dir(tools))
print(tools.add(3, 5))  # 8
print(tools.minus(3, 5))  # -2
```

### 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우, 모두 pip를 통해 설치 해야함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음

⇒ 이런 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음

```bash
python -m venv <폴더명>
deactivate  # 가상환경 비활성화
```
