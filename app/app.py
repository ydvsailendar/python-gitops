from flask import Flask
app = Flask(__name__)

@app.router("/")
def hello():
    return "Hello from Argo CD + Kubernetes\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


