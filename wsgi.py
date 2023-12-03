from flaskapp import create_app

app = create_app()
app.config["APPLICATION_ROOT"] = "/flaskappdemo/"