import time
import requests
class APImgr():

    def login(self):
        response = requests.post(
            url="http://admin.lijintu.com:81/admin/userlogon",
            json={
                'iphont': '18583007169',
                'password': '123456'
            }
        )
        print(response.status_code)
        res = response.json()
        r = res['result']['token']
        print(res)
        print(r)
        #记录token
        return r
        #储存登录成功的token


    def The_uesr(self):
        t = self.login()
        #再次登录-然后记录token
        data = {'token':t}
        time.sleep(1)
        res = requests.post(url='http://admin.lijintu.com:81/user/linkuser',params=data)
        print(res.url)
        assert res.status_code == 200
        try:
            print(res.json())
        except:
            print(res.text)

        #print(res.json())


    def linkuser(self,date='date',val='val'):
        r = self.login()
        #再次登录-然后记录token
        url = ('http://admin.lijintu.com:81/market/inputmarket?token='+r)
        print(url,)
        time.sleep(1)
        res = requests.post(url=url,
                            json={
                                date:"2019-01",
                                val:"100"
                                 })
        print(res.text)
#市场部数据查看

apimgr = APImgr()
