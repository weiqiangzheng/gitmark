from flask import Blueprint

from . import views

main = Blueprint('main', __name__)

main.add_url_rule('/hello/', 'hello', views.hello)
main.add_url_rule('/', 'index', views.index)
main.add_url_rule('/test-celery/', 'test-celery', views.test_celery)
main.add_url_rule('/test/', 'test', views.test)
main.add_url_rule('/import-repo/', view_func=views.ImportRepoView.as_view('import_repo'), defaults={'starred':True})
main.add_url_rule('/starred-repos/', view_func=views.StarredRepoView.as_view('starred_repos'))