from app import app,init_app

app.config.from_object("config.Config")
init_app()
if __name__=="__main__":
    app.run(host=app.config["HOST"])