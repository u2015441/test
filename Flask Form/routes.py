from flask import render_template, flash, redirect
from flask import Flask
from config import Config
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=False)
    phone = db.Column(db.String(120), index=True, unique=False)
    age = db.Column(db.Integer, index=True, unique=False)
    company = db.Column(db.String(20), index=True, unique=False)

    def __repr__(self):
        return '<id={}, User {}, email {}, phone {}, age {}, company {} >'.format(self.id, self.username, self.email,
                                                                                  self.phone, self.age, self.company)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone No.')
    age = IntegerField('Age')
    company = StringField('Company')
    submit = SubmitField('Submit')


@app.route('/')
@app.route('/index')
def submit():
    form = LoginForm()
    return render_template('form.html', title='Forum Submit', form=form)


@app.route('/register', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Submission requested By user {}, Email {}, Phone No {}, Age {} ,Company {}'.format(
            form.username.data, form.email.data, form.phone.data, form.age.data, form.company.data))
        u = User(username=form.username.data, email=form.email.data, phone=form.phone.data, age=form.age.data,
                 company=form.company.data)
        db.session.add(u)
        db.session.commit()
        return redirect('/data')

    return render_template('form.html', title='Forum Submit', form=form)


@app.route('/data')
def data():
    user = User.query.all()
    return render_template('data.html', user=user, title='data')



app.run(debug=True)