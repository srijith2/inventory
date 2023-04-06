import socket
from flask import *

app = Flask(__name__)
class internet_checker:
    def isConnect():
        try:
            s = socket.create_connection(
                ("www.geeksforgeeks.org", 80))
            if s is not None:
                s.close
            return True
        except OSError:
            pass
        return False

if internet_checker.isConnect():
    print("Yes")
else:
    render_template("no_internet.html")
    

if __name__ == "__main__":
    #secret_key for session
    app.run(debug=True)

