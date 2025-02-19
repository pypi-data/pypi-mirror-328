=======
History
=======

2.2.5 (2025-02-18)
------------------
* refactor pyproject.toml for using uv
* update code to remove warnings

2.2.4 (2025-02-18)
------------------
* fixes for Cython 3

2.2.3 (2023-05-09)
------------------
* updated code to be compatible with latest numba and clang
* also tested with Python 3.11

2.2.2 (2022-12-19)
------------------
* changed wrapper injection into fast solvers

2.2.1 (2022-12-13)
------------------
* fix broken downward compatibility of version 2.2.0
* improved import speed
* fix numerical rounding issue in fast lsoda
* fix pickling issue

2.2.0 (2022-12-13)
------------------
* fix issue with parallel execution of ode solvers

2.1.1 (2022-11-03)
------------------
* fix reporting of stepsizes chosen by ode solver

2.1.0 (2022-11-02)
------------------
* extra parameter h0 for initial step size ode solver

2.0.0 (2022-10-28)
------------------
* numba support for wrapper methods

1.1.1 (2022-10-25)
------------------
* fix memory leak in ode combined


1.1.0 (2022-10-18)
------------------
* inject wrapper into fast solvers and related functions such as merge
* fixed all warnings

1.0.8 (2022-08-01)
------------------

* fix race conditions when writing new traces files
* fix counting fast lru solver calls
* reduce number of 'new permutations' messages
* fix issue with reordering in exported XXX_dot functions

1.0.7 (2022-07-08)
-------------------
* fix issue with reordering in exported XXX_dot functions
* print sparsity of jacobian

1.0.6 (2022-06-08)
-------------------
* fix: consider interpolation data when pickling

1.0.5 (2022-05-09)
-------------------
* fix utils.get_platform
* fix race condition when deleting new traces files

1.0.4 (2022-04-04)
-------------------
* fix issue with detection arm vs x86 on linux

1.0.3 (2022-04-01)
-------------------
* fix issue with detection arm vs x86 on linux

1.0.2 (2022-04-01)
-------------------
* fix detection arm vs x86 on mac

1.0.1 (2022-03-23)
-------------------
* fix meta data on pypi

1.0.0 (2022-03-23)
-------------------
* release

0.22.3 (2021-12-13)
-------------------
* less output for new traces

0.22.3 (2021-12-13)
-------------------
* less output for new traces

0.22.2 (2021-12-10)
-------------------
* fix missing files in package
* user portalocker to avoid race conditions when reading/writing trace files

0.22.1 (2021-12-10)
-------------------
* fixed licenses

0.22.0 (2021-12-09)
-------------------
* rename to sympy2c, upload to pypi.org, update package meta data

0.21.5 (2021-11-18)
-------------------
* finaly fixed issue when switching time for combined odes is outside given time span.

0.21.4 (2021-11-15)
-------------------
* delete new_traces entries after recompile.

0.21.3 (2021-11-15)
-------------------
* fix issue when switching time for combined odes is outside given time span.

0.21.2 (2021-10-28)
-------------------
* better error message when reading json file fails.

0.21.1 (2021-10-27)
-------------------
* fix compilation flags for ubuntu 20.04.
* fix issue with file encodings of traces files.

0.21.0 (2021-09-24)
-------------------
* faster sparse lu fallback solver.
* cache fast lsoda variant static library.
* check if splits for fast ode solvers are out of range.

0.20.1 (2021-09-14)
-------------------
* Fix required cython version.

0.20.0 (2021-09-09)
-------------------
* report lu solver call counts.
* fix issue with split and traces handling.
* improve compilation time using -f-no-var-tracking compiler flag.
* consider compiler flags in cache folder name.

0.19.1 (2021-07-09)
-------------------
* remove C++17 dependency.

0.19.0 (2021-07-09)
-------------------
* fix compilation issue with anaconda on mac.
* fast ode solver reports more detailed execution time info.
* cache folder names contains sympy and numpy version info.
* fix issue with interpolation functions.

0.18.0 (2021-04-29)
-------------------
* official support for _ufunc versions of compiled functions.
* PythonFunction to compile pure Python function into wrapper.

0.17.0 (2021-04-23)
-------------------
* more arguments for merge function in combined odes.

0.16.3 (2021-03-31)
-------------------
* traces handling for OdeCombined.

0.16.2 (2021-03-31)
-------------------
* fix issue with caching OdeCombined intermediate data.
* fix issue when switching odes.

0.16.1 (2021-03-25)
-------------------
* fix issue when merging solutions of combined odes.

0.16.0 (2021-03-18)
-------------------
* new feature: combined odes.

0.15.3 (2021-03-03)
-------------------
* fix: more reliable server for gsl download, existing one was broken.

0.15.2 (2021-02-08)
-------------------
* fix: restore Python 3.6 support.


0.15.1 (2021-01-27)
-------------------

* fixed reordering of fast ode equations.

0.15.0 (2021-01-13)
-------------------

* reordering of fast ode equations.

0.14.1 (2020-12-09)
-------------------
* restore Python 3.6 support.

0.14.0 (2020-12-07)
-------------------
* fixed bug in unique id computation in OdeFast.
* own approach for symbolic matrix inversion to gain speed.

0.13.1 (2020-11-23)
-------------------
* fix traces handling.

0.13.0 (2020-11-20)
-------------------
* faster compilation times based on schur-complement approach for solving
  linear systems.
* better handling of traces.

0.12.1 (2020-10-16)
-------------------
* fix encoding issue when using subprocess module from standard library.

0.12.0 (2020-08-27)
-------------------
* unify API of ode and fast ode solver.
* support to specify compilation flags.
* reduced size if sympy_to_c Python package.

0.11.0 (2020-08-19)
-------------------
* reduce memory consumption of fast ode solver.
* support for bessel and 2f1 hyper geometric function.
* speed improvements in ode code related c functions.
* fix issue with handling rtol in fast ode solver.
* fix issue with memory handling / computation.

0.10.0 (2020-06-02)
-------------------
* new parameter max_order for fast ode solver.
* rtol parameter for fast ode solver can be a vector now to use different settings
  for different components of the ode.
* compiled wrapper module name now includes unique id to support loading different
  wrappers in the same python interpreter.


0.9.0 (2020-03-31)
------------------
* Use constant 'extrapolation' on rhs of interpolation intervals. This is
  usefull if the ode solver tries to evaluate the rhs of the ODE beyond the
  last time point.


0.8.11 (2020-03-24)
-------------------
* fixed bug related to included blas from release 0.8.10.


0.8.10 (2020-03-19)
-------------------

* add attribute sympy_to_c_version to compiled module.
* include blas / lapack dependencies.

0.8.9 (2020-03-06)
------------------

* fixed pickling problems (commit 2215dfb).
* compiled module already has "default" integral parameters defined. Wrappers
  now can be used after import without setting integration parameters for
  integrals with id "default" (commit d544632).
* fixed issue with caching expression hashes (commit e73dd5d).
* reduced output (commit 25e4d62).


0.8.8 (2020-02-25)
------------------

* fixed issues with code creation for integrals.

0.8.7 (2020-02-18)
------------------

* don't expose internal integrand functions to Python. Caused some issues in complex situations.
* print debug information about unique_id computations in case envrinment variable PRINTHASHES is set.

0.8.6 (2020-02-11)
------------------

* fixed pickling
* support for expressions including sympy.Abs.

0.8.5 (2020-02-04)
------------------

* fixed issues with sympy 1.4.X.

0.8.4 (2020-01-31)
------------------

* fixed issues with missing files in package.

0.8.3 (2020-01-30)
------------------

* fixed installation issues.
* internal improvements.
* smaller bug fixes.

0.8.2 (2019-12-10)
------------------

* added ``Module.unique_id``.
* ``unique_id`` computations are much faster now.
* decide late what code to generate and compile.
* less but better output during compilation.

0.8.1 (2019-11-21)
------------------

* fixed broken caching of generated or compiled code.
* improved some messages from lsoda_modified when integration fails.

0.8.0 (2019-11-07)
------------------

* permutations -> traces + improved switchin of solvers.
* fixed "set_sec_factor" function. Old version did nothing.
* increased default value for "mxstep" in modified lsoda 500 to 50,000.

0.7.0 (2019-10-25)
------------------

* support integrals and interpolation functions in fast odes.
* disable compilation of fast ode wrappers on demand (needed in PyCosmo for faster startup).
* sec_factor is not hard coded anymore but can be configured.
* wrapper how has function to retrieve symbols used in an ode.

0.6.1 (2019-10-03)
------------------

* fixed broken ode solver in case time variable appears in right hand side of ode.

0.6.0 (2019-10-01)
------------------

* implemented fast ode solver.
* ode returns result now transposed.

0.5.3 (2019-07-03)
------------------

* enforce continous memory layout for vector arguments.

0.5.2 (2019-07-02)
------------------
* improved speed of code generation for larger ode systems as used in PyCosmo.

0.5.1 (2019-06-20)
------------------
* ode solver functions now have doc strings.
* fixed Python package by adding missing file.

0.5.0 (2019-06-14)
------------------

* ode solver now computes and uses jacobian matrix if wanted.
* include ERROR expression.
* handle None in globals as nan.
* added symbolic isnan function.

0.4.2 (2019-04-11)
------------------

* fixed issues after upgrade sympy to version 1.4.
* better error message when interpolation argument is out of range.

0.4.1 (2019-04-10)
------------------

* fixed pickling issues.

0.4.0 (2019-04-10)
------------------

* Fixed issue with aliasing vectors.
* compiled module now also returns list with strings of LHS symbols.

0.3.0 (2019-04-02)
------------------

* improved output when parsing Python code fails.
* add Min and Max expressions.
* better tests.

0.2.0 (2019-03-22)
------------------

* include ODE solver codes.

0.1.0 (2019-03-20)
------------------

* First release on PyPI.
