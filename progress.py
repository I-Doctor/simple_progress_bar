'''
MIT License

Copyright (c) 2019 Kai Zhong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from time import time
from sys import stderr
from sys import stdout

__version__ = '1.0'

HIDE_CURSOR = '\x1b[?25l'
SHOW_CURSOR = '\x1b[?25h'


class Process(object):
    out_file = stderr
    check_tty = True
    hide_cursor = True

    def __init__(self, message='', **kwargs):
        self.index = 0
        self.start_time = time()
        self.now_time = self.start_time
        self.avg_time = AverageMeter()
        
        self.width = 0
        self.message = message
        self.line = ''

        if self.out_file and self.is_tty():
            if self.hide_cursor:
                print(HIDE_CURSOR, end='', file=self.out_file)
            self.out_file.flush()
    
    def 
