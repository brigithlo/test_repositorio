def Bintree(r): return [r,[],[]]

def insertLeft(root, newBranch):
    t=root [1]
    root[1]=[newBranch,t,[]]
    return root

def insertRight(root, newBranch):
    t=root[2]
    root[2]=[newBranch,[], t]
    return root

def getRootVal(root): return root[0]

def setRootVal(root, newVal): root[0]

def getLeftChild(root):return root[1]

def getRightChild(root):return root[2]

t=Bintree(1)
insertLeft(t,5)
insertRight(t,2)
inserrLeft(getRightChild(t),9)