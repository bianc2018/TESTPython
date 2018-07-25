#-* -coding:GBK -* -
#中文注释模板

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        #print("p-t:",pre,tin)
        #input()
        if len(pre)==0:
            return None
        root = TreeNode(pre[0])
        if len(pre)==1:
            return root
        tl,tr = self.split(tin,pre[0])
        #print("tin:",tl,tr)
        pl = pre[1:len(tl)+1]
        pr = pre[len(tl)+1:]
        #print("pre:",pl,pr)
        root.left = self.reConstructBinaryTree(pl,tl)
        root.right = self.reConstructBinaryTree(pr,tr)
        return root
    def split(self,List,p):
        pos = 0
        for i in range(0,len(List)):
            if List[i]==p:
                pos = i
                break;
        return List[:pos],List[pos+1:]
if __name__ == "__main__":
    s = Solution()
    s.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])