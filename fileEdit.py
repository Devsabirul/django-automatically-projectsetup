def add_text(filepath, insert_text, index_number):
    f = open(filepath, "r")
    line_index = index_number
    lines = None
    lines = f.readlines()
    lines.insert(line_index, insert_text)
    f = open(filepath, 'w')
    f.writelines(lines)
    f.close()


def replace(filepath, find_text, replace_text):
    # read input file
    fin = open(filepath, "rt")
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    data = data.replace(find_text, replace_text)
    # close the input file
    fin.close()
    # open the input file in write mode
    fin = open(filepath, "wt")
    # overrite the input file with the resulting data
    fin.write(data)
    # close the file
    fin.close()
    return fin


def checkSettingsFile(filepath):
    f = open(filepath, "rt")
    data = f.read()

    if "'DIRS': []," and "'django.contrib.staticfiles'," and "STATIC_URL = '/static/'" in data:
        # add Install App in settings.py ------------------------
        replace(filepath, "'django.contrib.staticfiles',",
                "'django.contrib.staticfiles',\n    'core',")
        # Insert DIRS file
        replace(filepath,
                "'DIRS': [],", '"DIRS": [os.path.join(BASE_DIR, "templates")],')
        # Add Static url root media file
        replace(filepath,
                "STATIC_URL = '/static/'", "STATIC_URL = 'static/'\nSTATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')\nSTATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]\n\n\nMEDIA_ROOT = os.path.join(BASE_DIR, 'media')\nMEDIA_URL = '/media/'")
    elif "path('admin/', admin.site.urls)," in data:
        replace(filepath,
                "path('admin/', admin.site.urls),", "path('admin/', admin.site.urls),\n    path('', include('core.urls'))")
    elif '"django.contrib.staticfiles"' and '"DIRS": [],' and 'STATIC_URL = "static/"' in data:
        # add Install App in settings.py ------------------------
        replace(filepath, '"django.contrib.staticfiles",',
                "'django.contrib.staticfiles',\n    'core',")
        # Insert DIRS file
        replace(filepath,
                '"DIRS": [],', '"DIRS": [os.path.join(BASE_DIR, "templates")],')
        # Add Static url root media file
        replace(filepath,
                'STATIC_URL = "static/"', "STATIC_URL = 'static/'\nSTATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')\nSTATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]\n\n\nMEDIA_ROOT = os.path.join(BASE_DIR, 'media')\nMEDIA_URL = '/media/'")
    elif 'path("admin/", admin.site.urls),' in data:
        replace(filepath,
                'path("admin/", admin.site.urls),', "path('admin/', admin.site.urls),\n    path('', include('core.urls'))")
