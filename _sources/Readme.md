# CBE 30338 Data Analytics, Optimization, and Control

This is a collection of class materials for CBE 303338 Data Analytics, Optimization, and Control taught at the University of Notre Dame. 

## Course Description

Dynamic modeling, data analytics, optimization, and control are essential to modern chemical technologies that enable precision medicine, sustainable energy, semiconductors, access to clean water, and beyond. In CBE 30338, students combine their knowledge of chemical engineering fundamentals (e.g., thermodynamics, transport, kinetics) and data analytics to develop dynamic models of diverse chemical technologies and processes. These models enable the design and optimization of control systems that use feedback to reject disturbances and drive systems to steady-state setpoints. CBE 30338 combines state-space modeling with modern computational and statistical methods to cover industrially relevant topics such as model predictive control, parameter estimation, and optimization. Students master techniques in hands-on experiments and a final semester project.

## Course Outline

| Weeks | Unit |
| :--: | :-- |
| 1 | Introductions to the Course and TC Lab |
| 1 - 4 | Dynamic Modeling and Data Analytics |
| 5 - 7 | Feedback Control |
| 7 - 9 | Computational Optimization |
| 10 - 11 | Predictive Control |
| 12 - 13 | Team Project Workshops |
| 14 | Student Project Presentations |

## Software Installation Instructions

Students will use their personal laptop computers to complete labratory and homework assignments. Below are instructions 

Start Here:
* Install anaconda: https://www.anaconda.com/
* Windows users: in the Start menu, search search for "Anaconda prompt". Open it and copy-paste-run the commands below
* Mac users: press command + space, then search for "terminal". Open it and copy-paste-run the commands below
* Create new conda environment: `conda create -n controls python=3.10`
* Activate new environemnt: `conda activate controls`

Extra Steps for Website Contributors (e.g., instructor, TAs, students please skip):
* Install Jupyter Book (may take a while, solve may freeze a few times): `conda install -c conda-forge jupyter-book`
* Install GHP Import (for publishing with GitHub pages): `conda install -c conda-forge ghp-import`

Everyone (students resume here after "Start Here" steps are complete):
* Install Jupyter Lab: `conda install -c conda-forge jupyterlab`
* Needed to switch kernels in Jupyter Lab: `conda install nb_conda_kernels`
* Install Pandas, Numpy, and Matplotlib: `conda install -c anaconda pandas numpy matplotlib scipy`
* Install IDAES-PSE (which includes pyomo): `conda install -c IDAES-PSE -c conda-forge idaes-pse`
* Install optimization solvers: `idaes get-extensions`
* Install tclab: `pip install tclab`

To run Python, in either the Acaconda prompty (Windows) or terminal (Mac):
* Activate our environment: `conda activate controls`
* Launch Jupyter lab: `jupyter lab`
* In the upper right corner, click on "Kernel" and change to "controls"
* You are now ready to test the TCLab hardware!

## Contact Us

Most of these materials were developed by [Prof. Jeffery Kantor](https://news.nd.edu/news/in-memoriam-jeffrey-kantor-former-vice-president-associate-provost-and-dean/). The repository is currently maintained by [Prof. Alexander Dowling](https://dowlinglab.nd.edu/) at [https://github.com/ndcbe/controls](https://github.com/ndcbe/controls).
