from flask import Flask
app = Flask("Teste")

@app.route("/olamundo",methods=["GET"])
def olaMundo():
    return {"ola":"mundo"}

app.run()