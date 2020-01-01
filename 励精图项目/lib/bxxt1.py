import time
import requests
class APImgr():#这是一个类

    def login(self,):
        response = requests.post(
            url="http://admin.lijintu.com:81/admin/userlogon",
            json={
                'iphont': '18583007169',
                'password': '123456'
            }
        )
        print(response.status_code)
        res = response.json()#打印相应200为正常
        r = res['result']['token']
        self.token = r
        print(res)
#打印token
        return r
#储存登录成功返回的token
    def The_uesr(self):
        #再次登录-然后记录token
        data = {'token':self.token}
        time.sleep(1)
        res = requests.post(url='http://admin.lijintu.com:81/user/linkuser?token='+data['token'])
        #print(res.url)
        assert res.status_code == 200
        try:
            print(res.json())
        except:
            print(res.text)
        #print(res.json())

#市场部数据录入
    def linkuser(self,date='date',val='val'):#def表示这里要声明一个函数
        data = {'token':self.token}
        #再次登录-然后记录token
        url = ('http://admin.lijintu.com:81/market/inputmarket?token='+data['token'])
        #print(url,)
        time.sleep(1)
        res = requests.post(url=url,
                            json={
                                date:"2019-01",
                                val:"100"
                                 })
        print(res.text)
#市场部数据查看
    def To_view(self,date='date'):
        data = {'token':self.token}
        #再次登录-然后记录token
        url = ('http://admin.lijintu.com:81/market/linkmarket?token='+data['token'])
        #print(url,)
        time.sleep(1)
        res = requests.post(url=url,
                            json={
                                date:"2019-10"
                                 })
        print(res.text)
    def entry(self):
        data = {}



apimgr = APImgr()
