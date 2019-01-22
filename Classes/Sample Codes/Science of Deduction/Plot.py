# Title: Plots for SOD IEEE Day
# Author: K Nitesh Srivats
# Date: 01/06/2018
import numpy as np
from matplotlib import pyplot as plt


def gradient_descent(x, y, alpha, iterations, beta=None):
    m = 2 * len(y)

    if beta is None:
        beta = np.random.random_sample(x.shape[1])
        beta.shape = (x.shape[1], 1)

    for iteration in range(iterations):
        hypothesis = x.dot(beta)
        loss = hypothesis - y
        # gradient = X.T.dot(loss)/m
        beta = beta - alpha * (x.T.dot(loss) / m)
        # cost_history[iteration] = np.sum((X.dot(beta)-y)**2)/m

    return beta


def get_graph(name, part_one, part_two=None, part_three=None):
    y = np.array(part_one, dtype="int8")
    len_one = y.shape[0]
    y.shape = (len_one, 1)
    x = np.array((np.ones(len_one), 
                 [(x + 1) for x in range(len_one)], 
                 [(x + 1) ** 2 for x in range(len_one)])).T

    try:
        coeff_one = np.load(name + ".npy")[:, 0]
        coeff_one.shape = (coeff_one.shape[0], 1)
        coeff_one = gradient_descent(x, y, 1e-3, int(1e+5), coeff_one)
    except FileNotFoundError:
        coeff_one = gradient_descent(x, y, 1e-3, int(1e+5))

    coeff = coeff_one

    if part_two is not None:
        y = np.array(part_two, dtype="int8")
        len_two = y.shape[0]
        y.shape = (len_two, 1)
        x = np.array((np.ones(len_two), 
                     [(x + 1 + len_one) for x in range(len_two)],
                     [(x + 1 + len_one) ** 2 for x in range(len_two)])).T

        try:
            coeff_two = np.load(name + ".npy")[:, 1]
            coeff_two.shape = (coeff_two.shape[0], 1)
            coeff_two = gradient_descent(x, y, 5e-4, int(1e+5), coeff_two)
        except FileNotFoundError:
            coeff_two = gradient_descent(x, y, 5e-4, int(1e+5))
        coeff = np.append(coeff, coeff_two, axis=1)
    
    if part_three is not None:
        y = np.array(part_three, dtype="int8")
        len_three = y.shape[0]
        y.shape = (len_three, 1)
        len_two += len_one
        x = np.array((np.ones(len_three),
                      [(x + 1 + len_two) for x in range(len_three)],
                      [(x + 1 + len_two) ** 2 for x in range(len_three)])).T
        try:
            coeff_three = np.load(name + ".npy")[:, 2]
            coeff_three.shape = (coeff_three.shape[0], 1)
            coeff_three = gradient_descent(x, y, 1e-4, int(1e+5), coeff_three)
        except FileNotFoundError:
            coeff_three = gradient_descent(x, y, 1e-4, int(1e+5))
   
        coeff = np.append(coeff, coeff_three, axis=1)

    np.save(name, coeff)


def draw_plots(names):
    get_graph(names[0], [9, 9, 8, 6, 4], [4.1, 4.3, 4.7, 5, 5.2])
    get_graph(names[1], [10, 9.5, 8.6, 6.7, 5], [4.6, 4.2, 3.9, 3.7, 3.5])
    get_graph(names[2], [12, 11.7, 10.8, 8.4, 6], [7, 7.2, 8, 8.8, 10])
    get_graph(names[3], [15.7, 14.3, 13.8, 11.5, 8], [11, 13, 17, 20.5, 24])
    get_graph(names[4], [24, 22, 20, 18, 13], [16.3, 18, 21], [15, 8])
    draw_plot([5, 10], names[0], 'k')
    draw_plot([5, 10], names[1], 'r')
    draw_plot([5, 10], names[2], 'orange')
    draw_plot([5, 10], names[3], 'g')
    draw_plot([5, 8, 10], names[4], 'magenta')
    plt.legend()
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
               ["Jan", "Feb", "Mar", "Apr", "May", "June",
                "July", "Aug", "Sept", "Oct", "Nov"])
    plt.xlabel("Months")
    plt.ylabel("Stock Prices")
    plt.title("Shares")
    plt.show()


def draw_plot(delimiters, name, color='b'):
    coeff_array = np.load(name + ".npy")
    steps = int(300 / delimiters[-1])
    delimiters = [0] + delimiters
    
    for i in range(1, len(delimiters)):
        coeff = coeff_array[:, i - 1]
        jumps = (delimiters[i] - delimiters[i - 1]) * steps
        x = np.array((np.ones(jumps),
                      np.linspace(delimiters[i - 1], delimiters[i],
                                  jumps, dtype="f2"),
                      np.linspace(delimiters[i - 1] ** 2, delimiters[i] ** 2,
                                  jumps, dtype="f2"))).T
        y = x.dot(coeff)
        if i == 1:
            X = x[:, 1]
            Y = y
        else:
            X = np.concatenate((X, x[:, 1]))
            Y = np.concatenate((Y, y))

    for i in range(len(Y)):
        if float(np.random.random_sample(1)) > 0.5:
            Y[i] += float(np.random.random_sample(1) / 5)
        else:
            Y[i] -= float(np.random.random_sample(1) / 5)

    plt.plot(X, Y, color, label=name)


if __name__ == '__main__':
    draw_plots(["Aviva", "Atlas Homes", "City Grave", "British Land", "Savills"])
