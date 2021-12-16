
* jupyter-notebook on debian (9, 10, 11)

-> konqueror par défaut = OK

sinon, c'est mort.

update-alternatives --config x-www-browser
-> choisir konqueror
apt install jupyter-notebook

dans la session :
export BROWSER="/usr/bin/konqueror"

~/.jupyter/jupyter_notebook_config.py
c.NotebookApp.browser = '/usr/bin/konqueror --app=%s'
c.NotebookApp.use_redirect_file = False
c.NotebookApp.open_browser = False
c.NotebookApp.allow_origin = 'localhost'
c.NotebookApp.trust_xheaders = False

jupyter-notebook --no-browser
jupyter-notebook --browser=konqueror
