from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Preethi Narayanan! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

#added the favorite course route
@app.route('/favorite-course')
def favorite_course():
    #this gets the subject and the course number
    subject = request.args.get('subject', '')
    course_number = request.args.get('course_number', '')

    return render_template(
        'favorite-course.html',
        subject=subject,
        course_number=course_number
    )

#added the contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    #this is if statement that displays the information if
    #the user enters
    if request.method == 'POST':
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        email = request.form.get('email', '')
        phone_number = request.form.get('phone_number', '')
        reason_for_contact = request.form.get('reason_for_contact', '')

        return render_template(
            'contact.html',
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            reason_for_contact=reason_for_contact,
            submitted=True
        )

#this returns the form again if the user does not submit
    return render_template('contact.html', submitted=False)

if __name__ == '__main__':
    app.run()
