'''
<license>
  * Copyright (C) 2024-2025 abdelmathin.com, Abdelmathin Habachi.
  *
  * https://abdelmathin.com
  * https://github.com/Abdelmathin/futilz
  *
  * Permission is hereby granted, free of charge, to any person obtaining
  * a copy of this software and associated documentation files (the
  * "Software"), to deal in the Software without restriction, including
  * without limitation the rights to use, copy, modify, merge, publish,
  * distribute, sublicense, and/or sell copies of the Software, and to
  * permit persons to whom the Software is furnished to do so, subject to
  * the following conditions:
  *
  * The above copyright notice and this permission notice shall be
  * included in all copies or substantial portions of the Software.
  *
  * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
  * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
  * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
  * CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
  * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
  *
  * File   : __init__.py
  * Created: 2025/02/05 15:18:57 GMT+1
  * Updated: 2025/02/05 15:18:57 GMT+1
</license>
'''

import os
import sys
import hashlib

__author__ = "Abdelmathin Habachi"
__github__ = "https://github.com/Abdelmathin/futilz"

class DotEnv:

    def __init__(self, reference = None):
        self.reference = reference

    def loadfirst(self, depth = None, environ = None, only = None, update_path = False):
        if (environ == None):
            environ = os.environ
        envfile   = None
        currdir   = os.path.abspath(self.reference)
        currdepth = 0
        while (currdepth < 1000) and (currdir != os.path.dirname(currdir)):
            if (depth and abs(depth) < currdepth):
                break
            tmpfile = os.path.join(currdir, ".env")
            if os.path.exists(tmpfile):
                envfile = tmpfile
                break
            currdir = os.path.dirname(currdir)
            currdepth += 1
        if not envfile:
            return ({})
        #
        try    : env_content = open(envfile).read()
        except : env_content = ""
        retval = {}
        for line in env_content.split("\n"):
            line = line.strip()
            if not ("=" in line):
                continue
            key   = line[:line.index("=")].strip()
            value = line[line.index("=") + 1:].strip()
            if not key or key.startswith("#"):
                continue
            if key.startswith("{{") and key.endswith("&"):
                if not update_path:
                    continue
                sys.path.insert(0, value)
                continue
            if key.startswith("{{") and key.endswith("+"):
                if not update_path:
                    continue
                sys.path.append(value)
                continue
            environ[key] = value
            retval[key]  = value
        return (retval)

def get_repo_dir():
    tries    = 0
    repo_dir = os.path.abspath(__file__)
    while (tries < 1000) and (os.path.dirname(repo_dir) != repo_dir):
        if os.path.exists(os.path.join(repo_dir, ".git")):
            return (repo_dir)
        tries += 1
        repo_dir = os.path.dirname(repo_dir)
    return (None)

def fix_path(path):
    for c in ["/./", "//"]:
        while (c in path):
            path = path.replace(c, "/")
    return (path)

def create_directory(dirname):
    d = ""
    for item in dirname.split("/"):
        d += item + "/"
        try    : os.mkdir(d)
        except : pass

def get_file_extension(filename):
    if (not filename) or not ("." in filename):
        return ("")
    if ("://" in filename[:16]):
        '''
            caseOf: http:// , https://, ftp:// ...
        '''
        filename = filename[filename.index("://") + len("://"):]
        filename = filename.strip().strip("/")
        if not ("/" in filename):
            return ("")
        filename = filename[filename.index("/") + len("/"):]
        for c in "?&#":
            '''
                remove queries, only for url's
            '''
            filename = filename.split(c)[0]
    if not ("." in filename):
        return ("")
    return (filename.split(".")[-1])

def is_image_extension(extension):
    return (extension in [
        "png" , "jpg" , "svg", "jpeg", "bmp" , "apng" ,
        "avif", "gif" , "jpg", "jpeg", "jfif", "pjpeg",
        "pjp" , "webp", "ico", "cur" , "tif" , "tiff"
    ])

def is_font_extension(extension):
    return (extension in [
        "ttf"
    ])

def find(
        dirname             = ".",
        files               = None,
        excluded            = None,
        extensions          = None,
        excluded_extensions = None,
        callback            = None,
        basedir             = None
    ):

    dirname = os.path.realpath(dirname).rstrip("/\\")
    if (basedir == None):
        basedir = dirname
    if (files == None):
        files = {}
    try:
        listfiles = os.listdir(dirname)
    except:
        return (files)
    for basename in listfiles:
        if (excluded) and (basename in excluded):
            continue
        file_ext = get_file_extension(basename)
        if (file_ext):
            if (extensions) and (not (file_ext in file_ext)):
                continue
            if (excluded_extensions) and (file_ext in excluded_extensions):
                continue
        filename = os.path.realpath(os.path.join(dirname, basename))
        find(
            dirname             = filename           ,
            files               = files              ,
            excluded            = excluded           ,
            extensions          = extensions         ,
            callback            = callback           ,
            excluded_extensions = excluded_extensions,
            basedir             = basedir
        )
        if (os.path.isdir(filename)):
            continue
        if (callback):
            callback(filename)
        files[filename] = filename[len(basedir):].strip("/\\")
    return (files)

def shasum_content(content, algo = "sha1"):
    try    : input_bytes = content.encode("utf-8")
    except : input_bytes = content
    hash_func = getattr(hashlib, algo, None)
    if hash_func is None:
        raise ValueError(f"Unsupported algorithm: {algo}")
    sha256 = hash_func()
    sha256.update(input_bytes)
    return (sha256.hexdigest())

def shasum_file(filename, mode = "r", algo = "sha1"):
    """
        Compute SHA hash of a given file
    """
    hash_func = getattr(hashlib, algo, None)
    if hash_func is None:
        raise ValueError(f"Unsupported algorithm: {algo}")
    with open(filename, "rb") as fp:
        hasher = hash_func()
        while chunk := fp.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def download_file(url, filename, headers = None):
    import requests as http_requests
    if not headers:
        headers = {
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
    basename = filename.split("/")[-1]
    dirname  = filename[:-len(basename)]
    create_directory(dirname)
    rsp = http_requests.get(
        url     = url,
        headers = headers
    )
    content = rsp.content
    try:
        with open(filename, "w") as fp:
            fp.write(content.decode("UTF-8"))
    except:
        with open(filename, "wb") as fp:
            fp.write(content)
