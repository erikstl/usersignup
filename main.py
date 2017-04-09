import webapp2
import re

#username = ""
#email = ""
#uError = ""
#pError = ""
#eError = ""


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
PASS_RE = re.compile("^.{3,20}$")

def valid_username(username):
    return USER_RE.match(username)

def valid_email(email):
    return EMAIL_RE.match(email)

def valid_password(password):
    return PASS_RE.match(password)

def build_page(username='',email='',uError='',eError='',pError='',vError=''):
    username_label = "<label><p>Name: </label>"
    username_input = "<input type='text' name='username' value='" + username + "'/> {0}</p>".format(uError)

    email_label = "<label><p>EMail: </label>"
    email_input = "<input type='text' name='email' value='" + email + "'/> {0}</p>".format(eError)

    password_label = "<label><p>Password: </label>"
    password_input = "<input type='password' name='password'> {0}</p>".format(pError)

    password2_label = "<label><p>Repeat Password: </label>"
    password2_input = "<input type='password' name='password2'> {0}</p>".format(vError)

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
        self.response.write(build_page('','','','',''))

    def post(self):
        pw = self.request.get('password')
        pw2 = self.request.get('password2')
        username = self.request.get('username')
        email = self.request.get('email')
        error = False

        if not valid_username(username):
            uError = "That is not a valid username"
            error = True
        else:
            uError = ""

        if not valid_password(pw):
            pError = "Please enter a valid password."
            error = True
        else:
            pError = ""

        if pw != pw2:
            vError = "Please be sure passwords match."
            error = True
        else:
            vError = ""

        if email == "":
            eError = ""
        elif not valid_email(email):
            eError = "Please enter a valid email address"
            error = True
        else:
            eError = ""

        if error:
            content = build_page(username,email,uError,eError,pError,vError)
            self.response.write(content)
        else:
            self.redirect('/welcome/?username={0}'.format(username))


class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        message = '<h1>Welcome, ' + username + '!</h1>'
        self.response.write(message)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome/', Welcome)
], debug=True)
