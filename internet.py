import socket
from flask import *
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