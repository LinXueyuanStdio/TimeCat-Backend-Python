# backend for android

- python 3.6
- pip 9.0.1

## 本地部署

### 安装virtualenv

clone仓库，用 virtualenv 创建虚拟环境 py35，并激活 py35

```bash
pip install --upgrade virtualenv
virtualenv py35 --python=python3.5
source py35/bin/activate
```

### 安装依赖

```bash
pip3 install -r requirements.txt
```

[创建虚拟环境并安装依赖](https://pipenv.readthedocs.io/en/latest/install/)

```bash
pip3 install pipenv
export PIPENV_IGNORE_VIRTUALENVS=1
pipenv install --three
pipenv shell
```

### 初始化数据库，并创建超级用户

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 启动服务器

```bash
python manage.py runserver
```

用浏览器打开http://localhost:8000/
