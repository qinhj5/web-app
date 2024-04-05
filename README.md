# web-app示例网站

---

<br/>

## 一、简介

这是一个基于Flask + MySQL搭建的网站模板，并且集成了Google登录。

<br/>

## 二、特性

* 后端使用Python语言编写
* 基于Flask框架搭建Web应用
* 数据存储使用MySQL
* 支持Google登录网站
* 基于Credential管理用户会话周期
* ...

<br/>

## 三、目录结构

```
web-app/
├── config/
│   ├── client.json
│   ├── mysql.json
│   └── secret.json
├── models/
│   ├── __init__.py
│   ├── base.py
│   └── user_tab.py
├── processors/
│   └── user.py
├── routes/
│   └── home.py
├── static/
│   ├── favicon.ico
│   ├── script.js
│   └── styles.css
├── templates/
│   └── index.html
├── .gitignore
├── app.py
├── app.wsgi
├── cli.py
├── debug.py
├── README.md
└── requirements.txt
```

<br/>

## 四、使用教程

<p>参考文章: <a href="https://blog.csdn.net/embracestar/article/details/132919569">《Apache+Flask在云服务器搭建个人网站》</a></p>

<br/>

---

<p align="center">有错误或者改进的地方请各位积极指出！</p>
<p align="center"><a href="https://github.com/qinhj5">GitHub</a> | <a href="https://blog.csdn.net/embracestar">CSDN</a></p>

---
