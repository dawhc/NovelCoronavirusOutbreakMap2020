### 疫情可视化地图小程序

By  gale-force-eight

---

基于python3和pyecharts的疫情可视化地图小程序，可以实时展示全国疫情地图、全球疫情地图、各个省份疫情地图以及各省份分市疫情数据柱状图。

运行之前需要安装`python3`，以及安装依赖的第三方库：`requests、pyecharts、web.py`，即打开终端/命令行输入：

> ```bash
> pip3 install requests pyecharts web.py
> ```

小程序分为源文件和静态模板两部分，源文件即main.py，静态模板即statics文件夹下的html文件。

安装完毕后直接使用python3运行main.py，或在终端/命令行进入小程序根目录并输入：

> ```bash
> python3 ./main.py
> ```

如果程序出现TraceBack或闪退，请**检查自己电脑的8080端口是否被占用**，或者在终端/命令行运行时自行指定端口（此时端口号被改为8888）：

> ```bash
> python3 ./main.py 8888
> ```

当程序显示`http://0.0.0.0:8080/`，即可打开浏览器并转到`localhost:8080`。注意不要转到`http://0.0.0.0:8080/`，这并不是web.py服务器在本机的部署的ip地址。

主页比较简洁，可展示国内疫情地图和世界疫情地图，并提供省份疫情地图的查询入口。

每个省份查询结果分成了省份疫情地图和省份疫情数据柱状图。所有地图可缩放可查看数据，所有柱状图可以点击图例来显示/隐藏单个数据。

疫情实时数据来源：view.inews.qq.com

