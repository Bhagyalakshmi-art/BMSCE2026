import sys

user_num=int(sys.argv[1])

for i in range(1,21):
    print('%d*%2d=%3d'%(user_num,i,user_num*i))