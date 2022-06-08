# blogproject/core/views.py
from flask import render_template, request, Blueprint
from blogproject.models import BlogPost

core = Blueprint('core',__name__)


# Home page
@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', blog_posts=blog_posts)


# About page
@core.route('/info')
def info():
    return render_template('info.html')