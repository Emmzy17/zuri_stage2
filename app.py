import os

from flask import Flask, render_template, url_for, redirect
from form import ContactForm
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['SECRET_KEY']='1231QA'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ["EMAIL_ADDRESS"]
app.config['MAIL_PASSWORD'] = "$$BufferOverFlowError33"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		msg = Message(form.subject.data, sender=form.email.data, recipients=["fredpwol@gmail.com"])
		msg.body = "From %s \n %s"%(form.name.data, form.message.data)
		mail.send(msg)
		return redirect(url_for('about'))
	return render_template('resume.html', form=form)
@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)
