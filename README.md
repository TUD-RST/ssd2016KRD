This repository contains supporting calculations for the paper: 
# "Holonomic Modeling and Hierarchic Tracking Control of an Unstable Underactuated Nonholonomic System"

which is submitted to the [SSD2016 Conference](http://www.ssd-conf.org/ssd16/index.php?site=cfp&conf=SAC).

The source code mainly consists in an IPython notebook, where documentation, actual source code and its output (including figures) can be combined in one executable document to facilitate comprehensibility.

The recommended way to [view that notebook](http://nbviewer.ipython.org/github/TUD-RST/ssd2016KRD/blob/master/holonomic_modeling_and_hierarchic_tracking_control_of%20an_unstable_underactuated_nonholonomic_system.ipynb) is via the web application [nbviewer](http://nbviewer.ipython.org/).

### Requirements
to run that notebook on your own platform:
 * Python 2.7 (not 3.x)
 * numpy, scipy, sympy, matplotlib
 * [`python-control`](https://github.com/python-control/python-control) (developed by Richard M. Murray ) 
 * Two modules developed by the first author of this paper:
   * [`symb_tools`](https://github.com/cknoll/rst_symbtools) (imported as `st`)
   * [`model_tools`](https://github.com/cknoll/rst_symbtools) (imported as `mt`)
 * (Optionally): Extension [`displaytools`](https://github.com/cknoll/displaytools) to conveniently print intermediate results (triggered by the special comment `##` )