import sys
sys.path.append('../')#系统自动搜索当前文件夹路径

from lib.bxxt1  import apimgr

apimgr.login()
print ( '【test登录】' )
apimgr.The_uesr()
print ( '【test获取数据id、姓名、手机号2】' )
apimgr.linkuser()
print ( '【test市场部数据载入3】' )
apimgr.To_view()
# t = 1
# def tets():
#     print(t)
# tets()