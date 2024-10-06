# 声明

本程序仅做学习抓包的用途，请勿用于其他用途。一切其他用途与本项目无关。

# 有什么用

跳过第二课堂网络学习的答题cd，提高答题效率，把时间用在更有意义的事情上面

# 部署环境

python>=3.6

    pip install mitmproxy

# 使用-方案proxy
在proxy.py的文件目录下输入

    mitmweb -p 8080 -s proxy.py

以win11为例，设置->网络和Internet->代理->使用代理服务器，代理ip地址:127.0.0.1，代理端口:8080

其他系统请自行百度搜索如何设置代理
# 使用-方案auto
先自行抓包获取secret与key_session，并写入同目录的user.txt中。或者使用方案proxy，在网络学习中随便打开一篇文章即可。

准备完成后

    python main.py

注意，本方案只做单选题，虽然够用就是了
# 视频教程
https://github.com/ANormalDD/HFUT_second_class
# Q&A
Q1:我看不到文章怎么答题

    A:为了省下翻到底部的时间，我删除了文章。
    1.随便答，答错没关系，再次进去重新答就行。
    2.访问http://127.0.0.1:8081/#/flows，找到最下方网址前缀为$https://dekt.hfut.edu.cn/scReports/api/wx/netlearning/的网站,点击他，在右侧点击response，然后按下ctrl+f搜索题目空前面的文本，即可看到答案
    3.跳过多选题，即可

Q2:为什么没题目

    A:或许他本身就没题目

Q3:关闭脚本断网了怎么办

    A:未关闭代理设置导致的

Q4:好麻烦，你能帮帮我吗

    A:不能，除非你vivo50（

Q5:auto方案报错怎么办

    重新获取secret与key_session，依旧报错请发issue

Q6:为什么不直接写登录流程，要抓包

    懒

Q7:已经结束嘞！搞不到那么多分了

    A:联系我，我有些大胆的想法可以解决这个问题，有一定风险，一直没去试（虽然在研究的时候就发现他似乎检测意识很淡薄，估计自己也是完成任务罢了）

Q8:其他问题

    发issue

