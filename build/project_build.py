'''

This is my homemade build function. It creates a build directory that holds all the static site files.
This directory is then copied to the s3 bucket where all static files are servered from.
All files are copied from the app directory to a temporary dist directory.
All .js files are uglified/moved to one file. Then the new .js file is added to index.html.
And all references to the project .js files are removed.


dist
    index.html <- uglify all .js files, remove all comments.
    app.js <- change all .html file references to /[filename.view.html], remove all comments.

    online-resume.js <- formatVisitor.filter.js, onlineResumeData.service.js, home.controller.js

    home.view.html <- was home/home.view.html
    angular-route.min.js <- was static/angular/angular-route.min.js
    angular-sanitize.min.js <- was static/angular/angular-sanitize.min.js
    angular.min.js <- was static/angular/angular.min.js
    styles.css <- was static/stylesheets/styles.css

copy all these files to the s3 bucket

delete the dist folder

run the integration tests against the new deployment <- done outside of this method.


'''

import os
import shutil
import re

from jsmin import jsmin

class BuildProject(object):

    def __init__(self):
        self.dist_path = os.path.join(os.getcwd(), "build", "dist")
        self.static_files = [
            "home.view.html",
            "angular.min.js",
            "angular-route.min.js",
            "angular-sanitize.min.js",
            "styles.css"
        ]

        self.js_files = [
            "home.controller.js",
            "formatVisitor.filter.js",
            "onlineResumeData.service.js",
        ]


    def build_project(self):
        # build the dist folder:
        self.create_dir(path=self.dist_path)

        # copy all the static files:
        self.copy_static_files(
            source=os.path.join(os.getcwd(), "app"),
            dest=self.dist_path
        )

        self.build_index_html(
            dest=self.dist_path
        )

        self.copy_app_js(
            source=os.path.join(os.getcwd(), "app"),
            dest=self.dist_path
        )

        self.minify_js_files(
            source=os.path.join(os.getcwd(), "app"),
            dest=self.dist_path
        )

        self.copy_to_s3()

        self.remove_dir(path=self.dist_path)


    # copy the dist folder contents to the s3 bucket:
    def create_dir(self, path):
        # remove the directory if it exists and then create a new empty directory:
        if os.path.exists(path):
            self.remove_dir(path=path)

        os.makedirs(path)



    def remove_dir(self, path):
        shutil.rmtree(path)


    def copy_static_files(self, source, dest):
        for path, dirs, files in os.walk(source):
            for this_file in files:
                if this_file in self.static_files:
                    source_path = os.path.join(path, this_file)
                    dest_path = os.path.join(dest, this_file)
                    shutil.copy(source_path, dest_path)
                    # print(f"copying {source_path} to {dist_path}")



    def build_index_html(self, dest):
        dest_path = os.path.join(dest, "index.html")

        # Javascript files:
        js_files = [x for x in self.static_files if ".js" in x]
        js_files.append("online-resume.min.js")

        # build the html file with the js links:
        index_html = "<!DOCTYPE html>\n"
        index_html += "<html ng-app='onlineResume'>\n"
        index_html += "<head>\n"
        index_html += "\t<title>Glenn Crosby &vert; Resume</title>\n"
        index_html += '\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n'

        index_html += '\t<link rel="stylesheet" type="text/css" href="/styles.css">\n'
        index_html += '</head>\n<body ng-view>\n'

        for js_file in js_files:
            index_html += f'\t<script type="text/javascript" src="/{js_file}"></script>\n'

        index_html += '</body>\n</html>'

        # write the html str
        with open(dest_path, "w") as f:
            f.write(index_html)


    def copy_app_js(self, source, dest):
        source_path = os.path.join(source, "app.js")
        dest_path = os.path.join(dest, "app.js")

        with open(source_path, "r") as f:
            app_js = f.read()

        # remove all comments:
        app_js = re.sub(r'// .*', '', app_js)

        view_files = [x for x in self.static_files if ".view.html" in x]

        # remove the .view. from all view files.
        # Update the view file and the name in the app file.
        for view_file in view_files:
            view_name = view_file.split(".")[0]
            app_js = re.sub(f"'.*/{view_file}'", f"'{view_name}.html'", app_js)
            shutil.move(
                src=os.path.join(dest, view_file),
                dst=os.path.join(dest, f"{view_name}.html")
            )


        with open(dest_path, "w") as f:
            f.write(app_js)


    def minify_js_files(self, source, dest):

        # Combine all the js files into one file:
        online_resume_min_js = ""

        # add the app.js file:
        with open(os.path.join(dest, "app.js"), "r") as f:
            online_resume_min_js += f.read()

        for path, dirs, files in os.walk(source):
            for this_file in files:
                if this_file in self.js_files:
                    source_path = os.path.join(path, this_file)
                    # dest_path = os.path.join(dest, this_file)
                    # shutil.copy(source_path, dest_path)
                    with open(source_path, "r") as f:
                        online_resume_min_js += f.read()
                        online_resume_min_js += "\n"


        # minify the js file:
        online_resume_min_js = jsmin(online_resume_min_js)


        with open(os.path.join(dest, "online-resume.min.js"), "w") as f:
            f.write(online_resume_min_js)


        # remove the app file in the dest folder:
        os.remove(path=os.path.join(dest, "app.js"))


    def copy_to_s3(self):
        pass


if __name__ == "__main__":
    BuildProject().build_project()

