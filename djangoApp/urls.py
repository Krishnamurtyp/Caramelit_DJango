"""djangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import loginRegister.views as loginviews
import staticHome.views as staticviews
import courses.views as courseviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Main page
    path('', staticviews.index, name="index"),
    path('aboutus', staticviews.aboutus, name="aboutus"),
    path('consortium', staticviews.consortium, name="consortium"),
    path('academy', staticviews.academy, name="academy"),
    path('products', staticviews.products, name="products"),
    path('program', staticviews.program, name="program"),
    path('changePassword/<str:token>', loginviews.changePassword, name='changePassword'),
    # Contact forms
    path('contact/contactform', staticviews.contactform, name="contactform"),
    path('contact/academycontact', staticviews.academycontact, name="academycontact"),
    path('contact/consortiumcontact', staticviews.consortiumcontact, name="consortiumcontact"),
    # User oriented pages
    path('user/login', loginviews.user_login, name='user_login'),
    path('user/register', loginviews.user_register, name='user_register'),
    path('user/forgot-password', loginviews.forgot_password, name='user_forgot_password'),
    path('user/successLogin', loginviews.user_successLogin, name='user_successLogin'),
    path('user/logout', loginviews.logout, name='user_logout'),
    # Instructor oriented pages
    path('instructor/instructor_login', loginviews.instructor_login, name='instructor_login'),
    path('instructor/instructor_register', loginviews.instructor_register, name='instructor_register'),
    path('instructor/instructor_forgot-password', loginviews.forgot_password, name='instructor_forgot_password'),
    path('instructor/instructor_successLogin', loginviews.instructor_successLogin, name='instructor_successLogin'),
    path('instructor/logout', loginviews.instructor_logout, name='instructor_logout'),
    # Entity oriented pages
    path('entity/entity_login', loginviews.entity_login, name='entity_login'),
    path('entity/entity_register', loginviews.entity_register, name='entity_register'),
    path('entity/entity_forgot-password', loginviews.forgot_password, name='entity_forgot_password'),
    path('entity/entity_successLogin', loginviews.entity_successLogin, name='entity_successLogin'),
    path('entity/logout', loginviews.entity_logout, name='entity_logout'),
    # Admin oriented pages
    path('admin/admin_login', loginviews.admin_login, name='admin_login'),
    path('admin/admin_register', loginviews.admin_register, name='admin_register'),
    path('admin/admin_forgot-password', loginviews.forgot_password, name='admin_forgot_password'),
    path('admin/admin_successLogin', loginviews.admin_successLogin, name='admin_successLogin'),
    
    path('admin/admin_manage', loginviews.admin_manage, name='admin_manage'),
    path('admin/addCourse', courseviews.new_course, name='admin_addCourse'),
    path('admin/new_course_resources', courseviews.course_resource, name='course_resource'),
    path('admin/save_course', courseviews.save_course, name='save_course'),

    path('admin/logout', loginviews.admin_logout, name='admin_logout'),
    path('admin/user_list', loginviews.user_list, name='user_list'),
    path('admin/instructor_list', loginviews.instructor_list, name='instructor_list'),
    path('admin/entity_list', loginviews.entity_list, name='entity_list'),
    path('admin/list_course', courseviews.course_list, name="course_list"),
    path('admin/new_course', courseviews.new_course, name="new_course"),
    path('admin/course_resource', courseviews.course_resource, name="course_resource"),
    path('admin/delete/<int:courseID>', courseviews.delete_course, name="delete_course"),
    path('admin/edit/<int:courseID>', courseviews.edit_course, name="edit_course"),
    path('admin/view/<int:courseID', courseviews.view_course, name="view_course"),
    # Industries related pages
    path('industries/automotive', staticviews.automotive, name="automotive"),
    path('industries/communication', staticviews.communication, name="communication"),
    path('industries/lifescience', staticviews.lifescience, name="lifescience"),
    path('industries/banking', staticviews.banking, name="banking"),
    path('industries/consumer', staticviews.consumer, name="consumer"),
    path('industries/travel', staticviews.travel, name="travel"),
    # Insights related pages
    path('insights/artificial', staticviews.artificial, name="artificial"),
    path('insights/blockchain', staticviews.blockchain, name="blockchain"),
    path('insights/iot', staticviews.iot, name="iot"),
    path('insights/futureworkforce', staticviews.futureworkforce, name="futureworkforce"),
    path('insights/cloudcomputing', staticviews.cloudcomputing, name="cloudcomputing"),
    path('insights/datascience', staticviews.datascience, name="datascience"),
    # Business related pages
    path('business/strategy', staticviews.strategy, name="strategy"),
    path('business/consulting', staticviews.consulting, name="consulting"),
    path('business/digital', staticviews.digital, name="digital"),
    path('business/technology', staticviews.technology, name="technology"),
    path('business/operations', staticviews.operations, name="operations"),
    path('business/Application', staticviews.Application, name="Application"),
    # Courses
    path('courses/backend', courseviews.backend, name="backend"),
    path('courses/fullstack', courseviews.fullstack, name="fullstack"),
    path('courses/functionaltesting', courseviews.functionaltesting, name="functionaltesting"),
    path('courses/mobility', courseviews.mobility, name="mobility"),
    path('courses/devops', courseviews.devops, name="devops"),
    path('courses/datascience', courseviews.datascience, name="datascience"),
    path('courses/cloud', courseviews.cloud, name="cloud"),
    path('courses/cyber', courseviews.cyber, name="cyber"),
    path('courses/digital', courseviews.digital, name="digital"),
    path('courses/erp', courseviews.erp, name="erp"),
    path('courses/it', courseviews.it, name="it"),
    path('courses/itcertification', courseviews.itcertification, name="itcertification"),
    path('courses/coursepage/coreui', courseviews.coreui, name="coreui"),
    path('courses/coursepage/advancedui', courseviews.advancedui, name="advancedui"),
    path('courses/coursepage/angularjs', courseviews.angularjs, name="angularjs"),
    path('courses/coursepage/reactjs', courseviews.reactjs, name="reactjs"),
    path('courses/coursepage/vuejs', courseviews.vuejs, name="vuejs"),
    path('courses/coursepage/java', courseviews.java, name="java"),
    path('courses/coursepage/dotnet', courseviews.dotnet, name="dotnet"),
    path('courses/coursepage/nodejs', courseviews.nodejs, name="nodejs"),
    path('courses/coursepage/advancejava', courseviews.advancejava, name="advancejava"),path('courses/coursepage/dotnetcore', courseviews.dotnetcore, name="dotnetcore"),     
    path('courses/coursepage/adwordexpert', courseviews.adwordexpert, name="adwordexpert"),path('courses/coursepage/adwordsfoundation', courseviews.adwordsfoundation, name="adwordsfoundation"),path('courses/coursepage/agile', courseviews.agile, name="agile"),path('courses/coursepage/aimlexpertcourse', courseviews.aimlexpertcourse, name="aimlexpertcourse"),path('courses/coursepage/aimlfoundationcourse', courseviews.aimlfoundationcourse, name="aimlfoundationcourse"),
    path('courses/coursepage/android', courseviews.android, name="android"),
    path('courses/coursepage/ansible', courseviews.ansible, name="ansible"),
    path('courses/coursepage/automation', courseviews.automation, name="automation"),
    path('courses/coursepage/awscloudpractitioner', courseviews.awscloudpractitioner, name="awscloudpractitioner"),
    path('courses/coursepage/awsdeveloperassociate', courseviews.awsdeveloperassociate, name="awsdeveloperassociate"),
    path('courses/coursepage/awssolutionarchitectassociate', courseviews.awssolutionarchitectassociate, name="awssolutionarchitectassociate"),
    path('courses/coursepage/awssysopsassociateadministrator', courseviews.awssysopsassociateadministrator, name="awssysopsassociateadministrator"),
    path('courses/coursepage/awstechnicalessentials', courseviews.awstechnicalessentials, name="awstechnicalessentials"),
    path('courses/coursepage/branding', courseviews.branding, name="branding"),
    path('courses/coursepage/ccsp', courseviews.ccsp, name="ccsp"),
    path('courses/coursepage/ceh', courseviews.ceh, name="ceh"),
    path('courses/coursepage/chef', courseviews.chef, name="chef"),
    path('courses/coursepage/cisa', courseviews.cisa, name="cisa"),
    path('courses/coursepage/cism', courseviews.cism, name="cissp"),
    path('courses/coursepage/cloudtesting', courseviews.cloudtesting, name="cloudtesting"),
    path('courses/coursepage/comptiasecurity', courseviews.comptiasecurity , name="comptiasecurity"),
    path('courses/coursepage/contentmarketing', courseviews.contentmarketing, name="contentmarketing"),
    path('courses/coursepage/corejava', courseviews.corejava, name="corejava"),
    path('courses/coursepage/dataanalytics', courseviews.dataanalytics, name="dataanalytics"),
    path('courses/coursepage/datascientistcertification', courseviews.datascientistcertification, name="datascientistcertification"),
    path('courses/coursepage/deeplearning', courseviews.deeplearning, name="deeplearning"),  
    path('courses/coursepage/devopsexpert', courseviews.devopsexpert, name="devopsexpert"),  
    path('courses/coursepage/devopsfoundation', courseviews.devopsfoundation, name="devopsfoundation"),  
    path('courses/coursepage/digitalmarketingexpert', courseviews.digitalmarketingexpert, name="digitalmarketingexpert"),  
    path('courses/coursepage/digitalmarketingfoundation', courseviews.digitalmarketingfoundation, name="digitalmarketingfoundation"),  
    path('courses/coursepage/docker', courseviews.docker, name="docker"),  
    path('courses/coursepage/dsbootcamp', courseviews.dsbootcamp, name="dsbootcamp"),  
    path('courses/coursepage/flutter', courseviews.flutter, name="flutter"),  
    path('courses/coursepage/fullstacknet', courseviews.fullstacknet, name="fullstacknet"),    
    path('courses/coursepage/fullstacktesting', courseviews.fullstacktesting, name="fullstacktesting"),     
    path('courses/coursepage/golang', courseviews.golang, name="golang"),     
    path('courses/coursepage/hadoop', courseviews.hadoop, name="hadoop"),     
    path('courses/coursepage/inforln', courseviews.inforln, name="inforln"),    
    path('courses/coursepage/ionic', courseviews.ionic, name="ionic"),    
    path('courses/coursepage/ios', courseviews.ios, name="ios"),    
    path('courses/coursepage/itilfoundation', courseviews.itilfoundation, name="itilfoundation"),     
    path('courses/coursepage/kubernets', courseviews.kubernets, name="kubernets"),   
    path('courses/coursepage/manualtesting', courseviews.manualtesting, name="manualtesting"),   
    path('courses/coursepage/mean', courseviews.mean, name="mean"),   
    path('courses/coursepage/measn', courseviews.measn, name="measn"),   
    path('courses/coursepage/mevn', courseviews.mevn, name="mevn"),          
    path('courses/coursepage/microsoftazureexpertcertification', courseviews.microsoftazureexpertcertification, name="microsoftazureexpertcertification"),    
    path('courses/coursepage/microsoftazurefundamentals', courseviews.microsoftazurefundamentals, name="microsoftazurefundamentals"),    
    path('courses/coursepage/microsoftdynamics', courseviews.microsoftdynamics, name="microsoftdynamics"), 
    path('courses/coursepage/mlwithpython', courseviews.mlwithpython, name="mlwithpython"), 
    path('courses/coursepage/naturallanguageprocessing', courseviews.naturallanguageprocessing, name="naturallanguageprocessing"), 
    path('courses/coursepage/onsenui', courseviews.onsenui, name="onsenui"),           
    path('courses/coursepage/openstack', courseviews.openstack, name="openstack"),        
    path('courses/coursepage/oracle', courseviews.oracle, name="oracle"),        
    path('courses/coursepage/pmiacp', courseviews.pmiacp, name="pmiacp"),        
    path('courses/coursepage/pmp', courseviews.pmp, name="pmp"),           
    path('courses/coursepage/prince2', courseviews.prince2, name="prince2"),    
    path('courses/coursepage/python', courseviews.python, name="python"),           
    path('courses/coursepage/reactnative', courseviews.reactnative, name="reactnative"),   
    path('courses/coursepage/remedy', courseviews.remedy, name="remedy"),   
    path('courses/coursepage/rootstack', courseviews.rootstack, name="rootstack"),         
    path('courses/coursepage/rprogramming', courseviews.rprogramming, name="rprogramming"),        
    path('courses/coursepage/ruby', courseviews.ruby, name="ruby"),        
    path('courses/coursepage/rubyfullstack', courseviews.rubyfullstack, name="rubyfullstack"),        
    path('courses/coursepage/salesforce', courseviews.salesforce, name="salesforce"),        
    path('courses/coursepage/sap', courseviews.sap, name="sap"),          
    path('courses/coursepage/scm', courseviews.scm, name="scm"),   
    path('courses/coursepage/seo', courseviews.seo, name="seo"),      
    path('courses/coursepage/servicenow', courseviews.servicenow, name="servicenow"),       
    path('courses/coursepage/smm', courseviews.smm, name="smm"),           
    path('courses/coursepage/smo', courseviews.smo, name="smo"),       
    path('courses/coursepage/xamarin', courseviews.xamarin, name="xamarin"),   
    path('courses/coursepage/vuejs', courseviews.vuejs, name="vuejs"),                                             
    # Read more
    path('courses/coursedetails', courseviews.coursedetails, name="coursedetails"),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)