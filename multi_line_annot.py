import matplotlib.pyplot as plt


def update_annot(ind, line, annot, ydata):
    x, y = line.get_data()
    annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
    # Get x and y values, then format them to be displayed
    x_values = " ".join(list(map(str, ind["ind"])))
    y_values = " ".join(str(ydata[n]) for n in ind["ind"])
    # Format of label can be changed here
    text = "{}, {}".format(x_values, y_values)
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event, line, annot, ydata):
    vis = annot.get_visible()
    if event.inaxes == ax:
        # Draw annotations if cursor in right position
        cont, ind = line.contains(event)
        if cont:
            update_annot(ind, line, annot, ydata)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            # Don't draw annotations
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()


def plot_line(x, y):
    line, = plt.plot(x, y, marker="o")
    # Annotation style may be changed here
    annot = ax.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)
    fig.canvas.mpl_connect("motion_notify_event",
                           lambda event: hover(event, line, annot, y))


# Your data values to plot
x1 = range(21)
y1 = range(0, 21)
x2 = range(21)
y2 = range(0, 42, 2)
# Plot line graphs
fig, ax = plt.subplots()
plot_line(x1, y1)
plot_line(x2, y2)
plt.show()
