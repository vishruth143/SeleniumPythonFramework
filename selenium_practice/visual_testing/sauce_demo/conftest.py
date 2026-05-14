"""
conftest.py — adds visual_testing/ to sys.path so that
`from framework.*` and `from sauce_demo.*` resolve correctly
when pytest is run from within the sauce_demo/ folder.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

