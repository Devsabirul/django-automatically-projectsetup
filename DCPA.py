import sys
import os
import fileEdit
import webbrowser


def DCPA():
    project_name = sys.argv[1]
    project_folder_path = input(
        "Enter a path where you want to create a project: ")
    os.chdir(project_folder_path)
    if os.path.exists(project_name):
        print("Folder Already Exists")
    else:
        os.mkdir(project_name)
        os.chdir(project_folder_path+"/"+project_name)
        os.system("virtualenv env")
        os.chdir(project_folder_path+"/"+project_name+"/env/Scripts")
        os.system("activate")
        print("Enverment Activated successfully")
        os.system("pip install --default-timeout=100 Django")
        os.chdir(project_folder_path+"/"+project_name)
        os.system("django-admin startproject "+project_name+" ./")
        os.chdir(project_folder_path+"/"+project_name)
        os.system("python manage.py startapp core")
        # add Install App and Insert DIRS file Add Static url root media file in settings.py
        fileEdit.checkSettingsFile(project_folder_path+"/"+project_name +
                                   "/"+project_name+"/settings.py")

        os.chdir(project_folder_path+"/"+project_name)
        os.mkdir('templates')
        os.mkdir('static')
        # Open file and insert 'import os' in line number 14
        fileEdit.add_text(project_folder_path+"/"+project_name +
                          "/"+project_name+"/settings.py", 'import os', 13)

        # create urls.py in app folder
        open(project_folder_path+"/"+project_name+"/core/urls.py", 'w')
        # setup app urls.py file
        url = '''from django.urls import path\nfrom .views import *\nurlpatterns = [\n   path('', home, name="Home"),\n]
        '''
        fileEdit.add_text(project_folder_path+"/" +
                          project_name+"/core/urls.py", url, 0)

        # add views function for home view
        viewFunction = '''from django.http import HttpResponse\n\ndef home(request):\n  return HttpResponse("<div style='text-align: center;margin-top: 50px;'><h1>The install worked successfully! Congratulations! </h1></div>")
        '''
        fileEdit.add_text(project_folder_path+"/" +
                          project_name+"/core/views.py", viewFunction, 1)

        # Add Url Static url
        fileEdit.add_text(
            project_folder_path+"/"+project_name +
            "/"+project_name+"/urls.py", 'from django.conf import settings\nfrom django.conf.urls.static import static\n', 17)

        fileEdit.replace(project_folder_path+"/"+project_name +
                         "/"+project_name+"/urls.py",
                         ']', '] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)')

        # add include function and configer core app urls
        fileEdit.replace(project_folder_path+"/"+project_name +
                         "/"+project_name+"/urls.py",
                         'from django.urls import path', 'from django.urls import path,include')

        fileEdit.checkSettingsFile(project_folder_path+"/"+project_name +
                                   "/"+project_name+"/urls.py")

        os.chdir(project_folder_path+"/"+project_name)
        os.system("python manage.py migrate")
        webbrowser.open('http://127.0.0.1:8000/')
        os.system("python manage.py runserver")
