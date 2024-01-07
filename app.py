from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from login_manager import login_manager
from controllers import setup_routes

app = Flask(__name__)

# 구성 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://funcoding:funcoding@localhost/my_memo_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

# 데이터베이스 및 로그인 관리자 초기화
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

# 라우팅 설정
setup_routes(app)

# 데이터베이스 테이블 생성
with app.app_context():
    db.create_all()
