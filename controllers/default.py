import random
from gluon.tools import Mail
from Crypto.Cipher import AES
import base64
import datetime
def index():
    return dict()
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())
@auth.requires_login()
def lawhome():
    s=auth.user
    l_id=s['id']
    t=str(l_id)
    l_id=t
    rows = db(db.cases).select()
    x=datetime.date.today()
    a1=x+datetime.timedelta(days=1)
    a2=a1+datetime.timedelta(days=1)
    a3=a2+datetime.timedelta(days=1)
    a4=a3+datetime.timedelta(days=1)
    a5=a4+datetime.timedelta(days=1)
    a6=a5+datetime.timedelta(days=1)
    a7=a6+datetime.timedelta(days=1)
    return locals()
def cases():
    return locals()
def cases1():
    s=auth.user
    fname = request.vars.firstname
    lname = request.vars.lastname
    ema = request.vars.email
    mobile = request.vars.mno
    sdate = request.vars.dat
    ta = request.vars.txt
    db.cases.insert(law_id=s['id'],first_name=fname,last_name=lname,email=ema,Case_Description=ta,mobile_number=mobile,Summon_date=sdate)
    redirect(URL('lawhome'))
    return locals()
def actions():
    xm=request.vars.rd
    session.myv=xm
    list_val=request.vars.list
    if(list_val == 'view'):
        redirect(URL('casedetails'))
    elif(list_val == 'summon'):
        redirect(URL('summon_edit'))
    elif(list_val == 'close'):
        db(db.cases.id==xm).delete()
        redirect(URL('lawhome'))
    elif(list_val == 'dis'):
        redirect(URL('description_temp'))
    return locals()
@auth.requires_login()
def casedetails():
    rows = db(db.cases).select()
    df=session.myv
    return locals()
@auth.requires_login()
def summon_edit():
    return locals()
def summon_temp():
    dfe=session.myv
    xme=request.vars.dt
    if(xme != None):
        rows = db(db.cases.id==dfe).select().first()
        rows.update_record(Summon_date=xme)
        redirect(URL('lawhome'))
    return locals()
@auth.requires_login()
def description_temp():
    return locals()
def change_description():
    dfe=session.myv
    xme=request.vars.txt
    if(xme != None):
        rows = db(db.cases.id==dfe).select().first()
        rows.update_record(Case_Description=xme)
        redirect(URL('lawhome'))
    return locals()
def client_case_search():
    return locals()
def client_case_view():
    rows = db(db.cases).select()
    case_id=request.vars.cid
    mobile=request.vars.phn
    email_id=request.vars.eid
    return locals()
def search_lawyer():
    rows = db(db.auth_user).select()
    return locals()
def lawyer_found():
    city=request.vars.city
    rows = db(db.auth_user).select()
    rows1 = db(db.rating).select()
    return locals()
def client_enter():
    return locals()
def common():
    return locals()
def processs():
    rows = db(db.cases).select()
    rows1 = db(db.auth_user).select()
    case_id=request.vars.cid
    session.ci=case_id
    email_id=request.vars.eid
    return locals()
def queries():
    case_id=session.ci
    client_on=session.cli
    rows = db(db.quer).select()
    return locals()
def enter_msg():
    cid=session.ci
    client_on=session.cli
    xme=request.vars.txt
    if(client_on == 0):
        pers='Lawyer'
    else:
        pers='Client'
    db.quer.insert(case_id=cid,person=pers,Msg=xme)
    redirect(URL('queries'))
    return locals()

def rating_feedback():
    return locals()

def rating_temp():
    el = request.vars.leid
    ratng = request.vars.points
    fb = request.vars.txt
    rows = db(db.rating).select()
    flag=0
    for row in rows:
        if str(el) == str(row.email):
            flag=1
            t_rating = int(row.rating)
            t_count = int(row.person_count)
            break
    if flag==0:
        db.rating.insert(email=el,rating=ratng,person_count=1,feedback=fb)
        redirect(URL('index'))
    elif flag==1:
        ratng=int(ratng)+t_rating
        t_count = int(t_count) +1
        k = db(db.rating.email==el).select().first()
        k.update_record(rating=ratng,person_count=t_count,feedback=fb)
        redirect(URL('index'))
    return locals()
def send_mail():
    mail = Mail()
    mail.settings.server = 'smtp.gmail.com:587'
    mail.settings.sender = 'lawyer.management@gmail.com'
    mail.settings.login = 'lawyer.management@gmail.com:managementsystem'
    
    msg='Hello and hiii folks'
    snd='tushanjain00@gmail.com'
    mail.send(to=[snd],
    subject='Khaale',
    message=msg)
    return locals()
def datee():
    return locals()
def feed():
    rows = db(db.feedb).select()
    return locals()
def enter_feedback():
   name = request.vars.name
   txt = request.vars.txt
   db.feedb.insert(name=name,feedback=txt)
   redirect(URL('feed'))
   return locals()
def test():
    redirect('http://www.vakilno1.com/bareacts/indianpenalcode/indianpenalcode.html')
    return locals()
