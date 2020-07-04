from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name







@app.route('/', methods=['POST', 'GET'])
def cat():
    categories = Category.query.all()
    if request.method == "POST":
        if "Add" in request.form:
            name = request.form['name']
            category = Category(name=name)
            db.session.add(category)
            db.session.commit()
            return redirect('/')

        if "Delete" in request.form:
            check = request.form.getlist('check')
            for i in range(len(check)):
                print(check[i])
                categ = Category.query.filter_by(id=int(check[i])).first_or_404()
                db.session.delete(categ)
                db.session.commit()

    return render_template("category.html", categories=categories)




if __name__ == "__main__":
    app.run(debug=True)
