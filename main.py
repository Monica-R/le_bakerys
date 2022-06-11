from bottle import (auth_basic, debug, error, get, post, redirect, request,
                    route, run, static_file, template)

from controller.register import RegistrationForm
from controller.contact import ContactForm
from model.users import Users
from model.modules import *

@get('/')
def index():
    return template('index')


@get('/admin')
@auth_basic(Modules.auth_admin)
def admin():
    return template('index')

@get('/registration')
def register():
    form = RegistrationForm(request.POST)
    return template('registration', form=form)

@get('/contact')
def register():
    form = ContactForm(request.POST)
    return template('contact', form=form)

@post('/registration')
def post_registration():
    form = RegistrationForm(request.POST) 
    if form.save.data:
        form_data = {
            'username' : form.username.data,
            'password' : form.password.data,
            'email' : form.email.data,
            'c_name' : form.c_name.data,
            'surname1' : form.surname1.data,
            'surname2' : form.surname2.data,
            'nid' : form.nid.data,
            'contact' : form.contact.data,
            'address' : form.address.data,
            'postal_code' : form.postal_code.data,
            'city' : form.city.data,
            'privacy_policy' : form.privacy_policy.data
        }
        keys = tuple(form_data.keys())
        values = tuple(form_data.values())
        clients.insert(values, keys)

        print(form_data)
        redirect('/')
    print(form.errors)
    return template('registration', form=form)

@get('/')
@get('/index')
def index():
    return static_file("index.html", root = "static")

@get('/users/clients')
def clients():
    pass

@get('/users/employee')
def employee():
    pass

@get('/products')
def products():
    return template("products")

@get('/order')
def order():
    pass

@error(404)
def error404(error):
    return static_file('404.html', root='static/src')
    
# Static Routes
@get("/static/styles/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/styles")

@get("/static/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="static/fonts")

@get("/static/resources/img/<filepath:re:.*\.(jpg|png|gif|ico|svg|jpeg|webp)>")
def img(filepath):
    return static_file(filepath, root="static/resources/img")

@get("/static/resources/video/<filepath:re:.*\.mp4>")
def video(filepath):
    return static_file(filepath, root="static/resources/video")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")



if __name__ == '__main__':
    run(host='localhost', port=8082, debug=True, reloader=True)
