# hello lightkurve

from lightkurve import search_targetpixelfile
pixelfile = search_targetpixelfile(8462852, quarter=16).download(quality_bitmask='hardest')
