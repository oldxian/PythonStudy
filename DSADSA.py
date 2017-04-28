#encoding:utf-8
emptyDict = {}




file = open(r'/home/oldxian/Desktop/词典/主题/主题.txt')
zhuti1 = open('/home/oldxian/Desktop/词典/主题/主题.txt','r')
zhuti2=open('/home/oldxian/Desktop/词典/主题/题材内容.txt','r')
zhuti3=open('/home/oldxian/Desktop/词典/主题/风格.txt','r')
zhizou1 = open ('/home/oldxian/Desktop/词典/制作/出品公司.txt','r')
zhizou2 = open ('/home/oldxian/Desktop/词典/制作/制作.txt','r')
zhizou3 = open ('/home/oldxian/Desktop/词典/制作/导演.txt','r')
zhizou4 = open ('/home/oldxian/Desktop/词典/制作/编剧.txt','r')
zhizou5 = open ('/home/oldxian/Desktop/词典/制作/选景.txt','r')
juqin1 =open('/home/oldxian/Desktop/词典/剧情/剧情.txt','r')
juqin2=open('/home/oldxian/Desktop/词典/剧情/发展.txt','r')
juqin3=open('/home/oldxian/Desktop/词典/剧情/开头.txt','r')
juqin4=open('/home/oldxian/Desktop/词典/剧情/泪点.txt','r')
juqin5=open('/home/oldxian/Desktop/词典/剧情/笑点.txt','r')
juqin6=open('/home/oldxian/Desktop/词典/剧情/结局.txt','r')
shiting1=open('/home/oldxian/Desktop/词典/视听/动作.txt','r')
shiting2=open('/home/oldxian/Desktop/词典/视听/画面.txt','r')
shiting3=open('/home/oldxian/Desktop/词典/视听/视听.txt','r')
shiting4=open('/home/oldxian/Desktop/词典/视听/试听效果中的其他','r')
shiting5=open('/home/oldxian/Desktop/词典/视听/镜头.txt','r')
shiting6=open('/home/oldxian/Desktop/词典/视听/音乐.txt','r')
juese1 =open('/home/oldxian/Desktop/词典/角色/反派.txt','r')
juese2 =open('/home/oldxian/Desktop/词典/角色/女主角.txt','r')
juese3 =open('/home/oldxian/Desktop/词典/角色/男主角.txt','r')
juese4 =open('/home/oldxian/Desktop/词典/角色/角色.txt','r')
juese5 =open('/home/oldxian/Desktop/词典/角色/角色中的其他.txt','r')
juese6 =open('/home/oldxian/Desktop/词典/角色/配角.txt','r')
zhutiSum = 0l
zhizouSum =0L
juqinSum=0l
shitingSum=0l
jueseSum=0l
for line in file.readlines() :
    for lin1 in zhuti1.readlines():
        if lin1 in line:
            zhutiSum=zhutiSum+1
            break

    for lin2 in zhuti2.readlines():
        if lin2 in line:
            zhutiSum = zhutiSum + 1
            break
    for lin3 in zhuti3.readlines():
        if lin3 in line:
            zhutiSum = zhutiSum + 1
            break
    for lin4 in zhizou1.readlines():
        if lin4 in line:
            zhizouSum=zhizouSum+1
            break
    for lin5 in zhizou2.readlines():
        if lin5 in line:
            zhizouSum = zhizouSum + 1
            break
    for lin6 in zhizou3.readlines():
        if lin6 in line:
            zhizouSum = zhizouSum + 1
            break
    for lin7 in zhizou4.readlines():
        if lin7 in line:
            zhizouSum = zhizouSum + 1
            break
    for lin8 in zhizou5.readlines():
        if lin8 in line:
            zhizouSum = zhizouSum + 1
            break
    for lin9 in juqin1.readlines():
        if lin9 in line:
            juqinSum =juqinSum+1
            break
    for lin10 in juqin2.readlines():
        if lin10 in line:
            juqinSum = juqinSum + 1
            break
    for lin11 in juqin3.readlines():
        if lin11 in line:
            juqinSum = juqinSum + 1
            break
    for lin12 in juqin4.readlines():
        if lin12 in line:
            juqinSum = juqinSum + 1
            break
    for lin13 in juqin5.readlines():
        if lin13 in line:
            juqinSum = juqinSum + 1
            break
    for lin14 in juqin6.readlines():
        if lin14 in line:
            juqinSum = juqinSum + 1
            break
    for lin15 in shiting1.readlines():
        if lin15 in line:
            shitingSum =shitingSum+1
            break
    for lin16 in shiting2.readlines():
        if lin16 in line:
            shitingSum = shitingSum + 1
            break
    for lin17 in shiting3.readlines():
        if lin17 in line:
            shitingSum = shitingSum + 1
            break
    for lin18 in shiting4.readlines():
        if lin18 in line:
            shitingSum = shitingSum + 1
            break
    for lin19 in shiting5.readlines():
        if lin19 in line:
            shitingSum = shitingSum + 1
            break
    for lin20 in shiting6.readlines():
        if lin20 in line:
            shitingSum = shitingSum + 1
            break
    for lin21 in juese1.readlines():
        if lin15 in line:
            jueseSum =jueseSum+1
            break
    for lin22 in juese2.readlines():
        if lin22 in line:
            jueseSum = jueseSum + 1
            break

    for lin23 in juese3.readlines():
        if lin23 in line:
            jueseSum = jueseSum + 1
            break
    for lin24 in juese4.readlines():
        if lin24 in line:
            jueseSum = jueseSum + 1
            break
    for lin25 in juese5.readlines():
        if lin25 in line:
            jueseSum = jueseSum + 1
            break
    for lin26 in juese6.readlines():
        if lin26 in line:
            jueseSum = jueseSum + 1
            break
itemDict = {}.fromkeys(('zhuti', 'zhizou', 'juqin', 'shiting', 'juese'), (zhutiSum,zhizouSum,juqinSum,shitingSum,jueseSum))

print (zhutiSum)
print (zhizouSum)
print (juqinSum)
print (shitingSum)
print (jueseSum)