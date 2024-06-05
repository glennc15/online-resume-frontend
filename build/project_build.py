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
import subprocess
import boto3
import sys

from jsmin import jsmin

class BuildProject(object):

    def __init__(self):
        self.source_path = os.path.join(os.getcwd(), "app")
        self.dist_path = os.path.join(os.getcwd(), "build", "dist")

        self.dist_files = [
            "home.view.html",
            "angular.min.js",
            "angular-route.min.js",
            "angular-sanitize.min.js",
            "styles.css",
            "home.controller.js",
            "home.view.html",
            "formatVisitor.filter.js",
            "onlineResumeData.service.js",
            "app.js",
            "index.html"
        ]

        self.minify = [
            "app.js",
            "home.controller.js",
            "formatVisitor.filter.js",
            "onlineResumeData.service.js",
        ]

    # @property
    # def dist_path(self):
    #     return self.dist_path

    # @dist_path.setter
    # def dist_path(self, value):
    #     self.dist_path = value


    def build_project(self, delete_distribution=True):
        # build the dist folder:
        self.create_dir(
            source=self.source_path,
            dest=self.dist_path,
            files=self.dist_files
        )

        self.minify_js_files(
            source=self.dist_path,
            dest=os.path.join(os.getcwd(), "build", "dist", "static", "angular"),
            js_files=self.minify,
            filename="online-resume.min.js"
        )

        self.update_index_html(
            filepath=os.path.join(self.dist_path, "index.html"),
            js_minified_file="/static/angular/online-resume.min.js",
            comment_files=self.minify
        )

        self.copy_to_s3(
            source=self.dist_path,
        )

        if delete_distribution:
            self.remove_dir(path=self.dist_path)


    def create_dir(self, source, dest, files):
        # remove the directory if it exists and then create a new empty directory:
        if os.path.exists(dest):
            self.remove_dir(path=dest)

        for path, dirs, source_files in os.walk(source):
            if "lib" not in path:
                for this_file in source_files:
                    if this_file in files:

                        partial_path = path[len(source):]
                        dest_path = os.path.join(dest, *partial_path.split("/"))

                        # create the directory structure if it does not exists:
                        if not os.path.exists(dest_path):
                            os.makedirs(dest_path)

                        shutil.copy(
                            src=os.path.join(path, this_file),
                            dst=os.path.join(dest_path, this_file)
                        )


    def remove_dir(self, path):
        shutil.rmtree(path)


    def copy_static_files(self, source, dest, static_files):
        for path, dirs, files in os.walk(source):
            for this_file in files:
                if this_file in static_files:
                    source_path = os.path.join(path, this_file)
                    dest_path = os.path.join(dest, this_file)
                    shutil.copy(source_path, dest_path)



    def build_index_html(self, dest, css_files, js_files):
        dest_path = os.path.join(dest, "index.html")

        # Javascript files:
        js_files.append("online-resume.min.js")
        # js_files.append("app.js")


        # build the html file with the js links:
        index_html = "<!DOCTYPE html>\n"
        index_html += "<html ng-app='onlineResume'>\n"
        index_html += "<head>\n"
        index_html += "\t<title>Glenn Crosby &vert; Resume</title>\n"
        index_html += '\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n'

        for css_file in css_files:
            index_html += f'\t<link rel="stylesheet" type="text/css" href="/static/css/{css_file}">\n'

        index_html += '</head>\n<body ng-view>\n'

        for js_file in js_files:
            index_html += f'\t<script type="text/javascript" src="static/js/{js_file}"></script>\n'

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
            # view_name = view_file.split(".")[0]
            app_js = re.sub(f"'.*/{view_file}'", f"'static/views/{view_file}'", app_js)
            # shutil.move(
                # src=os.path.join(dest, view_file),
                # dst=os.path.join(dest, f"{view_name}.html")
            # )


        with open(dest_path, "w") as f:
            f.write(app_js)


    def minify_js_files(self, source, dest, js_files, filename):

        # find the location of all the files to minify.
        file_paths = list()
        for path, dirs, files, in os.walk(source):
            for this_file in files:
                if this_file in js_files:
                    file_paths.append(os.path.join(path, this_file))

        # app.js has to be the first file in the list
        file_paths = sorted(file_paths, key=lambda x: x.split("\\")[-1])


        # Combine all the js files into one file, and remove the original file:
        js_str = ""
        for this_path in file_paths:
            with open(this_path, "r") as f:
                js_str += f.read()
            js_str += "\n"
            # remove the original file:
            os.remove(this_path)


        # minify the JavaScript and save it:
        minified_js_str = jsmin(js_str)
        with open(os.path.join(dest, filename), "w") as f:
            f.write(minified_js_str)

    def update_index_html(self, filepath, js_minified_file, comment_files):
        """
        updates the Javascript script tags. Add a script tag for the
        minified file and removes the script files to the old JS
        files that were minifled.

        """

        with open(filepath, "r") as f:
            index_html = f.read()


        # replace app.js with the minified file:
        index_html = index_html.replace(
            '<script type="text/javascript" src="/app.js"></script>',
            f'<script type="text/javascript" src="{js_minified_file}"></script>'
        )

        # remove the old JavaScript file script tags:
        for js_file in comment_files:
            index_html = re.sub(
                f'<script type=\"text/javascript\" src=\".*/{js_file}\"></script>',
                '',
                index_html
            )

        # remove the commented script tags:
        index_html = re.sub(
            '<!-- <script .*></script> -->',
            '',
            index_html
        )

        # remove the commented link tags:
        index_html = re.sub(
            '<!-- <link .*> -->',
            '',
            index_html
        )

        index_html = re.sub(
            "<!--.*?-->",
            "",
            index_html,
            flags=re.DOTALL
        )

        with open(filepath, "w") as f:
            f.write(index_html)


    def copy_to_s3(self, source):
        content_types = {
            "html": "text/html",
            "css": "text/css",
            "js": "text/javascript"
        }

        s3_client = boto3.client('s3')

        site_bucket_name = self.get_terraform_outputs().get("site_bucket_name")
        # site_bucket_name = "glenns-test-site"

        # the dist folder only contains files:
        for path, dirs, files in os.walk(source):
            for this_file in files:
                file_extension = this_file.split(".")[-1]

                key_path = path[len(source):]
                this_key = os.path.join(*key_path.split("/"), this_file)

                with open(os.path.join(path, this_file), "rb") as f:
                    try:
                        s3_client.put_object(
                            Body=f,
                            Bucket=site_bucket_name,
                            Key=this_key,
                            ContentType=content_types.get(file_extension)
                        )
                    except Exception as e:
                        raise e


    def get_terraform_outputs(self):
        terraform_outputs = subprocess.run(['cd terraform && terraform output'], stdout=subprocess.PIPE, shell=True)
        terraform_str = terraform_outputs.stdout.decode('utf-8')
        terraform_parts = [x.split(' = ') for x in terraform_str.split('\n')]
        terraform_outputs = dict([(x[0], x[1][1:-1]) for x in terraform_parts if len(x) > 1])

        return terraform_outputs

if __name__ == "__main__":
    '''
    cli:
    -k: keeps the distribution directiory after building it. The normal behaviour
        is to remove the directory after it's contents is moved to AWS.

    -d: deletes the distribution directory if it exists.

    '''
    if len(sys.argv) > 1:
        args = sys.argv[1]

    else:
        args = None

    if args == '-k':
        BuildProject().build_project(delete_distribution=False)

    elif args == '-d':
        build_project_obj = BuildProject()
        build_project_obj.remove_dir(
            path=os.path.join(os.getcwd(), "build", "dist")
        )

    else:
        BuildProject().build_project()

