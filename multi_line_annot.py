import matplotlib.pyplot as plt


class LineGraph():

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        # Label the graph
        # X and Y labels
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        # Titles
        plt.suptitle('Title of Graph', fontsize=16)

    def update_annot(self, ind, line, annot, ydata):
        x, y = line.get_data()
        annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
        # Get x and y values, then format them to be displayed
        x_values = " ".join(list(map(str, ind["ind"])))
        y_values = " ".join(str(ydata[n]) for n in ind["ind"])
        # Format of label can be changed here
        text = "{}, {}".format(x_values, y_values)
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.4)

    def hover(self, event, line, annot, ydata):
        vis = annot.get_visible()
        if event.inaxes == self.ax:
            # Draw annotations if cursor in right position
            cont, ind = line.contains(event)
            if cont:
                self.update_annot(ind, line, annot, ydata)
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
                                    lambda event: self.hover(event, line, annot, y))

    def show_graph(self):
        plt.show()


# Your data values to plot
x1 = range(21)
y1 = range(21)
x2 = range(21)
y2 = range(0, 42, 2)
# Create new graph
new_graph = LineGraph()
new_graph.plot_line(x1, y1)
new_graph.plot_line(x2, y2)
new_graph.show_graph()
