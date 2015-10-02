# -*- coding: utf-8 -*-

if not request.env.web2py_runtime_gae:
    
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    
    db = DAL('google:datastore+ndb')
   
    session.connect(request, response, db=db)
    


response.generic_patterns = ['*'] if request.is_local else []

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()
service = Service()
plugins = PluginManager()
not_empty = IS_NOT_EMPTY()
auth.settings.extra_fields['auth_user'] = [
    Field('Mobile','decimal(10,0)',
          writable=True,readable=True),
    Field('City','string',
          writable=True,readable=True)]
db.define_table(
    'cases',
    Field('law_id','string'),
    Field('first_name','string'),
    Field('last_name','string'),
    Field('email','string',requires=IS_EMAIL(),unique=True),
    Field('Case_Description','text',default='0'),
    Field('mobile_number','decimal(10,0)',required=not_empty),
    Field('Summon_date','date',requires=not_empty))
db.define_table(
    'quer',
    Field('case_id','string'),
    Field('person','string'),
    Field('Msg','text'))
db.define_table(
    'rating',
    Field('email','string'),
    Field('rating','string'),
    Field('person_count','decimal(10,0)'),
Field('feedback','text'))
db.define_table(
    'feedb',
    Field('name','string'),
    Field('feedback','text'))
auth.define_tables(username=False, signature=False)


mail = auth.settings.mailer
mail.settings.server ='smtp.gmail.com:587'
mail.settings.sender ='lawyer.interaction@gmail.com'
mail.settings.login = 'lawyer.management@gmail.com:managementsystem'


auth.settings.registration_requires_verification = True
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
auth.messages.verify_email = 'Click on the link http://' + request.env.http_host + URL(r=request,c='default',f='user',args=['verify_email']) + '/%(key)s to verify your email'
auth.messages.reset_password = 'Click on the link http://' + request.env.http_host + URL(r=request,c='default',f='user',args=['reset_password']) + '/%(key)s to reset your password'


from gluon.contrib.login_methods.janrain_account import use_janrain
use_janrain(auth, filename='private/janrain.key')
auth.settings.login_next = URL('lawhome')
auth.settings.register_next = URL('lawhome')
