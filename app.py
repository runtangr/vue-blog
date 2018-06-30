from collections import OrderedDict

from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware

import config
from views.api import api
from views import home


def create_app():
    app = Flask(__name__, static_folder = "./dist/static",
            template_folder = "./dist")
    app.config.from_object(config)

    app.register_blueprint(home.home_bp)
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, OrderedDict((
        ('/api', api),
    )))
    return app


app = create_app()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, debug=app.debug, threaded=True)
