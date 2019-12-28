#!/usr/bin/env python
import manimlib
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
if __name__ == "__main__":
    manimlib.main()
else:
    manimlib.stream_starter.start_livestream()
