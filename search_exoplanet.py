# Search an exoplanet in the TOI list

import lightkurve as lk

target = '237532896'
result = lk.search_targetpixelfile(target)
result
