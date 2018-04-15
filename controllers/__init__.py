from flask import Blueprint, render_template


mod = Blueprint('controllers', __name__)

@mod.route('/')
def home():
    return render_template('index.html')


from .Questions import routes as question_routes
from .Surveys import routes as survey_routes
# from .Feedbacks import routes as feedback_routes WAITING


routes = (question_routes + survey_routes)
# routes = (question_routes + survey_routes + feedback_routes) WAITING

for r in routes:
    mod.add_url_rule(
        r['rule'],
        endpoint=r.get('endpoint', None),
        view_func=r['view_func'],
**r.get('options', {}))

