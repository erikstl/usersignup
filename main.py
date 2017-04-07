import webapp2
import re

username = ""
email = ""
uError = ""
pError = ""
eError = ""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
PASS_RE = re.compile("^.{3,20}$")

def valid_username(username):
    return USER_RE.match(username)

def valid_email(email):
    return EMAIL_RE.match(email)

def valid_password(password):
    return PASS_RE.match(password)

def build_page(username='',uError='',eError='',pError=''):
    username_label = "<label><p>Name: </p></label>"
    username_input = "<input type='text' name='username' value='" + username + "'/> {0}".format(uError)

    email_label = "<label><p>EMail: </p></label>"
    email_input = "<input type='text' name='email' value='" + email + "'/> {0}".format(eError)

    password_label = "<label><p>Password: </p></label>"
    password_input = "<input type='password' name='password'> {0}".format(pError)

    password2_label = "<label><p>Repeat Password: </p></label>"
    password2_input = "<input type='password' name='password2'>"

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
        username = self.request.get('username')
        email = self.request.get('email')

        if not valid_username(username):
            uError = "That is not a valid username"
        else:
            uError = ""

        if pw != pw2:
            pError = "Please be sure passwords match"
        elif not valid_password(pw):
            pError = "Please enter a valid password"
        else:
            pError = ""

        if email == "":
            eError = ""
        elif not valid_email(email):
            eError = "Please enter a valid email address"
        else:
            eError = ""


        content = build_page(username,uError,eError,pError)

        self.response.write(content)




app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
