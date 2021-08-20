from flask import Flask, render_template, url_for, redirect
from form import ContactForm
app = Flask(__name__)
app.config['SECRET_KEY']='1231QA' 
@app.route('/', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		return redirect(url_for('about'))
	return render_template('resume.html', form=form)
@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)
