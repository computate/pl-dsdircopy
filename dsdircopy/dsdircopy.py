#                                                            _
# dircopy ds app
#
# (c) 2016 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os
import pudb

# import the Chris app superclass
from chrisapp.base import ChrisApp
#from distutils.dir_util import copy_tree

class DsdirCopy(ChrisApp):
    """
    Copy the *contents* of one or more obj storage directories given by the --dir
    argument to a new directory specified by <options.outpudir>. This argument is a
    string containing one or more directories separated by comma.
    """
    AUTHORS         = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH        = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC        = os.path.basename(__file__)
    EXECSHELL       = 'python3'
    TITLE           = 'A ChRIS ds app to copy obj storage directories'
    CATEGORY        = 'copy'
    TYPE            = 'ds'
    DESCRIPTION     = 'A plugin ds app to copy one or more obj storage directories'
    DOCUMENTATION   = 'http://wiki'
    LICENSE         = 'Opensource (MIT)'
    VERSION         = '1.0.0'
    MAX_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS = 1  # Override with integer value
    MAX_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Fill out this with key-value output descriptive info (such as an output file path
    # relative to the output dir) that you want to save to the output meta file when
    # called with the --saveoutputmeta flag
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        """
        self.add_argument('--dir', 
                          dest          = 'dir', 
                          type          = ChrisApp.unextpath,
                          optional      = False,
                          help          = 'directories to be copied')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        #output_folder = os.path.basename(options.dir.rstrip('/'))
        #output_path = os.path.join(options.outputdir, output_folder)
        #print('Copying %s to %s' % (options.inputdir, options.outputdir))
        #pudb.set_trace()
        #copy_tree(options.dir, options.outputdir)
        pass


# ENTRYPOINT
if __name__ == "__main__":
    app = DsdirCopy()
    app.launch()
