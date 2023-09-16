https://realpython.com/get-started-with-django-1/
python -m venv venv
This command will create a venv folder in your working directory. Inside this directory, you’ll find several files, including a copy of the Python standard library. Later, when you install new dependencies, they’ll also live in this directory. Next, you need to activate the virtual environment by running the following command:

.\venv\Scripts\activate || venv\script\activate.bat


create a new functional domain :
python manage.py startapp pages
python manage.py startapp projects
python manage.py startapp associations

python manage.py makemigrations projects
python manage.py migrate projects

first_project = ProjectSite(
	title="Donation Management Project",
	description="A web Donation Management project.", 
	technology="Django",)
 first_project.save()

second_project = ProjectSite(
	title="Donation Management Project1",
	description="A web Donation Management project1.", 
	technology="Django",)
second_project .save()

second_project = ProjectSite(
	title="Donation Management Project2",
	description="A web Donation Management project2.", 
	technology="Django",)
second_project .save()

#template to be used for other function domains to create
(venv) $ python manage.py startapp projects : start
...
Leverage the Django Admin Site : end

first_project = Association(
	name="Association Basma",
	motif="A web Donation Management project.", 
	adresse="215, bd tata",)
 first_project.save()

