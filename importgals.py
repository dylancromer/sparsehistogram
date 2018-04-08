import numpy as np

def import_csv(filename):
    infile = open(filename,'r')
    str_gals_transpose = []
    for i,line in enumerate(infile):
        try:
            if line[0] != '#':
                str_gals_transpose.append(line.split(','))
        except:
            pass
    infile.close()
    str_gals = np.asarray(str_gals_transpose).transpose()
    del str_gals_transpose
    gals = str_gals.astype(np.float)
    del str_gals
    return gals

def import_dat(filename):
    infile = open(filename,'r')
    str_gals_transpose = []
    for i,line in enumerate(infile):
        try:
            if line[0] != '#':
                str_gals_transpose.append(line.split())
        except:
            pass
    infile.close()
    str_gals = np.asarray(str_gals_transpose).transpose()
    del str_gals_transpose
    gals = str_gals.astype(np.float)
    del str_gals
    return gals

def import_csv_nonp(filename):
    infile = open(filename,'r')
    str_gals_transpose = []
    for i,line in enumerate(infile):
        try:
            if line[0] != '#':
                line = line.rstrip()
                str_gals_transpose.append(line.split(','))
        except:
            pass
    infile.close()
    gals = str_gals_transpose
    return gals
