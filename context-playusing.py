# Module: default
# Author: jurialmunkey
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
import sys
import xbmc

if __name__ == '__main__':
    xbmc.executebuiltin(f'RunPlugin({sys.listitem.getProperty("tmdbhelper.context.playusing")})')
