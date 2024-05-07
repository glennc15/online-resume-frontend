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

class BuildProject(object):

    def __init__(self):
        self.dist_path = os.path.join(os.getcwd(), "build", "dist")
        self.static_files = [
            "home.view.html",
            "angular-route.min.js",
            "angular-sanitize.min.js",
            "angular.min.js",
            "styles.css"
        ]


    def build_project(self):
        # build the dist folder:
        self.create_dir(path=self.dist_path)

        # copy all the static files:
        self.copy_static_files(
            source=os.path.join(os.getcwd(), "app"),
            dest=self.dist_path
        )

        self.copy_index_html(
            source=os.path.join(os.getcwd(), "app"),
            dest=self.dist_path
        )

        self.copy_app_js(
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



    def copy_index_html(self, source, dest):
        pass

    def copy_app_js(self, source, dest):
        pass

    def copy_to_s3(self):
        pass


if __name__ == "__main__":
    BuildProject().build_project()

