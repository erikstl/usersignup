import webapp2


content_header = ""

content = """
<form method="post" action="/signup">
    <label>First Name:</label> <input type="text" name="fname"><br>
    <label>Last Name:</label> <input type="text" name="lname"><br>
    <label>email:</label> <input type="text" name="email"><br>
    <label>Password:</label> <input type="password" name="password"><br>
    <label>Repeat Password:</label> <input type="password" name="password2"><br>
    <button>Sign Up</button>
</form>
"""

username = ""
email = ""

def build_page(fname,lname,email,password,password2):
    username_label = "<label><p>Name: </p></label>"
    username_input = "<input type='text' name='username' value='" + username + "'/>"

    email_label = "<label><p>EMail: </p></label>"
    email_input = "<input type='text' name='email' value='" + email + "'/>"

    password_label = "<label><p>Password: </p></label>"
    password_input = "<input type='text' name='password'>"

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


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(build_page("a","b","c","d","e"))


class SignUpHandler(webapp2.RequestHandler):
    def post(self):
        pw = self.request.get("password")
        pw2 = self.request.get("password2")
        if pw != pw2:
            error = "Please be sure passwords match"



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', SignUpHandler)
], debug=True)
