from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

class PyPlotWrapper:
    """
    A class that represents a line chart.

    Attributes:
        x_values (list): A list of x values.
        y_values (list): A list of y values.

    Methods:
        plot(): Plots a line chart.
        scatter(): Plots a scatter plot.
        bar(): Plots a bar chart.
        pie(): Plots a pie chart.
        histogram(): Plots a histogram.
        boxplot(): Plots a boxplot.
        subplot(): Creates multiple subplots in a single figure.
        save_figure(): Saves the current figure to a file.
        set_style(): Sets the style of the plot.
    """

    def __init__(self, x_values, y_values):
        self.x_values = x_values
        self.y_values = y_values

    def plot(self, save_as_png=False):
        plt.plot(self.x_values, self.y_values)
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        if save_as_png:
            plt.savefig('plot.png', format='png')
        plt.show()

    def scatter(self, save_as_png=False):
        plt.scatter(self.x_values, self.y_values)
        plt.xlabel('X Values')
        plt.ylabel('Y Values')      
        # Add the next 3 x and y values to the scatter
        next_x_values = np.arange(max(self.x_values) + 1, max(self.x_values) + 4)
        next_y_values = np.poly1d(np.polyfit(self.x_values, self.y_values, 1))(next_x_values)
        combined_x_values = np.concatenate((self.x_values, next_x_values))
        combined_y_values = np.concatenate((self.y_values, next_y_values))
        plt.scatter(self.x_values, self.y_values, color='blue')
        plt.scatter(next_x_values, next_y_values, color='red')  # Color the next values in red
        plt.plot(combined_x_values, np.poly1d(np.polyfit(self.x_values, self.y_values, 1))(combined_x_values), color='blue', linestyle='dotted')
        if save_as_png:
            plt.savefig('scatter.png', format='png')
        plt.show()

    def bar(self, save_as_png=False):
        plt.bar(self.x_values, self.y_values)
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        if save_as_png:
            plt.savefig('bar.png', format='png')
        plt.show()

    def pie(self, save_as_png=False):
        plt.pie(self.y_values, labels=self.x_values, autopct='%1.1f%%')
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        if save_as_png:
            plt.savefig('pie.png', format='png')
        plt.show()

    def histogram(self, save_as_png=False):
        plt.hist(self.y_values, bins=len(self.x_values))
        plt.xlabel('X Values')
        plt.ylabel('Frequency')
        if save_as_png:
            plt.savefig('histogram.png', format='png')
        plt.show()

    def boxplot(self, save_as_png=False):
        plt.boxplot(self.y_values)
        plt.xticks(range(1, len(self.x_values) + 1), self.x_values)
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        if save_as_png:
            plt.savefig('boxplot.png', format='png')
        plt.show()

    def subplot(self, nrows, ncols, plot_number, save_as_png=False):
        plt.subplot(nrows, ncols, plot_number)
        plt.plot(self.x_values, self.y_values)
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        if save_as_png:
            plt.savefig(f'subplot_{plot_number}.png', format='png')
        plt.show()

    def set_style(self, style):
        plt.style.use(style)
        plt.plot(self.x_values, self.y_values)
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        plt.show()

class PyPlot3DWrapper:
    """
    A class that represents a 3D line chart.

    Attributes:
        x_values (list): A list of x values.
        y_values (list): A list of y values.
        z_values (list): A list of z values.

    Methods:
        plot(): Plots a 3D line chart.
    """

    def __init__(self, x_values, y_values, z_values):
        self.x_values = x_values
        self.y_values = y_values
        self.z_values = z_values

    def plot(self, save_as_png=False):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.x_values, self.y_values, self.z_values)
        ax.set_xlabel('X Values')
        ax.set_ylabel('Y Values')
        ax.set_zlabel('Z Values')
        if save_as_png:
            plt.savefig('plot.png', format='png')
        plt.show()

    def scatter(self, save_as_png=False):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.x_values, self.y_values, self.z_values)
        ax.set_xlabel('X Values')
        ax.set_ylabel('Y Values')
        ax.set_zlabel('Z Values')
        
        # Add the next 3 x, y, and z values to the scatter
        next_x_values = np.arange(max(self.x_values) + 1, max(self.x_values) + 4)
        next_y_values = np.poly1d(np.polyfit(self.x_values, self.y_values, 1))(next_x_values)
        next_z_values = np.poly1d(np.polyfit(self.x_values, self.z_values, 1))(next_x_values)
        combined_x_values = np.concatenate((self.x_values, next_x_values))
        combined_y_values = np.concatenate((self.y_values, next_y_values))
        combined_z_values = np.concatenate((self.z_values, next_z_values))
        ax.scatter(self.x_values, self.y_values, self.z_values, color='blue')
        ax.scatter(next_x_values, next_y_values, next_z_values, color='red')  # Color the next values in red
        # plot combined values
        ax.plot(combined_x_values, np.poly1d(np.polyfit(self.x_values, self.y_values, 1))(combined_x_values), np.poly1d(np.polyfit(self.x_values, self.z_values, 1))(combined_x_values), color='blue', linestyle='dotted')
        if save_as_png:
            plt.savefig('scatter.png', format='png')
        plt.show()

    def bar(self, save_as_png=False):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.bar(self.x_values, self.y_values, self.z_values)
        ax.set_xlabel('X Values')
        ax.set_ylabel('Y Values')
        ax.set_zlabel('Z Values')
        if save_as_png:
            plt.savefig('bar.png', format='png')
        plt.show()
    

class PyPlotWrapperFactory:
    """
    A factory class that creates instances of PyPlotWrapper and PyPlot3DWrapper.

    Methods:
        create_pyplot_wrapper(): Creates an instance of PyPlotWrapper.
        create_pyplot_3d_wrapper(): Creates an instance of PyPlot3DWrapper.
    """

    def create_pyplot_wrapper(self, x_values, y_values):
        return PyPlotWrapper(x_values, y_values)

    def create_pyplot_3d_wrapper(self, x_values, y_values, z_values):
        return PyPlot3DWrapper(x_values, y_values, z_values)

# Example usage
if __name__ == '__main__':
    factory = PyPlotWrapperFactory()
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 3, 5, 7, 11]
    z_values = [1, 4, 9, 16, 25]
    choice = input("Enter the type of plot (line, scatter, bar, pie, histogram, boxplot, subplot, 3d_line, 3d_scatter, 3d_bar): ")

    if choice == "line":
        plot = factory.create_pyplot_wrapper(x_values, y_values)
        plot.plot()
    elif choice == "scatter":
        plot = factory.create_pyplot_wrapper(x_values, y_values)
        plot.scatter()
    elif choice == "bar":
        plot = factory.create_pyplot_wrapper(x_values, y_values)
        plot.bar()
    elif choice == "pie":
        plot = factory.create_pyplot_wrapper(x_values, y_values)
        plot.pie()
    elif choice == "histogram":
        plot = factory.create_pyplot_wrapper(x_values, y_values)
        plot.histogram()
    elif choice == "boxplot":
        plot = factory.create_pyplot_wrapper(x_values, y_values)
        plot.boxplot()
    elif choice == "subplot":
        plot = factory.create_pyplot_wrapper(x_values, y_values)
        plot.subplot(2, 2, 1)
        plot.subplot(2, 2, 2)
        plot.subplot(2, 2, 3)
        plot.subplot(2, 2, 4)
    elif choice == "3d_line":
        plot3d = factory.create_pyplot_3d_wrapper(x_values, y_values, z_values)
        plot3d.plot()
    elif choice == "3d_scatter":
        plot3d = factory.create_pyplot_3d_wrapper(x_values, y_values, z_values)
        plot3d.scatter()
    elif choice == "3d_bar":
        plot3d = factory.create_pyplot_3d_wrapper(x_values, y_values, z_values)
        plot3d.bar()
    else:
        print("Invalid choice.")