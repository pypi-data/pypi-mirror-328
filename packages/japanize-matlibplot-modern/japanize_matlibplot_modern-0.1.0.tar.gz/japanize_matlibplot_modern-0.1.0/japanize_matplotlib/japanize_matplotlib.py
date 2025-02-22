import os
import re
import matplotlib
from matplotlib import font_manager

FONTS_DIR = 'fonts'
FONT_NAME = "IPAexGothic"
FONT_TTF = 'ipaexg.ttf'


def parse_version(version_string):
    """
    Extracts up to (major, minor, patch) from a version string like '3.2.1' or '3.1.0rc2'.
    If it fails, returns (0, 0, 0) by default.
    """
    match = re.match(r'^(\d+)\.(\d+)(?:\.(\d+))?', version_string)
    if match:
        major = int(match.group(1))
        minor = int(match.group(2))
        patch = int(match.group(3)) if match.group(3) else 0
        return (major, minor, patch)
    return (0, 0, 0)


def japanize():
    font_dir_path = get_font_path()
    font_dirs = [font_dir_path]
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

    # Parse the matplotlib version without LooseVersion
    mpl_version = parse_version(matplotlib.__version__)

    # Compare tuple (major, minor, patch) against (3, 2, 0)
    # If < (3,2,0), it means we still need createFontList
    is_support_createFontList = mpl_version < (3, 2, 0)

    if is_support_createFontList:
        font_list = font_manager.createFontList(font_files)
        font_manager.fontManager.ttflist.extend(font_list)
    else:
        for fpath in font_files:
            font_manager.fontManager.addfont(fpath)

    matplotlib.rc('font', family=FONT_NAME)


def get_font_ttf_path():
    return os.path.join(get_font_path(), FONT_TTF)


def get_font_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), FONTS_DIR))


# Test call
japanize()
