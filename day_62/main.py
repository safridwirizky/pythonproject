from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField, URLField
from wtforms.validators import DataRequired
from pathlib import Path
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = URLField(label='Location', validators=[DataRequired()])
    open = TimeField(label='Open', validators=[DataRequired()])
    close = TimeField(label='Close', validators=[DataRequired()])
    coffee = SelectField(
        label='Coffee',
        choices=[
            ('✘', '✘'),
            ('☕️', '☕️'),
            ('☕️☕️', '☕️☕️'),
            ('☕️☕️☕️', '☕️☕️☕️'),
            ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
            ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')
        ],
        validators=[DataRequired()]
        )
    wifi = SelectField(
        label='Wifi', 
        choices=[
            ('✘', '✘'),
            ('💪', '💪'),
            ('💪💪', '💪💪'),
            ('💪💪💪', '💪💪💪'),
            ('💪💪💪💪', '💪💪💪💪'),
            ('💪💪💪💪💪', '💪💪💪💪💪')
        ],
        validators=[DataRequired()]
        )
    power = SelectField(
        label='Power', 
        choices=[
            ('✘', '✘'),
            ('🔌', '🔌'),
            ('🔌🔌', '🔌🔌'),
            ('🔌🔌🔌', '🔌🔌🔌'),
            ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
            ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')
        ],
        validators=[DataRequired()]
        )
    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(Path(__file__).resolve().parent / 'cafe-data.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow([
                form.cafe.data,
                form.location.data,
                form.open.data,
                form.close.data,
                form.coffee.data,
                form.wifi.data,
                form.power.data
            ])
        
        flash('Data berhasil disimpan! 🎉')
        
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)



@app.route('/cafes')
def cafes():
    with open(Path(__file__).resolve().parent / 'cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
