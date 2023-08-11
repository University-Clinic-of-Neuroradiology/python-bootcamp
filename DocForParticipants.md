# Instructions for participants

This instruction contain documentation and links to get started with the Python Bootcamp.

- [Start Here](#start-here)

- [Start a jupyter notebook server](#Start-a-jupyter-notebook-server)

- [Starting a terminal via Jupyter](#starting-a-terminal-via-jupyter)

- [Getting the Data](#getting-the-data)

- [Get started with the course!](#get-started-with-the-course)

- [Appendix of useful info](#appendix)

Documentation is in the form of MarkDown files (`*.md`), which are simple text files which you open from the Jupyter notebook, but they look nicer when browsing to GitLab.


## Start Here

We are using Python for the exercises. Python is an open-source interactive language. We provide Python scripts for the exercises, so you should be fine.
Nevertheless, it would be best to read also the Python tutorial first, see the [Appendices](#appendices).

We use [Jupyter notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html).
If you have never used Jupyter notebooks, you should [read the official documentation](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html).
A useful introduction to the notebook interface [can be found here](http://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html).

***Warning:** these instructions are when using JupyterLab as opposed to the "classic" notebook interface. If you choose to use the classic interface, you will have to modify the notebooks marginally by replacing `%matplotlib widget` with `%matplotlib notebook`. See also the [iPython section](#ipython) below.


## Start a jupyter notebook server

bla bla


## Starting a terminal via Jupyter

It is often useful to run commands in a shell where the Python kernels run.
- Jupyter "classic": on the "Home" tab, click on `New` on the right, and choose `Terminal`
- JupyterLab: go to the Launcher (click on the `+` sign top-left), and choose `Terminal`.


## Getting the Data

Some exercises use data that you will need.

## Get started with the course

All notebooks are located in several subdirectories of [`notebooks`](./notebooks) . Each have a `README.md` file that you should read beforehand, as some notebooks have special requirements (e.g., the order that they're run in). Note that you can open a `README.md` from the Jupyter notebook, but they look nicer when browsing to GitLab.

- [Introductory](./notebooks/Introductory/) notebooks are designed to familiarise you with Python, Jupyter, SIRF, and patterns seen in the other notebooks.
- ...

Start with the [introductory notebooks](notebooks/Introductory/) and the associated [README.md](notebooks/Introductory/README.md).

---------------------------

# Appendix

- [Python Basics](#python)
- [Jupyter notebook manipulations](#jupyter-notebook-manipulations)
- [File extensions](#file-extensions)


## Python Basics

Here is some suggested material on Python (ordered from easy to quite time-consuming).

-   The official Python tutorial. Just read Section 1, 3, a bit of 4 and a tiny bit of 6.
    <https://docs.python.org/2/tutorial/>

-   Examples for matplotlib, the python module that allows you to make plots almost like in MATLAB
    <https://github.com/patvarilly/dihub-python-for-data-scientists-2015/blob/master/notebooks/02_Matplotlib.ipynb>

-   You could read bits and pieces of Python the Hard Way
    <http://learnpythonthehardway.org/book/index.html>

-   Google has an online class on Python for those who know some programming.
    This goes quite in depth and covers 2 days.
    <https://developers.google.com/edu/python/?csw=1>


## Jupyter notebook manipulations

The initial web-page that you will see looks like a file browser (the *Jupyter Notebook dashboard*).
Click on `notebooks`, and drill down until you find a file with the extension `.ipynb` that looks of interest, and click on that.
This should open a new tab in your web browser (or JupyterLab window) with the notebook open, all ready to run.

You will normally work by executing each *cell* bit by bit, and then editing it to do some more work. Useful shortcuts:

-   `LEFT-CTRL + <RETURN>` executes the current cell.
-   `SHIFT + <RETURN>` executes the current cell and advances the cursor to the next cell.
-   `TAB` tries to complete the word/command you have just typed.
-   `Enter` edits "edit" mode to change a cell, `Esc` exits "edit" mode to "command" mode.
-    In "command" mode, press `A` to create a new cell Above, or `B` below your current cell. You can also use `C`, `X`, `V`.
-    Other keyboard shortcuts:
     - When using Jupyter "classic" mode, pressing `H` in "command" mode gives you a useful list of shortcuts.
     - When using JupyterLab, you need to go to the Advanced Settings Editor item in the Settings menu, then select Keyboard Shortcuts in the Settings tab. You probably want to check the `notebook` category. See the [JupyterLab doc](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#keyboard-shortcuts)/

Every open notebook has its own kernel. Closing a notebook tab does **not** stop its kernel.
Use the `File` menu ("classic": `Close and halt`, JupyterLab: `Close and shutdown notebook`).

***Warning:*** Clicking `Logout` will mean all sessions are closed and you will have to start again.


## File extensions

- `.dcm`: DICOM file
- `.nii` or `.nii.gz`: image files in Nifti format.
- `.py`: Python file
- `.ipynb`: jupyter notebook
- `.md`: text file with documentation (in Markdown format)
