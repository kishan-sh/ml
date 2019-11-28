import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.layouts import gridplot
from bokeh.io import push_notebook
output_notebook()
import numpy as np
def local_regression(x0, X, Y, tau):
	x0 = np.r_[1, x0] 
	X = np.c_[np.ones(len(X)), X]
	xw = X.T * radial_kernel(x0, X, tau) 
	beta = np.linalg.pinv(xw @ X) @ xw @ Y 
	return x0 @ beta 
def radial_kernel(x0, X, tau):
	return np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau * tau)) 
n = 1000
X = np.linspace(-3, 3, num=n)
print("The Data Set ( 10 Samples) X :\n",X[1:10])
Y = np.log(np.abs(X ** 2 - 1) + .5)
print("The Fitting Curve Data Set (10 Samples) Y :\n",Y[1:10])
X += np.random.normal(scale=.1, size=n)
print("Normalised (10 Samples) X :\n",X[1:10])
domain = np.linspace(-3, 3, num=300)
print(" Xo Domain Space(10 Samples) :\n",domain[1:10])
def plot_lwr(tau):
	prediction = [local_regression(x0, X, Y, tau) for x0 in domain]
	plot = figure(plot_width=400, plot_height=400)
	plot.title.text='tau=%g' % tau
	plot.scatter(X, Y, alpha=.3)
	plot.line(domain, prediction, line_width=2, color='red')
	return plot
show(gridplot([[plot_lwr(10.), plot_lwr(1.)],[plot_lwr(0.1), plot_lwr(0.01)]]))