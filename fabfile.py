from fabric.api import local

def update(m="Auto-update the app"):
    """ save the to github """
    local("git add .")
    local("git commit -a -m '{0}'".format(m))

