# code = UTF-8
# Author:fineSummer
# Date:2021-07-12 16:15

import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./script')

    runner = unittest.TextTestRunner()

    runner.run(suite)