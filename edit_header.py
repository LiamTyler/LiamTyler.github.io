import os
from pathlib import Path

addition = \
"""
<!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-145372343-1"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'UA-145372343-1');
    </script>
"""

rootdir = Path('/home/liam/Documents/LiamTyler.github.io/')
file_list = [f for f in rootdir.glob('**/*.html') if f.is_file()]

for f in file_list:
    newFile = ""
    with open(f, 'r') as fp:
        for line in fp:
            if line.strip() == "</head>":
                newFile += addition
            newFile += line

    if newFile != "":
        fp = open(f, 'w')
        fp.write(newFile)


