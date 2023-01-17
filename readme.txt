other 
running project python manage.py runserver

steps
1.creating new project.
  run 
    django-admin startproject prjecom
2.create new app.
  run 
    python manage.py startapp core
3.install apps in settings.py
  navigate to the prjecom
		    settings.py
4.configure templates
  a)create templates file in the base directory
  b)in the settings.py navigate t the templates section navigate to the templates section and in the      'Dirs'    tab add os.path.join(BASE_DIR,'templates') 
        #base_dir is the base directory where the manage.py file is located
         'DIRS': [os.path.join(BASE_DIR,'templates')],

5.configure static and media files 
  in the settings.py add below the static_url:-
  # where files used to create your site
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')

  #collecting all the static files where you want to deploy app
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]

  #url we wanet the files to go through
  MEDIA_URL='media/'

  #the images uploaded relating to product that are used in your files/projects
  MEDIA_ROOT=os.path.join(BASE_DIR,'media')

6.create a new view,urls and template then run server
  under the core.view.py file add function
    def index(request):
      return render(request,'core/index.html')

  under the templates folder
     add a core file
       in the core file add a html file i.e. index.html
7.create a new file in the core file 
  main.py
8.where you want to create a custom path
  pass vthe name of the index in the 
