from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import User, adminUser, instructor, entity, program_details, subprogram_details, course_names
import hashlib, jwt, datetime
from django.http import HttpResponse

salt = b'vB\\xa6\\xc4M(\\x07\\xbd\\xcc\\x00\\xf5*\\x93\\xb9\\xdb{\\xa4)\\xa4\\xff\\xe3_Z\\x87<\\xc4\\xcc\\x93\\xe5\\xa3\\x8f\\xdb'

# Main page
def index(request):
    return render(request, 'index.html')

# User related pages
def user_login(request):
    try:
        if len(request.COOKIES.get('username')) > 0 and (request.COOKIES.get('type') == 'student' or request.COOKIES.get('type') == 'professional'):
            return redirect('/ugser/successLoin')
    except Exception as e:
        pass
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            student = User.objects.get(email=email)
            if student.password == str(key):
                response = redirect('/user/successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', student.user_type)
                return response
            else:
                return render(request, 'login.html', {'state': 2})
        except Exception as e:
            return render(request, 'login.html', {'state': 3})
    return render(request, 'login.html')

def user_register(request): 
    if request.method == 'POST':
        global salt
        try:
            typeUser = request.POST.get('typeUser')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            phone = int(request.POST.get('phone'))
            birthDate = request.POST.get('birthDate')
            password = request.POST.get('password')
            country = request.POST.get('country')
            state = request.POST.get('state')
            college = request.POST.get('college')
            skills = request.POST.get('skill')
            student = User.objects.filter(email=email)
            if len(student) > 0:
                return render(request, 'register.html', {'state': 3})
            student = User(
                first_name=fname,
                last_name=lname,
                user_type=typeUser,
                email=email,
                phone=phone,
                birth_date = birthDate,
                country=country,
                state=state,
                college=college,
                skill_set=skills,
                password=str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)),
            )
            student.save()
            return render(request, 'register.html', {'state': 2})
        except Exception as e:
            return render(request, 'register.html', {'state': 4})
    return render(request, 'register.html')

def forgot_password(request):
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        typeUser = request.POST.get('typeUser')
        if typeUser == 'user':
            user = User.objects.filter(email=email)
        elif typeUser == 'instructor':
            user = instructor.objects.filter(email=email)
        elif typeUser == 'entity':
            user = entity.objects.filter(email=email)
        elif typeUser == 'admin':
            user = adminUser.objects.filter(email=email)
        if len(user) == 0:
            return render(request, 'forgotPassword.html', {'state': 2})
        else:
            user = user[0]
            encoded_jwt = jwt.encode({'email': user.email, 'type': typeUser, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15)}, 'caramelitdjangosecretkeytoken', 'HS256')
            try:
                msg = "Hello,\nYou requested a password change for your profile.\nHere is your link to change your password: http://127.0.0.1:8000/changePassword/"+str(encoded_jwt)[2:-1]+"\nThis link will expire in 15 minutes"
                send_mail("Password Reset", msg, 'Madarauchiha3524@gmail.com', [user.email], fail_silently=False,)
                return render(request, 'forgotPassword.html', {'state': 3})
            except Exception as e:
                return render(request, 'forgotPassword.html', {'state': 4})
    return render(request, 'forgotPassword.html')

def changePassword(request, token):
    global salt
    data = ''
    try:
        data = jwt.decode(token, 'caramelitdjangosecretkeytoken', algorithms='HS256')
        if data['type'] == 'user':
            user = User.objects.filter(email=data['email'])
        elif data['type'] == 'instructor':
            user = instructor.objects.filter(email=data['email'])
        elif data['type'] == 'entity':
            user = entity.objects.filter(email=data['email'])
        elif data['type'] == 'admin':
            user = adminUser.objects.filter(email=data['email'])
        if len(user) == 0:
            return render(request, 'successResetPassword.html', {'state': 2})
    except Exception as e:
        return render(request, 'successResetPassword.html', {'state': 1})
    
    if request.method == 'GET':
        return render(request, 'successResetPassword.html', {'state': 3})
    if request.method == 'POST':
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        if data['type'] == 'user':
            user = User.objects.get(email=data['email'])
        elif data['type'] == 'instructor':
            user = instructor.objects.get(email=data['email'])
        elif data['type'] == 'entity':
            user = entity.objects.get(email=data['email'])
        elif data['type'] == 'admin':
            user = adminUser.objects.get(email=data['email'])
        user.password = str(key)
        user.save()
        return render(request, 'successResetPassword.html', {'state': 4})

def user_successLogin(request):
    username = request.COOKIES.get('username')
    usertype = request.COOKIES.get('type')
    if len(username) == 0:
        response = redirect('/user/login')
        response.set_cookie('username', None)
        response.set_cookie('type', None)
        return response
    if request.method == 'POST':
        student = User.objects.filter(email=username).values()
        student.update(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            state=request.POST.get('state'),
            college=request.POST.get('college'),
            highest_qualification=request.POST.get('highestQualification'),
            university_name=request.POST.get('universityName'),
            roll_no=request.POST.get('rollNo'),
            specialisation=request.POST.get('specialisation'),
            college_state=request.POST.get('collegeState'),
            skill_set=request.POST.get('skills'),
        )
        return redirect('/user/successLogin')
    student = User.objects.filter(email=username).values()
    data = student[0]
    if usertype == 'student':
        return render(request, 'successLogin.html', {'data': data})
    elif usertype == 'professional':
        return render(request, 'successLoginProfessional.html', {'data': data})

def logout(request):
    response = redirect('/user/login')
    response.set_cookie('username', None)
    response.set_cookie('type', None)
    return response

def successPasswordReset(request):
    return render(request, 'successResetPassword.html')

# Instructor related pages
def instructor_login(request):
    try:
        if len(request.COOKIES.get('username')) > 0 and request.COOKIES.get('type') == 'instructor':
            return redirect('/instructor/instructor_successLogin')
    except Exception as e:
        pass
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            instructor1 = instructor.objects.get(email=email)
            if instructor1.password == str(key):
                response = redirect('/instructor/instructor_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'instructor')
                return response
            else:
                return render(request, 'instructor_login.html', {'state': 2})
        except Exception as e:
            return render(request, 'instructor_login.html', {'state': 3})
    return render(request, 'instructor_login.html')

def instructor_register(request):
    if request.method == 'POST':
        global salt
        try:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            phone = int(request.POST.get('phone'))
            password = request.POST.get('password')
            subject = request.POST.get('subject')
            jobtype = request.POST.get('jobtype')
            experience = request.POST.get('experience')
            description = request.POST.get('description')
            instructor1 = instructor.objects.filter(email=email)
            if len(instructor1) > 0:
                return render(request, 'instructor_register.html', {'state': 3})
            instructor1 = instructor(
                first_name=fname,
                last_name=lname,
                email=email,
                phone=phone,
                subjects=subject,
                job_type=jobtype,
                experience=experience,
                description=description,
                password=str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)),
            )
            instructor1.save()
            return render(request, 'instructor_register.html', {'state': 2})
        except Exception as e:
            return render(request, 'instructor_register.html', {'state': 4})
    return render(request, 'instructor_register.html')

def instructor_successLogin(request):
    username = request.COOKIES.get('username')
    usertype = request.COOKIES.get('type')
    if len(username) == 0 or usertype != 'instructor':
        response = redirect('/instructor/instructor_login')
        response.set_cookie('username', None)
        response.set_cookie('type', None)
        return response
    if request.method == 'POST':
        instructor1 = instructor.objects.filter(email=username).values()
        instructor1.update(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            subjects=request.POST.get('subjects'),
            experience=request.POST.get('experience'),
            job_type=request.POST.get('role'),
            state=request.POST.get('state'),
            description=request.POST.get('description'),
            job_organisation_name=request.POST.get('jobOrganisation'),
            job_experience=request.POST.get('jobExperience'),
            job_location=request.POST.get('jobLocation'),
            job_state=request.POST.get('jobState'),
            skills=request.POST.get('skills'),
        )
        return redirect('/instructor/instructor_successLogin')
    instructor1 = instructor.objects.filter(email=username).values()
    data = instructor1[0]
    return render(request, 'instructor_successLogin.html', {'data': data})

def instructor_logout(request):
    response = redirect('/instructor/instructor_login')
    response.set_cookie('username', None)
    response.set_cookie('type', None)
    return response

# Entity related pages
def entity_login(request):
    try:
        if len(request.COOKIES.get('username')) > 0 and (request.COOKIES.get('type') == 'College' or request.COOKIES.get('type') == 'Organization'):
            return redirect('/entity/entity_successLogin')
    except Exception as e:
        pass
    if request.method == 'POST':
        global salt
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            entity1 = entity.objects.get(email=email)
            if entity1.password == str(key):
                response = redirect('/entity/entity_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', entity1.role)
                return response
            else:
                return render(request, 'entity_login.html', {'state': 2})
        except Exception as e:
            return render(request, 'entity_login.html', {'state': 3})
    return render(request, 'entity_login.html')

def entity_register(request):
    if request.method == 'POST':
        global salt
        try:
            first_name=request.POST.get('fname')
            last_name=request.POST.get('lname')
            email = request.POST.get('email')
            birthDate = request.POST.get('birthDate')
            phone = int(request.POST.get('phone'))
            password = request.POST.get('password')
            country = request.POST.get('Country')
            state = request.POST.get('state')
            skill = request.POST.get('skill_set')
            role = request.POST.get('inlineRadioOptions')
            entity1 = entity.objects.filter(email=email)
            if len(entity1) > 0:
                return render(request, 'entity_register.html', {'state': 3})
            if role == 'College':
                entity1 = entity(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    role=role,
                    birth_date=birthDate,
                    phone=phone,
                    country=country,
                    state=state,
                    university_name=request.POST.get('university_name'),
                    skill_set=skill,
                    college_name=request.POST.get('college'),
                    university_skill=request.POST.get('college_skill'),
                    description=request.POST.get('college_description'),
                    password=str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)),
                )
                entity1.save()
            elif role == 'Organization':
                entity1 = entity(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    role=role,
                    birth_date=birthDate,
                    phone=phone,
                    country=country,
                    state=state,
                    organisation_name=request.POST.get('organization_name'),
                    skill_set=skill,
                    college_name=request.POST.get('college'),
                    organisation_email=request.POST.get('organization_email'),
                    description=request.POST.get('organization_description'),
                    password=str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)),
                )
                entity1.save()
            return render(request, 'entity_register.html', {'state': 2})
        except Exception as e:
            return render(request, 'entity_register.html', {'state': 4})
    return render(request, 'entity_register.html')

def entity_successLogin(request):
    username = request.COOKIES.get('username')
    usertype = request.COOKIES.get('type')
    if len(username) == 0:
        response = redirect('/entity/entity_login')
        response.set_cookie('username', None)
        response.set_cookie('type', None)
        return response
    if request.method == 'POST':
        entity1 = entity.objects.filter(email=username).values()
        entity1.update(
            college_name=request.POST.get('collegeName'),
            university_name=request.POST.get('universityName'),
            university_type=request.POST.get('universityType'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            country=request.POST.get('country'),
            state=request.POST.get('state'),
            skill_set=request.POST.get('skills'),
            description=request.POST.get('description'),
        )
        return redirect('/entity/entity_successLogin')
    entity1 = entity.objects.filter(email=username).values()
    data = entity1[0]
    print(data)
    if usertype == 'College':
        return render(request, 'college_successLogin.html', {'data' : data})
    elif usertype == 'Organization':
        return render(request, 'organisation_successLogin.html', {'data': data})

def entity_logout(request):
    response = redirect('/entity/entity_login')
    response.set_cookie('username', None)
    response.set_cookie('type', None)
    return response

# Admin related pages
def admin_login(request):
    try:
        if len(request.COOKIES.get('username')) > 0 and request.COOKIES.get('type') == 'admin':
            return redirect('/admin/admin_successLogin')
    except Exception as e:
        pass
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            admin = adminUser.objects.get(email=email)
            if admin.password == str(key):
                response = redirect('/admin/admin_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'admin')
                return response
            else:
                return render(request, 'admin_login.html', {'state': 2})
        except Exception as e:
            return render(request, 'admin_login.html', {'state': 3})
    return render(request, 'admin_login.html')

def admin_register(request):
    if request.method == 'POST':
        global salt
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = int(request.POST.get('phone'))
            password = request.POST.get('password')
            admin1 = adminUser.objects.filter(email=email)
            if len(admin1) > 0:
                return render(request, 'admin_register.html', {'state': 3})
            admin1 = adminUser(
                name=name,
                email=email,
                phone=phone,
                password=str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)),
            )
            admin1.save()
            return render(request, 'admin_register.html', {'state': 2})
        except Exception as e:
            return render(request, 'admin_register.html', {'state': 4})
    return render(request, 'admin_register.html')

def admin_successLogin(request):
    username = request.COOKIES.get('username')
    usertype = request.COOKIES.get('type')
    if len(username) == 0:
        response = redirect('/admin/admin_login')
        response.set_cookie('username', None)
        response.set_cookie('type', None)
        return response
    admin = adminUser.objects.filter(email=username)[0]
    print(admin)
    return render(request, 'admin_successLogin.html', {'name': admin.name})

def admin_logout(request):
    response = redirect('/admin/admin_login')
    response.set_cookie('username', None)
    response.set_cookie('type', None)
    return response

def user_list(request):
    users_data = User.objects.all()
    return render(request, 'user_list.html', {'users': users_data})

def instructor_list(request):
    instructor_data = instructor.objects.all()
    return render(request, 'instructor_list.html', {'instructors': instructor_data})

def entity_list(request):
    entity_data = entity.objects.all()
    return render(request, 'entity_list.html', {'entities': entity_data})

def addprogram(request):
    if request.method == 'POST':
        program_name=request.POST['program']
        p=program_details(program=program_name )
        p.save()
    program_name=program_details.objects.all()     
    return render(request, 'admin_addstructure1.html', {'program_name':program_name })
    
def addprogram2(request):
    if request.method == 'POST':
        subprogram_name=request.POST['subprogram']
        program_name=request.POST['program_sub']
        p=subprogram_details(subprogram_name=subprogram_name,program=program_name )
        p.save()
    subprogram_name=subprogram_details.objects.all()     
    return render(request, 'admin_addstructure2.html', {'subprogram_name':subprogram_name })
         
def addprogram3(request):
    if request.method == 'POST':
        course_name=request.POST['coursename']
        image=request.POST['img']
        subprogram=request.POST['subprogram']
        
        p=course_names(course_name=course_name,subprogram=subprogram,img=image )
        p.save()
    subprogram_name=course_names.objects.all()     
        
    return redirect('/filter')

def display(request):
    program={}
    subprogram={}
    for idp,p in program_details.objects.values_list('id','program'):
        program[p]=[]
        for ids,sp in subprogram_details.objects.filter(program=p).values_list('id','subprogram_name'):
            program[p].append(sp)
            subprogram[sp]=[]
            for c in course_names.objects.filter(subprogram=sp):
                subprogram[sp].append(c)
    data=subprogram_details.objects.filter(program="").values_list('id','subprogram_name')
    return render(request,'display.html',{'program':program,'subprogram':subprogram})

def admin_manage(request):
    admin = adminUser.objects.filter(email=request.COOKIES.get('username')).values()[0]
    return render(request,'admin_manage.html', {'data': admin})

def admin_addstructure(request):
    return render(request,'admin_addstructure.html')

def admin_addstructure1(request):
    return render(request,'admin_addstructure1.html')

def admin_addstructure2(request):
    return render(request,'admin_addstructure2.html')