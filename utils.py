#coding=utf-8
import requests
import json



#获取access_token
def get_token(APIkey,Secretkey):
    APIkey = APIkey
    Secretkey = Secretkey
    token_url = 'https://wenxin.baidu.com/younger/portal/api/oauth/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(APIkey,Secretkey)
    token = requests.post(token_url)
    if token.status_code!=200:
        return -1
    else:
        token_data = json.loads(token.text)['data']
        return token_data


#获取摘要
def get_summary(access_token,text,seq_len=16,min_dec_len=10):
    url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernie/3.0/zeus"
    header = {'Content-Type':"application/x-www-form-urlencoded"}
    data = {
        'access_token': access_token,
        'text': text,
        'seq_len': seq_len,
        'min_dec_len': min_dec_len,
        'temperature': 2,
        'task_prompt': 'Summarization'}
    summary = requests.post(url=url,data=data,headers=header)
    if summary.status_code!=200:
        return -1
    else:
        summary_data = json.loads(summary.text)['data']['result']
        return summary_data


#获取绘图ID
def get_imgID(access_token,text,style='油画'):
    url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernievilg/v1/txt2img"
    header = {'Content-Type': "application/x-www-form-urlencoded"}
    data = {
        'access_token': access_token,
        'text': text,
        'style': style,
    }
    task = requests.post(url=url,data=data,headers=header)
    if task.status_code!=200:
        return -1
    else:
        task_id = json.loads(task.text)['data']['taskId']
        return task_id


#获取绘图结果
def get_img(access_token,task_id):
    url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernievilg/v1/getImg"
    header = {'Content-Type': "application/x-www-form-urlencoded"}
    data = {
        'access_token': access_token,
        'taskId': task_id
    }
    img = requests.post(url=url, data=data, headers=header)
    if img.status_code!=200:
        return -1
    else:
        img_data = json.loads(img.text)['data']
        status = img_data['status']
        if status == 0:
            return int(img_data['waiting'][0:-1])
        else:
            websites = ""
            for i in img_data['imgUrls']:
                websites += i['image']+"\n"
            return websites
