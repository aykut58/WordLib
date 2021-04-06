from flask import jsonify

class AuthenticationException(Exception):

    def __init__(self,*args:object,code):
        super().__init__(*args)
        self.code=code

def default_error_handler(exception):
    print(type(exception),str(exception))
    return jsonify({"Error":"Something Went Wrong"}),500

def authentication_error_handler(exception):
    return jsonify({"Error":str(exception)}),exception.code

def http_error_handler(exception):
    return jsonify({"Error":str(exception)}),exception.code

def data_error_handler(exception):
    print("data exception")
    print(type(exception),str(exception))
    return jsonify({"Error":str(exception)}),400