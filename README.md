# GitHub Repository for Deep Learning Lecture


## README content

<!-- vim-markdown-toc GFM -->

* [Repository content](#repository-content)
* [Requirements](#requirements)
* [Setup](#setup)
  * [Makefile targets](#makefile-targets)
  * [Step-by-step instructions](#step-by-step-instructions)
* [Lecture notebooks](#lecture-notebooks)

<!-- vim-markdown-toc -->


## Repository content

```
.
├── Makefile                  # run `make help` to see make targets
├── README.md                 # this readme file
├── requirements.txt          # virtualenv requirements file
├── configs                   # notebook configs
├── docs                      # sources, e.g., images for notebooks
├── notebook                  # lecture notebooks
└── src                       # custom python module
```


## Requirements

1. Python 3.7
1. `virtualenv`

Please familiarize yourselves with `virtualenv` (or a similar tool such as `conda`). Some background information can be found in the [virtualenv docs](https://virtualenv.pypa.io/en/latest/) or [here](https://stackoverflow.com/questions/34398676/does-conda-replace-the-need-for-virtualenv).

In the lecture, we will use Jupyter notebooks to illustrate implementation-related key points. Please make sure that you can execute the notebooks before joining the class so you can easily follow the coding parts in the lectures.


## Setup

### Makefile targets

The [Makefile](./Makefile) included in this repository is purely for convenience (e.g., setting up the virtual environment, launching a notebook server). It should work on Linux and Mac OS X systems.

```
$ make help
Make targets:
  build          create virtualenv and install packages
  build-lab      `build` + lab extensions
  freeze         persist installed packaged to requirements.txt
  clean          remove *.pyc files and __pycache__ directory
  distclean      remove virtual environment
  run            run jupyter lab
Check the Makefile for more details
```

### Step-by-step instructions

1. Open a terminal and navigate to the path that you want to clone the repository to
1. Clone the repository
    ```
    $ git clone git@github.com:sbstn-gbl/dl-lecture.git
    ```
1. Navigate to repository path, create virtual environment and install required modules with
    ```
    $ cd dl-lecture && make build
    ```
1. Start a notebook server with
    ```
    $ make run
    ```

If `make` does not work on your computer run the steps included in the [Makefile](./Makefile) manually. You only need to do this setup once.


## Lecture notebooks

- [Notebook 1: Gradient Descent](notebooks/1-gradient-descent.ipynb)
- [Notebook 2: Backpropagation](notebooks/2-backpropagation.ipynb)
- [Notebook 3: Spiral ](notebooks/3-spiral.ipynb)
- [Notebook 4: Tensorboard](notebooks/4-tensorboard.ipynb)
- [Notebook 5: Weight initialization](notebooks/5-weight-initialization.ipynb)
