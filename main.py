튜플 = (1,2,3,4,5)
리스트 = [1,2,3,4,5]#리스트랑 다르게 변경이 안됨
세트 = {5,4,'a','b',1,4,4}#리스트랑 다르게 순서가 없음
                  #중복이 없음
""" 
#캐스팅 바꾸고싶은자료형(변수)
# c++  (바꾸고싶은것)변수
비대면 = ['기원','중원','하영','세환']
대면 = ['상목', '계현', '형준', '중원']
print( set(비대면) - set(대면))

for i in 세트:
    print(i)
"""
dict_example = {
    '이름': '손호용',
'나이' : 15,
    '성별' : '남자'
}
dict_example['추가키'] = '추가값'
dict_example.update(추가키='추가값')
dict_example.pop('추가키')
#json 딕셔너리 key : value
print(dict_example.keys())
print(dict_example.values())
print(dict_example['이름'])