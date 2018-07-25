#-* -coding:GBK -* -
#中文注释模板
def qsort(us):
    length = len(us)
    flag = True
    while flag:
        left = 0;
        right = length-1;
        tmp = us[0]
        flag = False
        print(us,tmp)
        input()
        while left <right:
            print("right",us,us[left],us[right])
            while left<right:
                if us[right] <= tmp:
                    us[left] = us[right]
                    left+=1
                    flag = True
                    break;
                else:
                    right-=1

            print("left",us,us[left],us[right])
            while left<right:
                if us[left] >= tmp:
                    us[right] = us[left]
                    right-=1
                    flag = True
                    break
                else:
                    left+=1
            print("after",us,us[left],us[right])
        us[left] = tmp
    return us

if __name__ == "__main__":
    us = [10,5,3,1,7,2,8]
    print(us)
    print(qsort(us))