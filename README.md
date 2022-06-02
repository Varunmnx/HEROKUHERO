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

## How do this work

deploys websites using heroku
uses s3 bucket to create vm's
uses pulumi api to interact with heroku and aws
