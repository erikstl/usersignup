import webapp2


#content_header = ""

#content = """
#<form method="post" action="/signup">
#    <label>First Name:</label> <input type="text" name="fname"><br>
#    <label>Last Name:</label> <input type="text" name="lname"><br>
#    <label>email:</label> <input type="text" name="email"><br>
#    <label>Password:</label> <input type="password" name="password"><br>
#    <label>Repeat Password:</label> <input type="password" name="password2"><br>
#    <button>Sign Up</button>
#</form>
#"""

username = ""
email = ""
uError = ""
pError = ""
eError = ""

def build_page(username='',uError='',eError='',pError=''):
    username_label = "<label><p>Name: </p></label>"
    username_input = "<input type='text' name='username' value='" + username + "'/> {0}".format(uError)

    email_label = "<label><p>EMail: </p></label>"
    email_input = "<input type='text' name='email' value='" + email + "'/> {0}".format(eError)

    password_label = "<label><p>Password: </p></label>"
    password_input = "<input type='text' name='password'> {0}".format(pError)

    password2_label = "<label><p>Repeat Password: </p></label>"
    password2_input = "<input type='text' name='password2'>"

    submit_button = "<input type='submit' value='Sign Up'>"

    form = ("<form method='post'>" +
            username_label + username_input +
            email_label + email_input + password_label + password_input +
            password2_label + password2_input +
            "<br>" + submit_button +
            "</form>")

    return form


class Index(webapp2.RequestHandler):
    def get(self):
        self.response.write(build_page('','','',''))

    def post(self):
        pw = self.request.get('password')
        pw2 = self.request.get('password2')
        username = self.request.get('fname')
        email = self.request.get('email')

        if pw != pw2:
            pError = "Please be sure passwords match"
        else:
            pError = ""

        content = build_page(username,uError,eError,pError)

        self.response.write(content)




app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
