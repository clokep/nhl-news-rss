from flask import Flask

from parser import main

application = Flask(__name__)


@application.route("/")
def serve():
    return main()


if __name__ == "__main__":
    application.run()
