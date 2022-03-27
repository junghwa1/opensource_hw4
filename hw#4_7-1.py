## 변수 선언 부분 ##

arr = ['0xA37B','0x23CC','0x88D9','0xBB8F','0x3A9A']

'''2019038062 염중화'''

## 메인 코드 부분 ##

print("정렬 전 데이터 : ", arr[0:5])


for j in range(0,5):
    int(arr[j],16)

for k in range(0,5):
    for i in range(k+1,5):
        if (arr[i] < arr[k]):
            Min=i
    arr[k],arr[Min] = arr[Min],arr[k]

print("정렬 후 데이터 : ", arr[0:5])
