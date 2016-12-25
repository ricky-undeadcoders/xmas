from os.path import join as path_join
from flask import Flask, g, request, Response, render_template, url_for


#################################################
# INITIALIZE FLASK APP,
# REGISTER BLUE PRINTS
#################################################
app = Flask(import_name=__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


#################################################
# ERROR HANDLING
#################################################

@app.errorhandler(404)
def page_not_found(e):
    return '404 Not Found :-(', 404


@app.errorhandler(405)
def method_not_allowed(e):
    return 'Server Error', 405


@app.errorhandler(500)
def server_error(e):
    return '500 error', 500


#################################################
# RUN SCRIPTS
#################################################

def test_run():
    app.run(debug=True, host='127.0.0.1')


if __name__ == "__main__":
    test_run()
