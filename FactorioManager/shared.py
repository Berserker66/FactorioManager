__author__ = 'Fabian'
import sys

is_frozen = hasattr(sys, "frozen") and sys.frozen

del(sys)