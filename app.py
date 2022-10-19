from asyncio.windows_events import NULL
from flask import Flask, request, abort ,jsonify
import json ,os
from  simplegmail  import  Gmail 
gmail  =  Gmail ()
app = Flask(__name__)
res={}
def send(email,vscode):
    text = f'''驗證碼為：{vscode}
    '''
    params = {
    "to": email,
    "sender": "s1410832047@gms.nutc.edu.tw",
    "subject": "學伴網註冊申請",
    "msg_html": text,
    "signature": True
    }
    message = gmail.send_message(**params)
    print("OK ")

@app.route("/send_mail", methods=['GET'])
def get_res():
    try:
        email = request.args.get('email')
        vscode = request.args.get('vscode')
        send(email,vscode)
        res['status'] = 'ok'
        res['message'] = '發送成功'
    except:
        res['status'] = 'error'
        res['message'] = '發生錯誤'
    return res

if __name__ == "__main__":
    app.run(port=8888,debug=True,host='0.0.0.0')