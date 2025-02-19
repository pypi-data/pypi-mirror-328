from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import ttk
from arnica.plots.hoveritems import HoverItems

PADDING = 3


class Viewer2D:
    def __init__(self, master: ttk.Frame, otroot, callback_2d: callable):
        """Creation of a viewer for matplotlib figures"""
        self.otroot = otroot
        self.callback_2d = callback_2d

        # Header frame to refresh
        _header_frame = ttk.Frame(master)
        _header_frame.pack(side="top", fill="both", padx=PADDING, pady=PADDING)
        refresh2d = ttk.Button(
            _header_frame, text="refresh2d", command=self.refresh_2d_view
        )
        refresh2d.pack(side="top")

        # Create a Frame to hold the plot
        _canvas_frame = ttk.Frame(master)
        _canvas_frame.pack(
            side="top", padx=PADDING, pady=PADDING, fill="both", expand=True
        )

        # Create the Matplotlib figure and axes
        _fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = _fig.add_subplot(111)
        # self.fig, self.ax = plt.subplots()
        # Embed the figure into the Tkinter frame
        self.canvas = FigureCanvasTkAgg(_fig, master=_canvas_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side="top", fill="both", expand=True)
        # create the hover object
        self.hover = HoverItems(self.ax)

        # Add the Matplotlib Navigation Toolbar
        # Header frame to refresh
        _footer_frame = ttk.Frame(master)
        _footer_frame.pack(side="top", fill="x", padx=PADDING, pady=PADDING)
        _toolbar = NavigationToolbar2Tk(self.canvas, _footer_frame)
        _toolbar.update()
        _toolbar.pack(side="top", fill="x", expand=True)

    def refresh_2d_view(self):
        self.ax.clear()
        self.callback_2d(self.ax, self.hover, self.otroot.get())
        self.canvas.draw_idle()
