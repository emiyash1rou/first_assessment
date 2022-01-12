
from website import create_app
app = create_app()
if __name__=="__main__":
    app= create_app()

    @app.route("/")
    def home():
        return "<h1>Hello World</h1>"
    @app.route("/profile")
    def profile():
        return "<h1>Profile</h1>"
    app.run(debug=True)
