# MultiAnnotationLineGraph
Example code on how to annotate multiple lines using matplotlib.  
Generalises an example found on stackoverflow to accomodate many lines.

# How to Use
Ensure matplotlib is installed.  
Add multi_line_annot.py to the folder your project is in.  
Add ```import multi_line_annot.py as mla```  to top of your file.  
Then use these commands to create the graph:  
```
    # Initialise new graph
    new_graph = LineGraph()
    # Plot as many lines as needed
    new_graph.plot_line(x1, y1)
    new_graph.plot_line(x2, y2)
    # Open window and display graph
    new.show_graph()
```

# What I Learned
Increased readability of file.  
Simple matplotlib graphing(lines, bars).  
Matplotlib annotations, subplots.  
f strings  

# Acknowledgements
Original code comes from 'ImportanceOfBeingErnest' on Stackoverflow.  
https://stackoverflow.com/a/47166787/10302020  