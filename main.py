import mitmproxy
import json
from datetime import datetime
class ModifyResponse:
    time = 0
    def logerr(str) :
        print("\033[91m"+str+"\033[0m")

    def logtxt(str):
        print("\033[42m"+str+"\033[0m")

    def logstart(str):
        print("\033[33m"+str+"\033[0m")
    def dump(data):
        with open("1"+datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".json","w") as f: 
            json.dump(data, f, indent=4)
    def response(self, flow: mitmproxy.http.HTTPFlow):
        global time
        # 检查响应的 Content-Type 是否为 JSON
        if flow.request.url.startswith("https://dekt.hfut.edu.cn/scReports/api/wx/netlearning/") and "page" not in flow.request.url and "filter/condition" not in flow.request.url and "questions" not in flow.request.url:
            if "application/json" in flow.response.headers.get("Content-Type", ""):
                # 解析原始的JSON响应
                data = json.loads(flow.response.get_text())
                if(data["data"]["category"]=="0"):
                    if("articleQueSt" in data["data"]):
                        ModifyResponse.logtxt("origin:articleQueSt"+str(data["data"]["articleQueSt"]))
                        data["data"]["articleQueSt"] = 0
                        data["data"]["contents"] = data["data"]["content"]
                        data["data"]["content"] = "<p> simplified </p>"
                    else :
                    #  time=time+1
                        ModifyResponse.dump(data)
                        ModifyResponse.logerr("need to updata")
                else:
                    data["data"]["category"]="0"
                    ModifyResponse.logtxt("Original type is video(https://dekt.hfut.edu.cn/"+data['data']['videoUrl']+")"+".The program have changed it to paragragh")
                    data['data']['videoUrl']=""
                    data["data"]["articleQueSt"] = 0
                    data["data"]["content"] = "<p> fuck it </p>"
                flow.response.set_text(json.dumps(data))
        if flow.request.url.startswith("https://dekt.hfut.edu.cn/scReports/api/wx/netlearning/questions/"):
            if "application/json" in flow.response.headers.get("Content-Type", ""):
                data = json.loads(flow.response.get_text())
                #ModifyResponse.dump(data)
                if(data['data']['questions']):
                    ModifyResponse.logtxt("origin answerSec"+str(data['data']['questions'][0]['answerSec']))
                    data['data']['questions'][0]['answerSec'] = 999
                    data['data']['showSec'] = -1
                else: ModifyResponse.logtxt("No question")
                flow.response.set_text(json.dumps(data))
                #ModifyResponse.dump(data)
        if flow.request.url.startswith("https://dekt.hfut.edu.cn/scReports/api/wx/netlearning/page/"):
            ModifyResponse.logtxt("page")
            if "application/json" in flow.response.headers.get("Content-Type", ""):
                #odifyResponse.logtxt("in")
                data = json.loads(flow.response.get_text())
                for i in data['data']['list'] :
                    #ModifyResponse.logtxt(i['category'])
                    i['category'] = "0"
                flow.response.set_text(json.dumps(data))

addons = [
    ModifyResponse()
]