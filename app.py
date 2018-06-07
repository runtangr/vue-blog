from collections import OrderedDict

from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware

import config
from views.api import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

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
    app.run(host='0.0.0.0', port=5000, debug=app.debug, threaded=True)
