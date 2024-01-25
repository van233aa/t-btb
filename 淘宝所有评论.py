import requests
import parsel
import csv
from wordcloud import WordCloud
import jieba
jieba.setLogLevel(jieba.logging.INFO)

f=open('淘宝详细评论.csv','a',encoding='utf-8-sig',newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(["id","userNick","reviewWordContent","memory","color"])


cookies = {
    'cna': 'WZhgGW7QHlkCAX0+A0/DQEcr',
    'enc': 'HjzrtgQ6iza5hYZiJZDAoB4sqcrPOOlPJaMshW2JzL9%2BtQEplVjiGCMsPv0Jxji70980QljQCOpduiSik7JRnwwkdsYzRWBgz4vPsncMCzViMsk1EGbhmYYL4lMzVcx5',
    'l': 'fBPPwb4ePFUwA6oZBO5CPurza77T3QAb8sPzaNbMiIEGa6Hd1E3mNNCTxJgJRdtjgT5YNetrWDM-1dekPXz38dkDBeYQjqf1zw9p8e9AWT_V.',
    'xlly_s': '1',
    'lid': '1%E9%A2%9D%E4%BD%A0%E8%A6%81',
    'mtop_partitioned_detect': '1',
    'dnk': '1%5Cu989D%5Cu4F60%5Cu8981',
    'uc1': 'cookie14=UoYekxscFHou2g%3D%3D&pas=0&existShop=false&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie21=UtASsssme%2BBq',
    'uc3': 'id2=UUwY%2FjT0bMBm3g%3D%3D&vt3=F8dD3ChDY1%2Fo321qMos%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&nk2=UgctmamckQ%3D%3D',
    'tracknick': '1%5Cu989D%5Cu4F60%5Cu8981',
    '_l_g_': 'Ug%3D%3D',
    'uc4': 'nk4=0%40UG9HBO6kEfTM0JAUF%2BgUE8Op&id4=0%40U27Hq%2BUCSKrvyrlevPBZnxZorM03',
    'unb': '2487531532',
    'lgc': '1%5Cu989D%5Cu4F60%5Cu8981',
    'cookie1': 'U%2BToMxxNdCDZC%2BRFB5GsP11l8Gt9DqMwcYdor%2B5SHYw%3D',
    'login': 'true',
    'cookie17': 'UUwY%2FjT0bMBm3g%3D%3D',
    'cookie2': '1df147668f2773bcbbd445b9a248703e',
    '_nk_': '1%5Cu989D%5Cu4F60%5Cu8981',
    'sgcookie': 'E100NUVB0y8L1sv%2FetiA4U8eQz872FI5UOxgJN8vcsySWyGzm4qttX5qgDBN8oWxPyYBNkgNf1VC7C7lT2ITIoIMxIuTvSYJuOtLlRLNwZRBQyTp%2FZbhG3ANHcvMXhiJVQTr',
    'cancelledSubSites': 'empty',
    'sg': '%E8%A6%812b',
    't': '9de5473acbef25a874d99010d5ac0984',
    'csg': '0f15f6a7',
    '_tb_token_': '5674537b8a736',
    '_m_h5_tk': '92028045d536aae3e4f09f319fea0971_1706191386794',
    '_m_h5_tk_enc': '3757466e7c48e9356fcd854fda57e755',
    'hng': 'CN%7Czh-CN%7CCNY%7C156',
    'x5sec': '7b22733b32223a2263313864396632366538363063373633222c22617365727665723b33223a22307c434b617279613047454f2b646f5950372f2f2f2f2f774561444449304f4463314d7a45314d7a49374d5443586d65546242513d3d227d',
    'tfstk': 'eMgJfAtmjKvoOOWamUKm8j-jT-OmJ4hzkYl1-J2lAxHxQAQHa0DnDWMmpy4nOLkKJ-MR-0coO6FInzZEqJ2upyhEBIvMSFcrayzWIdYiN-CN1y1uZFQjabzFgsXBjmGPJBn9_MD541WlCZ0mJ7tsCOom3so4wued--Qp4BV72RG8Hd9skdr8CbwARgujSVeItO2TtgOvMMSUVS-oV8PRABtjbSeMiijFYoV4MRAvMMSUVSPYIIjcYMr0g',
    'isg': 'BEZGJYNcX-PZuQvczdvhj_xMlzzIp4ph-5Uo1zBvbGlFM-dNmDaacQHFC2__m4J5',
}

headers = {
    'authority': 'h5api.m.tmall.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cna=WZhgGW7QHlkCAX0+A0/DQEcr; enc=HjzrtgQ6iza5hYZiJZDAoB4sqcrPOOlPJaMshW2JzL9%2BtQEplVjiGCMsPv0Jxji70980QljQCOpduiSik7JRnwwkdsYzRWBgz4vPsncMCzViMsk1EGbhmYYL4lMzVcx5; l=fBPPwb4ePFUwA6oZBO5CPurza77T3QAb8sPzaNbMiIEGa6Hd1E3mNNCTxJgJRdtjgT5YNetrWDM-1dekPXz38dkDBeYQjqf1zw9p8e9AWT_V.; xlly_s=1; lid=1%E9%A2%9D%E4%BD%A0%E8%A6%81; mtop_partitioned_detect=1; dnk=1%5Cu989D%5Cu4F60%5Cu8981; uc1=cookie14=UoYekxscFHou2g%3D%3D&pas=0&existShop=false&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie21=UtASsssme%2BBq; uc3=id2=UUwY%2FjT0bMBm3g%3D%3D&vt3=F8dD3ChDY1%2Fo321qMos%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&nk2=UgctmamckQ%3D%3D; tracknick=1%5Cu989D%5Cu4F60%5Cu8981; _l_g_=Ug%3D%3D; uc4=nk4=0%40UG9HBO6kEfTM0JAUF%2BgUE8Op&id4=0%40U27Hq%2BUCSKrvyrlevPBZnxZorM03; unb=2487531532; lgc=1%5Cu989D%5Cu4F60%5Cu8981; cookie1=U%2BToMxxNdCDZC%2BRFB5GsP11l8Gt9DqMwcYdor%2B5SHYw%3D; login=true; cookie17=UUwY%2FjT0bMBm3g%3D%3D; cookie2=1df147668f2773bcbbd445b9a248703e; _nk_=1%5Cu989D%5Cu4F60%5Cu8981; sgcookie=E100NUVB0y8L1sv%2FetiA4U8eQz872FI5UOxgJN8vcsySWyGzm4qttX5qgDBN8oWxPyYBNkgNf1VC7C7lT2ITIoIMxIuTvSYJuOtLlRLNwZRBQyTp%2FZbhG3ANHcvMXhiJVQTr; cancelledSubSites=empty; sg=%E8%A6%812b; t=9de5473acbef25a874d99010d5ac0984; csg=0f15f6a7; _tb_token_=5674537b8a736; _m_h5_tk=92028045d536aae3e4f09f319fea0971_1706191386794; _m_h5_tk_enc=3757466e7c48e9356fcd854fda57e755; hng=CN%7Czh-CN%7CCNY%7C156; x5sec=7b22733b32223a2263313864396632366538363063373633222c22617365727665723b33223a22307c434b617279613047454f2b646f5950372f2f2f2f2f774561444449304f4463314d7a45314d7a49374d5443586d65546242513d3d227d; tfstk=eMgJfAtmjKvoOOWamUKm8j-jT-OmJ4hzkYl1-J2lAxHxQAQHa0DnDWMmpy4nOLkKJ-MR-0coO6FInzZEqJ2upyhEBIvMSFcrayzWIdYiN-CN1y1uZFQjabzFgsXBjmGPJBn9_MD541WlCZ0mJ7tsCOom3so4wued--Qp4BV72RG8Hd9skdr8CbwARgujSVeItO2TtgOvMMSUVS-oV8PRABtjbSeMiijFYoV4MRAvMMSUVSPYIIjcYMr0g; isg=BEZGJYNcX-PZuQvczdvhj_xMlzzIp4ph-5Uo1zBvbGlFM-dNmDaacQHFC2__m4J5',
    'referer': 'https://detail.tmall.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}

params = {
    'jsv': '2.7.2',
    'appKey': '12574478',
    't': '1706186210492',
    'sign': 'ed5c8f6ad093476b69e00e24dadc1469',
    'api': 'mtop.alibaba.review.list.for.new.pc.detail',
    'v': '1.0',
    'isSec': '0',
    'ecode': '0',
    'timeout': '10000',
    'ttid': '2022@taobao_litepc_9.17.0',
    'AntiFlood': 'true',
    'AntiCreep': 'true',
    'preventFallback': 'true',
    'data': '{"itemId":"750153632189","bizCode":"ali.china.tmall","channel":"pc_detail","pageSize":20,"pageNum":1}',
}

response = requests.get('https://h5api.m.tmall.com/h5/mtop.alibaba.review.list.for.new.pc.detail/1.0/', params=params, cookies=cookies, headers=headers)
taobao_data=response.json()
# print(response.text)
list=taobao_data['data']['module']['reviewVOList']
for i in list:
    reviewWordContent=i['reviewWordContent']
    userNick=i['userNick']
    id=i['id']
    memory=i['skuText']['存储容量']
    color=i['skuText']['机身颜色']
    print(id,userNick,reviewWordContent,'一加12'+memory,color)
    csv_writer.writerow([id,userNick,reviewWordContent,'一加12'+memory,color])


with open('淘宝详细评论.csv','r',encoding='utf-8-sig')as f:
    reader=csv.reader(f)
    # header=next(reader)
    column_index=2
    column_data=[row[column_index] for row in reader]

strc="".join(column_data)
print(strc)
words=jieba.lcut(strc)
new_words=''.join(words)

words=jieba.lcut(strc)
new_words=''.join(words)

excludes={'comment'}
wordcloud=WordCloud(width=2000,
                    height=1080,
                    font_path='msyh.ttc',
                    background_color='white',
                    stopwords=excludes,
                    ).generate(new_words)
wordcloud.to_file('淘宝所有评论图片.png')







