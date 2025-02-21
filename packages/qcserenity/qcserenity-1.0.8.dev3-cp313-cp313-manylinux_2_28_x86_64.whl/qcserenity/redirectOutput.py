import os
import sys

class redirectOutputToFile(object):
    '''
    A context manager that redirects stdout to a file for its scope, usage:

    with redirectOutputToFile('output.txt'):
        os.system('ls -l')
    '''
    
    def __init__(self, filepath, *args, **kw):
        sys.stdout.flush()
        self._origstdout = sys.stdout
        self._oldstdout_fno = os.dup(sys.stdout.fileno())
        self._file = open(filepath, 'w')  # Open your file for writing

    def __enter__(self):
        self._newstdout = os.dup(1)
        os.dup2(self._file.fileno(), 1)  # Redirect stdout to the file
        sys.stdout = os.fdopen(self._newstdout, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self._origstdout
        sys.stdout.flush()
        os.dup2(self._oldstdout_fno, 1)  # Restore original stdout
        self._file.close()  # Ensure the file is closed