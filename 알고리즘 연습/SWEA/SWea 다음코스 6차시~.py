# a=int(input())
# cnt = 0
# while cnt<a:
#     num = int(input())
    
#     tem = list(map(int,input().split()))
#     print(cnt+1,max(tem)-min(tem))
    
#     cnt+=1
###########################7차시

a= int(input())
trial=0
while trial<a:
    mv,arrive,recharge = map(int,input().split())
    dis = 0
    cnt = 0
    center= list(map(int,input().split()))
    for i in range(len(center)-1):
        if dis+mv >=arrive:
            cnt+=1
            # print("@")
            break
        elif center[i] < dis+mv < center[i+1]:
            dis=center[i]
            cnt+=1
            # print("$")
        elif center[i] < dis+mv <= center[i+1]:
            dis = center[i+1]
            cnt+=1
            # print("%")
        elif dis+mv<center[i]:
            cnt=0
            # print("^")
            break

        else:
                   
            if center[i+1]<dis+mv:
                if dis+mv >= center[-1]:
                    cnt+=1
                # print("&")
                else:
                        pass
                
    print("#{} {}".format(trial+1,cnt))
    trial += 1 
#####################
T = int(input())
for i in range(T):
    K, N, M = map(int, input().split(' '))
    location = list(map(int, input().split(' ')))
    re_location = [*location, N]
    # print(re_location)
    interval = []
    for j in range(len(re_location)-1):
        interval.append(re_location[j+1]-re_location[j])
    interval = [re_location[0], *interval]
    print(interval)
    if max(interval) > K:
        result = 0
    else:
        result = 0
        dist = interval[0]
        
        for k in range(len(interval)-1):
            dist += interval[k+1]
            print(dist)
            if dist > K:
                result += 1
                dist=interval[k+1]
    print('#%d %d'%(i+1,result))
    