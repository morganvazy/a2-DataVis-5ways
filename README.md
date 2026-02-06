


Readme Requirements
---

A good readme with screenshots and structured documentation is required for this project. 
It should be possible to scroll through your readme to get an overview of all the tools and visualizations you produced.

- Each visualization should start with a top-level heading (e.g. `# d3`)
- Each visualization should include a screenshot. Put these in an `img` folder and link through the readme (markdown command: `![caption](img/<imgname>)`.
- Write a paragraph for each visualization tool you use. What was easy? Difficult? Where could you see the tool being useful in the future? Did you have to use any hacks or data manipulation to get the right chart?

Other Requirements
---

0. Your code should be forked from the GitHub repo.
1. Place all code, Excel sheets, etcetera in a named folder. For example, `r-ggplot, matlab, mathematica, excel` and so on.
2. Your writeup (readme.md in the repo) should also contain the following:

- Description of the Technical achievements you attempted with this visualization.
  - Some ideas include interaction, such as mousing over to see more detail about the point selected.
- Description of the Design achievements you attempted with this visualization.
  - Some ideas include consistent color choice, font choice, element size (e.g. the size of the circles).

**NOTE: THE BELOW IS A SAMPLE ENTRY TO GET YOU STARTED ON YOUR README. YOU MAY DELETE THE ABOVE.**

# R + ggplot2 + plotly + HTML widgets

R is a language used for statistical computing and data visualization. ggplot2 is a data visualization library in R. plotly is a graphing library that allows for interactive graphs.
HTML widgets is a framework that can embed interactive visualizations without requiring Javascript coding.

I created a static visualization of the penglings dataset using ggplot2's "geom_point()", aesthetic functions for the color and size of the data points, and labs() for the axis labels. The colors are hex codes that match the colors of the graph we were tasked with replicating. Creating a manual scale and using hex codes let me keep consistent colors across all of my graphs.
I created an interactive visualization using plotly. When mousing over a point, a box appears showing the Flipper length, body mass, species, and bill length of the penguin that is represented by that data point. The box disappears when the mouse is removed.

Examples and documentation for ggplot2 and plotly were abundant and easy to find. ggplot2 allows for a diverse visualization with little code. The biggest barrier was familiarizing myself with the goem_point() and aes() functions since I had no previous experience with these.

![ggplot2](img/MVggplot2_plot.png)

## Technical Achievements
- Hover feature that shows the penguin's flipper length, body mass, species, and bill length using plotly.
## Design Achievements
- created a manual color scale with hex codes so colors were accurate to the original reference picture
## Sources & References
- https://www.sthda.com/english/wiki/ggplot2-scatter-plots-quick-start-guide-r-software-and-data-visualization - reference for scatterplot
- https://ggplot2.tidyverse.org/reference/labs.html - used for axis labels
- https://stackoverflow.com/questions/37465285/interactive-scatter-plots-in-r-overlay-hover-summary-tooltip-as-user-supplied-p - used for hover feature

# d3...

(And so on...)


## Technical Achievements
- **Proved P=NP**: Using a combination of...
- **Solved AI Forever**: ...

### Design Achievements
- **Re-vamped Apple's Design Philosophy**: As demonstrated in my colorscheme...
