from django.shortcuts import render, redirect
from .models import Course, Course_resource, Course_category, Course_subcategory

# List all courses
def course_list(request):
    courses = Course.objects.all().values()
    return render(request, 'courses/courses.html', {'Courses' : courses})

def new_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('coursename')
        category_name = request.POST.get('categoryname')
        subcategory_name = request.POST.get('subcategoryname')
        course_difficulty = request.POST.get('coursedifficulty')
        course_description = request.POST.get('coursedescription')
        resource = request.POST.get('numResource')
        response = redirect('/course/course_resource')
        course_cat = Course_category(category_name=category_name)
        course_cat.save()
        course_subcat = Course_subcategory(subcategory_name=subcategory_name,
                                            category=course_cat)
        course_subcat.save()
        course = Course(
            subcategory=course_subcat,
            subcategory_name=subcategory_name,
            category_name=category_name,
            course_name=course_name,
            course_difficulty=course_difficulty,
            course_description=course_description,
        )
        course.save()
        resources = []
        for i in range(int(resource)):
            resources.append('Resource '+str(i+1))
        response.set_cookie('resources', resources)
        response.set_cookie('course_id', course.course_id)
        return response
    return render(request, 'courses/new_course.html')

def course_resource(request):
    resources = request.COOKIES.get('resources')
    resources = resources[1:-1].replace("'", "").split(',')
    if request.method == 'POST':
        res = len(resources)
        course = Course.objects.filter(course_id=request.COOKIES.get('course_id'))[0]
        for resource in resources:
            Course_res = Course_resource(
                course=course,
                resourse_name=request.POST.get(resource+'_name'),
                resourse_link=request.POST.get(resource+'_link'),
                resourse_length=request.POST.get(resource+'_length'),
            )
            Course_res.save()
    return render(request, 'courses/course_resource.html', {'resources' : resources })

def edit_course(request, courseID):
    course = Course.objects.filter(course_id=courseID).values()
    if request.method == 'POST':
        course_name = request.POST.get('coursename')
        category_name = request.POST.get('categoryname')
        subcategory_name = request.POST.get('subcategoryname')
        course_difficulty = request.POST.get('coursedifficulty')
        course_description = request.POST.get('coursedescription')
        course.update(
            subcategory_name=subcategory_name,
            category_name=category_name,
            course_name=course_name,
            course_difficulty=course_difficulty,
            course_description=course_description,
        )
        return redirect('/course/list_course')
    return render(request, 'courses/edit_course.html', {'data' : course[0]})

def delete_course(request, courseID):
    Course.objects.filter(course_id=courseID).delete()
    return redirect('/course/list_course')

# Course pages
def uicourses(request):
    if request.COOKIES.get('username') == None or request.COOKIES.get('username') == 'None':
        return redirect('/user/login')
    uicourse = Course.objects.filter(course_id=2)
    uicourse_resource = Course_resource.objects.filter(course=uicourse[0])
    similar = Course.objects.filter(category_name=uicourse[0].category_name)
    return render(request, 'courses/course.html', {'course' : uicourse[0], 'course_resource' : uicourse_resource, 'similar' : similar, 'lectures' : len(uicourse_resource)})

def backend(request):
    return render(request, 'courses/backend.html')
def coreui(request):
    return render(request, 'courses/coursespage/coreui.html')

def fullstack(request):
    return render(request, 'courses/fullstack.html')

def functionaltesting(request):
    return render(request, 'courses/functionaltesting.html')

def mobility(request):
    return render(request, 'courses/mobility.html')

def devops(request):
    return render(request, 'courses/devops.html')

def datascience(request):
    return render(request, 'courses/datascience.html')

def cloud(request):
    return render(request, 'courses/cloud.html')

def cyber(request):
    return render(request, 'courses/cyber.html')

def digital(request):
    return render(request, 'courses/digital.html')

def erp(request):
    return render(request, 'courses/erp.html')

def it(request):
    return render(request, 'courses/it.html')

def itcertification(request):
    return render(request, 'courses/itcertification.html')

def coreui(request):
    return render(request, 'courses/coursepage/uicourses.html')

def advancedui(request):
    return render(request, 'courses/coursepage/advancedui.html')

def angularjs(request):
    return render(request, 'courses/coursepage/angularjs.html')

def reactjs(request):
    return render(request, 'courses/coursepage/reactjs.html')

def vuejs(request):
    return render(request, 'courses/coursepage/vuejs.html')

def java(request):
    return render(request, 'courses/coursepage/java.html')

def dotnet(request):
    return render(request, 'courses/coursepage/dotnet.html')

def nodejs(request):
    return render(request, 'courses/coursepage/nodejs.html')

def coursedetails(request):
    return render(request, 'courses/coursedetails.html')


#subcurses

def advancejava(request):
    return render(request, 'courses/coursepage/advancejava.html')
def dotnetcore(request):
    return render(request,
                   'courses/coursepage/dotnetcore.html')
def adwordexpert(request):
    return render(request, 'courses/coursepage/adwordexpert.html')
def adwordsfoundation(request):
    return render(request, 'courses/coursepage/adwordsfoundation.html')

def agile(request):
    return render(request, 'courses/coursepage/agile.html')



def aimlfoundationcourse(request):
    return render(request, 'courses/coursepage/aimlfoundationcourse.html')



def aimlexpertcourse(request):
    return render(request, 'courses/coursepage/aimlexpertcourse.html')
def android(request):
    return render(request, 'courses/coursepage/android.html')
def ansible(request):
    return render(request, 'courses/coursepage/ansible.html')

def automation(request):
    return render(request, 'courses/coursepage/automation.html')


def awscloudpractitioner(request):
    return render(request, 'courses/coursepage/awscloudpractitioner.html')


def awsdeveloperassociate(request):
    return render(request,'courses/coursepage/awsdeveloperassociate.html')

def awssolutionarchitectassociate(request):
    return render(request,'courses/coursepage/awssolutionarchitectassociate.html')

def awssolutionarchitectassociate(request):
    return render(request,'courses/coursepage/awssolutionarchitectassociate.html')
 
def awssysopsassociateadministrator(request):
    return render(request,'courses/coursepage/awssysopsassociateadministrator.html')
  
def awstechnicalessentials(request):
    return render(request,'courses/coursepage/awstechnicalessentials.html')
  
def branding(request):
    return render(request,'courses/coursepage/branding.html')
  
  
def ccsp(request):
    return render(request,'courses/coursepage/ccsp.html')


def ceh(request):
    return render(request,'courses/coursepage/ceh.html')


def cisa(request):
    return render(request,'courses/coursepage/cisa.html')


def chef(request):
    return render(request,'courses/coursepage/chef.html')

def cism(request):
    return render(request,'courses/coursepage/cism.html')
def smm(request):
    return render(request,'courses/coursepage/smm.html')
def smo(request):
    return render(request,'courses/coursepage/smo.html')
def cloudtesting(request):
    return render(request,'courses/coursepage/cloudtesting.html')
def comptiasecurity(request):
    return render(request,'courses/coursepage/comptiasecurity.html')

def contentmarketing(request):
    return render(request,'courses/coursepage/contentmarketing.html')


def corejava(request):
    return render(request,'courses/coursepage/corejava.html')


def dataanalytics(request):
    return render(request,'courses/coursepage/dataanalytics.html')


def datascientistcertification(request):
    return render(request,'courses/coursepage/datascientistcertification.html')


def deeplearning(request):
    return render(request,'courses/coursepage/deeplearning.html')



def devopsexpert(request):
    return render(request,'courses/coursepage/devopsexpert.html')



def devopsfoundation(request):
    return render(request,'courses/coursepage/devopsfoundation.html')


def digitalmarketingexpert(request):
    return render(request,'courses/coursepage/digitalmarketingexpert.html')

def digitalmarketingfoundation(request):
    return render(request,'courses/coursepage/digitalmarketingfoundation.html')



def docker(request):
    return render(request,'courses/coursepage/docker.html')




def dsbootcamp(request):
    return render(request,'courses/coursepage/dsbootcamp.html')



def flutter(request):
    return render(request,'courses/coursepage/flutter.html')

def fullstacknet(request):
    return render(request,'courses/coursepage/fullstacknet.html')


def fullstacktesting(request):
    return render(request,'courses/coursepage/fullstacktesting.html')


def golang(request):
    return render(request,'courses/coursepage/golang.html')


def hadoop(request):
    return render(request,'courses/coursepage/hadoop.html')




def inforln(request):
    return render(request,'courses/coursepage/inforln.html')


def ionic(request):
    return render(request,'courses/coursepage/ionic.html')


def ios(request):
    return render(request,'courses/coursepage/ios.html')



def itilfoundation(request):
    return render(request,'courses/coursepage/itilfoundation.html')


def kubernets(request):
    return render(request,'courses/coursepage/kubernets.html')


def manualtesting(request):
    return render(request,'courses/coursepage/manualtesting.html')


def mean(request):
    return render(request,'courses/coursepage/mean.html')


def measn(request):
    return render(request,'courses/coursepage/measn.html')



def mevn(request):
    return render(request,'courses/coursepage/mevn.html')


def microsoftazureexpertcertification(request):
    return render(request,'courses/coursepage/microsoftazureexpertcertification.html')

def microsoftazurefundamentals(request):
    return render(request,'courses/coursepage/microsoftazurefundamentals.html')



def microsoftdynamics(request):
    return render(request,'courses/coursepage/microsoftdynamics.html')

def mlwithpython(request):
    return render(request,'courses/coursepage/mlwithpython.html')

def naturallanguageprocessing(request):
    return render(request,'courses/coursepage/naturallanguageprocessing.html')


def onsenui(request):
    return render(request,'courses/coursepage/onsenui.html')


def openstack(request):
    return render(request,'courses/coursepage/openstack.html')

def oracle(request):
    return render(request,'courses/coursepage/oracle.html')

def pmiacp(request):
    return render(request,'courses/coursepage/pmiacp.html')


def pmp(request):
    return render(request,'courses/coursepage/pmp.html')


def prince2(request):
    return render(request,'courses/coursepage/prince2.html')


def python(request):
    return render(request,'courses/coursepage/python.html')



def reactnative(request):
    return render(request,'courses/coursepage/reactnative.html')



def remedy(request):
    return render(request,'courses/coursepage/remedy.html')
def servicenow(request):
    return render(request,'courses/coursepage/servicenow.html')


def rootstack(request):
    return render(request,'courses/coursepage/rootstack.html')

def rprogramming(request):
    return render(request,'courses/coursepage/rprogramming.html')
def ruby(request):
    return render(request,'courses/coursepage/ruby.html')

def rubyfullstack(request):
    return render(request,'courses/coursepage/rubyfullstack.html')


def salesforce(request):
    return render(request,'courses/coursepage/salesforce.html')


def sap(request):
    return render(request,'courses/coursepage/sap.html')



def scm(request):
    return render(request,'courses/coursepage/scm.html')


def seo(request):
    return render(request,'courses/coursepage/seo.html')

def xamarin(request):
    return render(request,'courses/coursepage/xamarin.html')

def vuejs(request):
    return render(request,'courses/coursepage/vuejs.html')






















  
