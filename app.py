from flask import Flask, render_template

skills_app = Flask(__name__)

my_skills = [("html", 80), ("CSS", 75), ("Python", 95), ("MySQL", 45), ("JavaScript", 80), ("React JS", 80), ("Node JS", 70), ("MongoDB", 70)]


@skills_app.route("/")
def homepage():
    return render_template("homepage.html", pagetitle="Home", test="Hello H", custom_css="home")


@skills_app.route("/about")
def about():
    return render_template("about.html", pagetitle="About", test="Hello A")


@skills_app.route("/add")
def add():
    return render_template("add.html", pagetitle="add", test="Hello Add", custom_css="add")


@skills_app.route("/skills")
def skills():
    return render_template(
        "skills.html",
        pagetitle="My skills",
        page_head="My skills",
        description="This is my skills page",
        skills=my_skills,
        custom_css="skills"
    )


if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)
