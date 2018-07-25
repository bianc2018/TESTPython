#-* -coding:GBK -* -
#中文注释模板
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if target<array[0][0] or target>array[-1][-1]:
            return False
        self.row = len(array)
        self.col = len(array[0])
        i = self.row-1
        j = 0
        p = 0
        d = 0

        flag =0;
        r = self.find_sub(target,array,i,j)
        if r==0:
           return True
        elif r==-2:
           return False
        elif r==-1:
           i = int(i/2)
           p=self.row
           d = 0
           flag = 0
        elif r==1:
           i=self.row
           j = int(self.col/2)
           p = self.col
           d = 0
           flag = 1

        while True:
            print("i,j",i,j)
            r = self.find_sub(target,array,i,j)
            if r==0:
                return True
            elif r==-2:
                return False
            elif r==-1:
                if p<=d:
                    return False
                if flag==0:
                    p = i
                    i = int((p-d)/2)
                else:
                    p=j
                    j = int((p-d)/2)
            elif r==1:
                if p<=d:
                    return False
                if flag==0:
                    d = i
                    i = int((p-d)/2)
                else:
                    d=j
                    j = int((p-d)/2)


    def find_sub(self,target, array,row,col):
        #-1,0,1
        tag = 0
        print(row,col)
        if row<0 or row>=self.row or col<0 or col>=self.col:
            return -2
        while True:
            print("68",row,col)
            if array[row][col] == target:
                return 0
            elif array[row][col] < target:
                if tag==1:
                    return -2
                tag =-1
            else:
                if tag==-1:
                    return -2
                tag =1
            row-=1
            col+=1
            if row<0 or col>=self.col:
                return tag

if __name__ == "__main__":
    s=Solution()
    print(s.Find(7,[[1,2,8,9],[4,7,10,13]]))