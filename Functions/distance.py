# 欧氏距离
def distance(a,b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i]-b[i])**2
    return sqrt(sum)
# print( 'a,b 多维距离为：',distance((1,1,2,2),(2,2,4,4)))


# 曼哈顿距离
def threeMHDdis(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1]) + abs(a[2]-b[2])
# print('a,b 三维曼哈顿距离为：', threeMHDdis((1,1,1),(2,2,2)))


# 切比雪夫距离
def moreQBXFdis(a,b):
    maxnum = 0
    for i in range(len(a)):
        if abs(a[i]-b[i]) > maxnum:
            maxnum = abs(a[i]-b[i])
    return maxnum
# print( 'a,b多维切比雪夫距离：' , moreQBXFdis((1,1,1,1),(3,4,3,4)))


# 夹角余弦距离
def moreCos(a,b):
    sum_fenzi = 0.0
    sum_fenmu_1,sum_fenmu_2 = 0,0
    for i in range(len(a)):
        sum_fenzi += a[i]*b[i]
        sum_fenmu_1 += a[i]**2
        sum_fenmu_2 += b[i]**2

    return sum_fenzi/( sqrt(sum_fenmu_1) * sqrt(sum_fenmu_2) )
# print ('a,b 多维夹角余弦距离：',moreCos((1,1,1,1),(2,2,2,2)))


# 汉明距离
def hanmingDis(a,b):
    sumnum = 0
    for i in range(len(a)):
        if a[i]!=b[i]:
            sumnum += 1
    return sumnum
# print ('a,b 汉明距离：',hanmingDis((1,1,2,3),(2,2,1,3)))


# 杰卡德距离
def jiekadeDis(a,b):
    set_a = set(a)
    set_b = set(b)
    dis = float(len( (set_a | set_b) - (set_a & set_b) ) )/ len(set_a | set_b)
    return dis
# print ('a,b 杰卡德距离：', jiekadeDis((1,2,3),(2,3,4)))


# 杰卡德相似系数
def jiekadeXSDis(a,b):
    set_a = set(a)
    set_b = set(b)
    dis = float(len(set_a & set_b)  )/ len(set_a | set_b)
    return dis
# print( 'a,b 杰卡德相似系数：', jiekadeXSDis((1,2,3),(2,3,4)))
