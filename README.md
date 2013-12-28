djbootstrap
===========
Django Bootstrap: my general template for new Django projects

Django version: 1.6

Creating a new clone
--------------------
1. Clone the project with a new name:

        git clone . /path/to/new
        cd /path/to/new

2. Rename `myproj` to your `newproj` everywhere:

        mv myproj newproj
        grep -rl myproj . | grep -v ^./.git/ | xargs sed -i s/myproj/newproj/g

3. Rename `myapp` to your `newapp` everywhere:

        mv myapp newapp
        grep -rl myapp newapp | xargs sed -i s/myapp/newapp/g

4. Restart repo:

        rm -fr .git
        git init
        git remote rm origin
        git remote add origin newurl

Updating a clone
----------------
TODO