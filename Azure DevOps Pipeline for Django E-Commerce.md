Azure DevOps Pipeline for Django E-Commerce

---

1. Pipeline Trigger

trigger:
- main  # Runs the pipeline when code is pushed to 'main' branch

Explanation

The pipeline automatically triggers when changes are pushed to the main branch of the repository.

This means that whenever a developer pushes code to main, the pipeline runs automatically.



---

2. Define the Agent Pool

pool:
  vmImage: 'ubuntu-latest'  # Use Ubuntu for the pipeline agent

Explanation

Agent Pool: Defines where the pipeline runs.

vmImage: 'ubuntu-latest': Uses the latest Ubuntu virtual machine (VM) as the environment for running the pipeline.

Azure DevOps provides different agents (Windows, macOS, Ubuntu). Here, Ubuntu is used.



---

3. Set Up Python Version

- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.x'  # Use the latest Python version

Explanation

UsePythonVersion@0: An Azure DevOps task to set up Python.

versionSpec: '3.x': Uses the latest Python 3 version (e.g., 3.8, 3.9, 3.10).

Why? Django applications require Python, and this ensures the correct version is installed.



---

4. Install Dependencies

- script: |
    python -m venv env  # Create a virtual environment
    source env/bin/activate  # Activate virtual environment
    pip install --upgrade pip
    pip install -r requirements.txt  # Install project dependencies
  displayName: 'Install Dependencies'

Explanation

Runs a shell script (because Ubuntu uses Bash).

python -m venv env: Creates a virtual environment named env.

source env/bin/activate: Activates the virtual environment (for Linux/macOS).

pip install --upgrade pip: Upgrades pip (Python package manager).

pip install -r requirements.txt: Installs project dependencies from requirements.txt file.

Why? This step ensures the Django project has all required packages installed in an isolated environment.



---

5. Prepare Django Application

- script: |
    python manage.py collectstatic --noinput  # Collect static files
    python manage.py makemigrations
    python manage.py migrate  # Apply database migrations
  displayName: 'Prepare Django Application'

Explanation

python manage.py collectstatic --noinput:

Collects all static files (CSS, JS, images) into a central directory (STATIC_ROOT).

--noinput: Prevents interactive prompts.


python manage.py makemigrations:

Generates database migration files based on model changes.


python manage.py migrate:

Applies migrations to the database.


Why? This step prepares the Django application by ensuring that:

Static files are properly set up.

Database schema is updated according to the models.




---

6. Archive the Project as a Build Artifact

- task: ArchiveFiles@2  # Create a zip file of the project
  inputs:
    rootFolderOrFile: '.'  # Include all project files
    archiveType: 'zip'
    archiveFile: '$(Build.ArtifactStagingDirectory)/ecommerce_build.zip'
    replaceExistingArchive: true
  displayName: 'Create Build Artifact'

Explanation

ArchiveFiles@2: Azure DevOps built-in task to create an archive (zip file).

rootFolderOrFile: '.': Archives the entire project directory.

archiveType: 'zip': Specifies that the archive format is .zip.

archiveFile: '$(Build.ArtifactStagingDirectory)/ecommerce_build.zip':

Saves the zip file in Azure DevOps' artifact staging directory.


replaceExistingArchive: true:

Overwrites the existing archive if it exists.


Why? This step packages the application into a single zip file that can be used for deployment.



---

7. Publish the Build Artifact

- task: PublishBuildArtifacts@1  # Store artifact in Azure DevOps
  inputs:
    pathToPublish: '$(Build.ArtifactStagingDirectory)/ecommerce_build.zip'
    artifactName: 'drop'
  displayName: 'Publish Build Artifact'

Explanation

PublishBuildArtifacts@1: Azure DevOps task to upload the artifact.

pathToPublish: '$(Build.ArtifactStagingDirectory)/ecommerce_build.zip':

Specifies the location of the zip file created earlier.


artifactName: 'drop':

The artifact will be named drop in Azure DevOps.


Why? This step makes the artifact available for later stages (e.g., deployment).



---

Summary of the Pipeline Steps


---

This Azure DevOps pipeline automates the build process for a Django e-commerce application by:

1. Triggering when code is pushed to main.


2. Setting up Python for execution.


3. Installing dependencies in a virtual environment.


4. Preparing Django (static files, migrations).


5. Archiving the project.


6. Publishing the artifact for deployment.
