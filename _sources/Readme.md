# CBE 30338 Data Analytics, Optimization, and Control

This is a collection of class materials for CBE 303338 Data Analytics, Optimization, and Control taught at the University of Notre Dame. 

## Course Description

Dynamic modeling, data analytics, optimization, and control are essential to modern chemical technologies that enable precision medicine, sustainable energy, semiconductors, access to clean water, and beyond. In CBE 30338, students combine their knowledge of chemical engineering fundamentals (e.g., thermodynamics, transport, kinetics) and data analytics to develop dynamic models of diverse chemical technologies and processes. These models enable the design and optimization of control systems that use feedback to reject disturbances and drive systems to steady-state setpoints. CBE 30338 combines state-space modeling with modern computational and statistical methods to cover industrially relevant topics such as model predictive control, parameter estimation, and optimization. Students master techniques in hands-on experiments and a final semester project.

## Course Outline

| Weeks | Unit |
| :--: | :-- |
| 1 | Introductions to the Course and TC Lab |
| 1 - 4 | Modeling |
| 5 - 6 | Feedback Control |
| 7 - 8 | Process Analytics |
| 9 - 10 | Optimization |
| 11 - 12 | Predictive Control |
| 13 | Discrete Event Systems |
| 14 | Student Project Presentations |

## Installing Conda

Start Here:
* Install anaconda: https://www.anaconda.com/
* Create new conda environment: `conda create -n controls python=3.10`
* Activate new environemnt: `conda activate controls`

Extra Steps for Website Contributors (e.g., instructor, TAs):
* Install Jupyter Book (may take a while, solve may freeze a few times): `conda install -c conda-forge jupyter-book`
* Install GHP Import (for publishing with GitHub pages): `conda install -c conda-forge ghp-import`

Students:
* Install Jupyter Lab: `conda install -c conda-forge jupyterlab`
* Install Pandas, Numpy, and Matplotlib: `conda install -c anaconda pandas numpy matplotlib scipy`
* Install IDAES-PSE (which includes pyomo): `conda install -c IDAES-PSE -c conda-forge idaes-pse`
* Install tclab: `pip install tclab`



## Contact Us

Most of these materials were developed by [Prof. Jeffery Kantor](https://news.nd.edu/news/in-memoriam-jeffrey-kantor-former-vice-president-associate-provost-and-dean/). The repository is currently maintained by [Prof. Alexander Dowling](https://dowlinglab.nd.edu/) at [https://github.com/ndcbe/controls](https://github.com/ndcbe/controls).
