# top level listing of what to upload for the application server
APP_SRC = [
    'briefkasten',
    'middleware_scripts',
    'buildout/appserver.cfg',
    'bootstrap.py',
    'templates',
    'setup.cfg',
    'setup.py',
]

# top level listing of what to upload for the application server
CLEANSER_SRC = [
    'middleware_scripts',
]


def deploy_freebsd():
    from deployment import freebsd
    from ezjaildeploy.commandline import main
    main(blueprints=freebsd)
