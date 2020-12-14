# Vince J. Straub, 2020
# https://stackoverflow.com/questions/38478409/finding-out-complementary-opposite-color-of-a-given-color

from matplotlib import colors as mcolors
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random 
import glob 


class SRWdrawer:
    """Creates a simple random walk drawing in 2 dimensions
       composed of a plot, a line (lattice path) made up of 
       n number of steps, where n is a parameter provided by 
       the user or chosen randomly, and face color (background)
       with a color complementary to that of the line. The 
       current limit of n is set to 10000000. Fig size, face 
       color, number of panels (grid size) are all arguments 
       that can be set by the user upon initialization."""

    def __init__(self, steps=random.randint(0, 10000000), fig_size=(12, 10), face_color='', cols=3, rows=3):
        # Declare class fields
        self.steps = steps 
        self.cumstom_fig_size = fig_size
        self.cumstom_face_color = face_color
        self.num_cols = cols 
        self.num_rows = rows

    def fill_array(self, x, y):
        """Returns non-zero 1D arrays of size n"""
        for i in range(1, self.steps): 
            val = random.randint(1, 4) 
            if val == 1: 
                x[i] = x[i - 1] + 1
                y[i] = y[i - 1] 
            elif val == 2: 
                x[i] = x[i - 1] - 1
                y[i] = y[i - 1] 
            elif val == 3: 
                x[i] = x[i - 1] 
                y[i] = y[i - 1] + 1
            else: 
                x[i] = x[i - 1] 
                y[i] = y[i - 1] - 1
        return x, y

    def get_panel_number(self, panel_val, set_cols=True):
        """Returns column or row argument entered by user
        otherwise returns default value of 3."""
        if set_cols == True:
            if panel_val == 3:
                pass
            else: 
                panel_val == self.num_cols
        else:
            if panel_val == 3:
                pass 
            else:
                panel_val == self.num_rows
        return panel_val

    def get_fig_size(self, size):
        """Returns figure size entered by user
        otherwise returns default value of (12, 10)."""
        if size == (12, 10):
            pass
        else: 
            size == self.cumstom_fig_size
        return size

    def check_color(self, cumstom_color, line_color):
        """Returns custom color or random color if custom
        color string is left empty."""
        if cumstom_color == '':
            face_color = self.get_complementary_color(line_color)
        else:
            face_color = self.cumstom_face_color
        return face_color
   
    def get_color(self):
        """"Returns random color."""
        mpl_colors = list(mcolors.cnames.values())
        color = mpl_colors[random.randint(0,len(mpl_colors)-1)]
        return color
    
    def get_complementary_color(self, hex):
        """Returns complementary RGB color."""
        if hex[0] == '#':
            hex = hex[1:]
        rgb = (hex[0:2], hex[2:4], hex[4:6])
        comp = ['%02X' % (255 - int(a, 16)) for a in rgb]
        return '#'+''.join(comp)

    def get_fig(self, num_cols, num_rows, fig_size):
       """Returns figure with 1 or more grid panels where each 
       panel has a different random walk pattern."""
       fig, axes = plt.subplots(ncols=num_cols, nrows=num_rows, constrained_layout=True, figsize=fig_size)
       fig.patch.set_alpha(0)
       for i, ax in enumerate(fig.axes):
           # Declare and fill two empty 1D arrays of size n
           x, y = self.fill_array(np.zeros(self.steps), np.zeros(self.steps))
           # Generate line and face color
           line_color = self.get_color()
           face_color = self.check_color(self.cumstom_face_color, line_color)
           ax.set_facecolor(face_color)
           # Hide axes
           ax.axes.get_xaxis().set_visible(False)
           ax.axes.get_yaxis().set_visible(False)
           ax.spines['top'].set_visible(False)
           ax.spines['right'].set_visible(False)
           ax.spines['bottom'].set_visible(False)
           ax.spines['left'].set_visible(False)
           # Plot panel
           ax.plot(x, y, color=line_color, linewidth=0.2, linestyle='--') 
    
    def show_fig(self):
        fig_size = self.get_fig_size(self.cumstom_fig_size)
        num_cols = self.get_panel_number(self.num_cols)
        num_rows = self.get_panel_number(self.num_rows, set_cols=False)
        self.get_fig(num_cols, num_rows, fig_size)
        plt.show()

    def save_fig(self, file_num=1, type='png'):
        fig_size = self.get_fig_size(self.cumstom_fig_size)
        num_cols = self.get_panel_number(self.num_cols)
        num_rows = self.get_panel_number(self.num_rows, set_cols=False)
        self.get_fig(num_cols, num_rows, fig_size)
        plt.savefig('{}.{}'.format(str(file_num), type), bbox_inches='tight', pad_inches=0.25)


if __name__ == "__main__":
    num_images = int(input("What number of figures would you like to create?"))
    for n in range(1, num_images+1):
        srw=SRWdrawer()
        srw.save_fig(file_num=n)
        plt.close()
    print('\n All figures saved to file. Showing last figure...')
    srw.save_fig()