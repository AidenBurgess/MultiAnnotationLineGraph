import matplotlib.pyplot as plt


class LineGraph:

    def __init__(self):
        # Disable toolbar - optional
        plt.rcParams['toolbar'] = 'None'
        self.fig, self.ax = plt.subplots()
        # X and Y labels
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        # Title
        plt.suptitle('Title', fontsize=16)

    def update_annot(self, line, annot):
        # Get x and y values
        x, y = line.get_data()
        x = x[self.ind["ind"][0]]
        y = y[self.ind["ind"][0]]
        # Change location of annotation
        annot.xy = (x, y)
        # Text to display on label
        text = f"{x}, {int(y):,}"
        annot.set_text(text)
        # Set transparency
        annot.get_bbox_patch().set_alpha(0.8)

    def hover(self, event, line, annot):
        vis = annot.get_visible()
        if event.inaxes == self.ax:
            cont, self.ind = line.contains(event)
            # Set annotation if cursor contacts line
            if cont:
                self.update_annot(line, annot)
                annot.set_visible(True)
                self.fig.canvas.draw_idle()
            else:
                # Don't draw annotations
                if vis:
                    annot.set_visible(False)
                    self.fig.canvas.draw_idle()

    def plot_line(self, x, y):
        line, = plt.plot(x, y, marker="o")
        # Annotation style may be changed here
        annot = self.ax.annotate("", xy=(0, 0), xytext=(-20, 20),
                                 textcoords="offset points",
                                 bbox=dict(boxstyle="round", fc="w"),
                                 arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)
        self.fig.canvas.mpl_connect("motion_notify_event",
                                    lambda event: self.hover(event, line, annot))

    def show_graph(self):
        plt.show()


if __name__ == '__main__':
    # Your data values to plot
    x1 = range(21)
    y1 = range(0, 21)
    x2 = range(21)
    y2 = range(0, 42, 2)
    # Plot line graphs
    new = LineGraph()
    new.plot_line(x1, y1)
    new.plot_line(x2, y2)
    new.show_graph()
