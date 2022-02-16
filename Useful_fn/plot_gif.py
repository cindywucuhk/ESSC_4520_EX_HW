##################################################
### Plot gif
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful packages
##################################################
import imageio         # plotting gif


##################################################
## Functions
##################################################
def gif_plot(images, name):
  """ Plotting gif from images file.
    Arguments:
    images[list] - list that stored all the images
    name[str] - the saved-dir/name of the gif (without ".gif")
  """
  save_name = name + ".gif"
  imageio.mimsave(save_name, images, fps=5)


##################################################