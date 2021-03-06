from urllib.request import urlretrieve

__author__ = 'saturn4er'

import core.BasicLibs.fs as fs


def download_file(url, destination=''):
    print('Downloading file %s to %s' % (url, destination))
    fs.require_full_path(destination)
    fname, _ = urlretrieve(url, destination)
    return fname
