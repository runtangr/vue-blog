## blog

    第一个基础版本完成，非常感谢开源。
    
## 使用说明 
```
dev环境:
    安装:
        virtualenv venv
        source venv/bin/activate
        pip install -r requirements.txt
    初始化数据库(需安装mysql，同时创建test库)：
        export FLASK_APP=manager.py 
        venv/bin/flask initdb
    编译:
        npm run install
        npm run build     
    运行：
        python app.py  
生产环境：
    程序部署：
        初次使用：docker-compose up -d
        后面修改启动不需要再启动init 服务：docker-compose up -d web
    nginx部署：
        https://github.com/runtangr/vue-blog-nginx
        docker-compose up -d
        这里使用了桥接网络，只需服务即可连接。
```
## 产考借鉴

    非常感谢以下网站和开源代码。
    https://www.xuhaodong.cn/home
    https://huangxuan.me/
    http://www.chunibyo.org/blog
    https://github.com/dongweiming/wechat-admin.git
    https://github.com/Molunerfinn/vue-koa-demo
