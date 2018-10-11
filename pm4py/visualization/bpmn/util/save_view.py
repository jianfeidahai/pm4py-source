import shutil
import subprocess, os, sys

def view(bpmn_figure):
    """
    View on the screen a BPMN figure that has been rendered

    Parameters
    ----------
    bpmn_figure
        BPMN figure
    """
    is_ipynb = False

    try:
        get_ipython()
        is_ipynb = True
    except:
        pass

    if is_ipynb:
        from IPython.display import Image
        return Image(open(bpmn_figure, "rb").read())
    else:
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', bpmn_figure))
        elif os.name == 'nt':  # For Windows
            os.startfile(bpmn_figure)
        elif os.name == 'posix':  # For Linux, Mac, etc.
            subprocess.call(('xdg-open', bpmn_figure))

def save(bpmn_figure, output_file_path):
    """
    Save a BPMN figure that has been rendered

    Parameters
    -----------
    bpmn_figure
        BPMN figure
    output_file_path
        Path where the figure should be saved
    """
    shutil.copyfile(bpmn_figure, output_file_path)