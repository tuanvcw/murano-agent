# Copyright (c) 2013 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    import win32file
    import os

    def symlink(source, link_name):
        src = os.path.abspath(source)
        dest = os.path.abspath(link_name)
        win32file.CreateSymbolicLink(dest, src, 0)

    os.symlink = symlink
except ImportError:
    pass