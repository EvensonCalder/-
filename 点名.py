from random import randint
from tkinter import *
DictName = {1: '陈昊楠',
2: '陈俊逸',
3: '陈吾宇',
4: '陈元乙',
5: '陈正丰',
6: '解宇天',
7: '刘赟洋',
8: '刘泽锐',
9: '缪宇博',
10: '莫光海',
11: '彭毅聪',
12: '桑嘉鸿',
13: '王舒啸',
14: '王宇浩',
15: '王自醇',
16: '谢奕辰',
17: '俞俊杰',
18: '张劭锴',
19: '周巍',
20: '曾赵媛',
21: '陈乐妍',
22: '高佳怡',
23: '高雪',
24: '胡静璇',
25: '康筱',
26: '李江月',
27: '李科漫',
28: '刘靓婧',
29: '宋佳琳',
30: '汪家彤',
31: '王珂雪',
32: '徐锦航',
33: '赵奕欣',
34: '周语笑',
35: '吴杨如',
36: '庞李琪'}
used=[0]*37
rond=0
root=Tk()
root.title('点名器  by Star. Cyy')
root.geometry('720x480')
Num = 1
flag = True
lb2 = Label(root,text='')
lb2.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.2)
def get():
    global rond
    rnd=randint(1,36)
    while (used[rnd]>rond//36):
        rnd=randint(1,36)
    lb2 = Label(root,text=DictName[rnd],font=("楷体",56))
    lb2.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.3)
    used[rnd]=used[rnd]+1;
    rond=rond+1;
lb1 = Label(root,text='点名器',font=24)
lb1.place(relx=0.3, rely=0, relwidth=0.4, relheight=0.2)
lb2 = Label(root,text=' ',font=("楷体",36))
lb2.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.2)
btn1 = Button(root, text='点名', command=get,font=24)
btn1.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.2)
root.mainloop()
