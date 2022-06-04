# Herokuhero


## requrements
- should have a aws account
- should have a pulumi account
- should have chocolate packagemanager installed 
- run`@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`
- above code is used to install chocolate
- should have pulumi CLI installed using `choco install pulumi`
- install aws CLI
- configure aws using `configure aws` command
- create new pulumi project using `pulumi new`
- install flask using `pip install flask requests` 
- set up a ssh key using `ssh-keygen -m PEM`
-  `cd Users/(yourusername)/.ssh`
- if id_rsa donot have .pem extension rename it
- cd to your project folder


## How do this work

deploys websites using aws and
uses aws infastructure  to create vm's
uses pulumi api to interact with heroku and aws
