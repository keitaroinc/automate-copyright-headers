import os

def add_headers(license, year, path, ext, long_comment_start, long_comment_end):
    AGPL_30_header = "\nThis program is free software: you can redistribute it and/or modify\nit under the terms of the GNU Affero General Public License as\npublished by the Free Software Foundation, either version 3 of the\nLicense, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the\nGNU Affero General Public License for more details.\n\nYou should have received a copy of the GNU Affero General Public License\nalong with this program.  If not, see <https://www.gnu.org/licenses/>.\n"

    Apache_20_header = '\nLicensed under the Apache License, Version 2.0 (the "License");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\nhttps://www.apache.org/licenses/LICENSE-2.0\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.'

    copyright_warning = "********************** File may contain copyright notice. Inspect manually **********************"

    copyright_line="Copyright (c) "+ year +" Keitaro AB"
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if ext in file:
                f1name = str(os.path.join(root,file))
                f1 = open(f1name, "r")
                f1lines = f1.readlines()
                f1.close()
                add_header = True
                counts = 0
                for line in f1lines:
                    if ("copyright" in line or "Copyright" in line or "license" in line or "License" in line):
                        print (f1name, copyright_warning)
                        add_header = False
                        break
                    elif ("vendor" in f1name or ".min.js" in f1name):
                        print (f1name, copyright_warning)
                        add_header = False
                        break
                    counts = counts + 1
                    if (counts > 15):
                        break
                if (add_header):
                    f2name = os.path.join("copy",root,"tmp")
                    f2 = open(f2name, "w")
                    f2.write(long_comment_start)
                    f2.write("\n")
                    f2.write(copyright_line)
                    if (license == "AGPL"):
                        f2.write(AGPL_30_header)
                    elif (license == "Apache"):
                        f2.write(Apache_20_header)
                    f2.write(long_comment_end)
                    f2.write("\n")
                    f2.write("\n")
                    for i in range(0, len(f1lines)):
                        f2.write(f1lines[i])
                    os.remove(f1name)
                    os.replace(f2name, f1name)

                
                
year="2018"
path = os.getcwd()
license = "Apache"
add_headers(license, year, path, ".py", '"""', '"""')
add_headers(license, year, path, ".js", "/*", "*/")
add_headers(license, year, path, ".css", "/*", "*/")
add_headers(license, year, path, ".html", "<!--", "-->")


