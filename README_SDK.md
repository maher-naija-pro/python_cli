#######################################################################
neuro-deploy 0.0.3

Released: 21-03-2023


neuro-deploy, the next version of neuro-deploy, is now stable and recommended for general use.it is easy to start using neuro deploy in your existing projects as well as new projects. Going forward, API updates and all new feature work.


Introduction
neuro-deploy  is a Python package that provides interfaces to deply ML models. Currently, all features work with Python 3.


Services
At the moment, neuro-deploy supports:

User management
Tokens management
Models


Installation
Install via pip:

$ pip install neuro-deploy
Install from source:

ChangeLogs
To see what has changed over time in neuro-deploy, you can check out the release notes in our website
Finding Out More About Boto

Online documentation is also available. The online documentation includes full API documentation as well as Getting Started Guides for many of the neuro-deploy modules.



Getting Started with neuro-deploy

Your credentials can be passed into the methods that create connections. Alternatively, neuro-deploy will check for the existence of the following environment variables to ascertain your credentials:

ND_ACCESS_TOKEN - Your Neuro deploy Access Key ID

ND_SECRETKEY - Your  Neuro deploy  Secret Access Key

Credentials and other settings can also be stored in a Neuro deploy config files:

~/.nd/secrets  #where your access credentials are stored
~/.nd/config   #where your configuration is stroes : user name / URL
~/.nd/token    #where your jwt token is tored after login




