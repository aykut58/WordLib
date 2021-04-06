from flask import jsonify,request

def default_error_handler(exception):
    #TODO log
    print(type(exception),str(exception),request.path,request.method)
    return jsonify({"Error":"Something Went Wrong"}),500

def http_error_handler(exception):
    return jsonify({"Error":str(exception)}),exception.code

def database_error_handler(exception):
    print(type(exception),str(exception))
    return jsonify({"Error":str(exception)}),500