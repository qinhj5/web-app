1. 准备服务器

    在此步骤中，你需要准备一台服务器来托管你的项目。你可以选择云服务器或物理服务器，确保服务器满足你的项目需求。


2. 配置域名和DNS

    需要配置域名解析（DNS）以将域名指向你的服务器IP地址。这一步通常需要在你的域名注册商或DNS提供商处进行设置。


3. 服务器安装Homebrew、MySQL和Git

   使用Homebrew包管理器，在服务器上安装Python、MySQL和Git。以下是安装命令：
   ```bash
      # 安装Homebrew（如果尚未安装）
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      
      # 安装Python3.10
      brew install python@3.10
      
      # 安装MySQL
      brew install mysql
      
      # 安装Git
      brew install git
   ```

4. 配置MySQL
   ```bash
   # 启动MySQL服务
   sudo service mysql start
   
   # 启动安装向导
   sudo mysql_secure_installation
   
   # 登录数据库
   mysql -u root -p
  
   # 创建DB
   CREATE DATABASE flask_test_db;
   ```


5. 下载源码并进入项目目录
   ```bash
   git clone https://github.com/qinhj5/WebRepo.git
   cd WebRepo
   ```

6. 创建虚拟环境和安装依赖
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   ```


7. 编辑配置文件和初始化数据库
   ```bash
   vim config.json
   python3 cli.py --func create
   python3 cli.py --func init_users
   ```


8. 运行服务
   ```bash
   sudo sh ./run_live.sh
   ```