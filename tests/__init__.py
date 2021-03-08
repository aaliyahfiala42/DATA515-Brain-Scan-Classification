import sys, os
path = os.path.dirname(__file__)
path = os.path.join(path, 'brain-scan')
if path not in sys.path:
    sys.path.append(path)
