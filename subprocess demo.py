#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess
'''
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n')
obj.stdin.write('print 2 \n')
obj.stdin.write('print 3 \n')
obj.stdin.write('print 4 \n')
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print cmd_out
print cmd_error
'''

child1 = subprocess.Popen(["cat","/etc/passwd"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
child2 = subprocess.Popen(["grep","0:0"],stdin=child1.stdout, stdout=subprocess.PIPE)
out = child2.communicate()