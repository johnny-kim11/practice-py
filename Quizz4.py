#Quiz) 당신의 학교에서는 파이썬 코딩대회를 추진합니다. 
#참석률을 높이기 위해 댓글이벤트를 진행하기로 하였습니다. 
#댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 됩니다.

#조건1: 작성자 20명
#조건2: 무작위 추첨 & 중복불가
#조건3: random　모듈의 shuffle & sample 을 활용


from random import *
par = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  #list

coffee = list(shuffle(par))
print(coffee)
print("커피당첨자: ", end="")
print(sample(par,3))