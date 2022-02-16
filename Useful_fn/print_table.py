##################################################
### Print table
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful packages
##################################################
import numpy as np                # for nummerical munipilation
from tabulate import tabulate     # plot table


##################################################
def print_table(table_ls, heading):
  """ Printing the data in a table format
    Arguments:
    table_ls[list] - Row names & data you want to print, in a format of [[row_name],[data 1], [data 2], ...]
    heading - Column names, in a format of [" ", "col_name 1", "col_name 2", ...]
  """
  # get a correct format by transposing the data
  table_ls = np.array(table_ls).T.tolist()
  # print the data in table format
  print(tabulate(table_ls, headers=heading))
