#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import os.path
import tempfile
import base64


logo = ''
logo += 'R0lGODlhIAAgAPcAAAIBApuBfT9BRX8VGzchFQMTBSQCAd/BvwcEDwEKARIBAqNGSf/j262jnAMB'
logo += 'CKxmZevx4bttdwIFAdKEhBMLBIUvLxMBCf2lu+v192NdT+nVywwBAToVDwMKCNuPlgMFCNVoe64o'
logo += 'Ng8VFt2loBgGAt/j7f/58qhwbQkKDhsBA//b1SknL92TlntDQwEOAqNRU9np24tfVQMCBeCtrQsB'
logo += 'Bdt5ea6QkR4RC8/K0MdnbwsBCP/75Z0tOwUOCQwFCRINDhUBBRUHCP/T2681M/n6/wIDAYsfLqVl'
logo += 'agsDAvqUnAoSDaR5egoGA9yDiRQPB+OzsQYcFuGkpslVVSsuLAsJBfjz+1hdZeB7jb2BfwIBC//0'
logo += '7B0BB3lTUfzq4WRUWN3LwwIKBREDAv/i5KmxqQMHBf/UzQUJCwMHCz01M8+Nh4cXFcmjnBQKCjsR'
logo += 'GwUHB85wcQIOBX9ta5A1Oa48Svv+/+O5wcaGjf/t6v/U0wYBAT1TSzYiJhQFEBYBAsdCVAMDCAEH'
logo += 'AVY2MqFVWSMLEaEZL//L0EU/R5gvKuNVaZVMVfqEksWVkj8eHv7u8tM/UI9PSYAcJKswRFshK2dC'
logo += 'PlRmWlNPQ/+srE81K5ESJvF5j+2+ufF3fWc/QaclMa5dX/+vtP+ll82npv+krMJ8fO5vfJNrYa9p'
logo += 'abFLVa8+OFMjM/nCvSAdH2NcZu3v+/mbl8h2df/MyptVVp0NF8ttd/+0xD0rJe+De+vv6b9nWQoa'
logo += 'DpppbK8wOO+PjxsTH8FLTaE1Mc2bm+uEjfy4tP6Kk21jbdqYmGU9OcFlbv+xwX07Q69ZSfx+jqF/'
logo += 'f5AdKNtwettmbWBjV4thX//GyHQ2M19TR9VdYbdVXf/25d9/g/+zpw0ZCYtLSe+ho7c2QDkPFFEZ'
logo += 'Hx0YDsCKiv/N2bGHgf/28/iaorNjZcOnn8h1ev+HndtTW5szPicEC/z77LeGgrMjPfz99P/d3Pmo'
logo += 'q75sbrRGQwQOEN+IirF1d08zMZdUThUPFvGJiWdLRzAWGf/m54E7OSH5BAAAAAAALAAAAAAgACAA'
logo += 'Bwj/AAcBUQBkS4o+CjZQYQJISQ8kFBT0iRboIJANHzq4IcOESZ8UGzbk2SAxZBgkSgCElJii1KI1'
logo += 'nFIosCADgIwiAEYmzAMGEICfOfMAoGAgmYdEsbBMOxGNHbsNQIGO3MIGTgKbHSQA+AGARIQr66SI'
logo += 'asLNnDsbe0RGBVCkSJ88CRLI+NADTg8ATpaAQLSsEylSTQQt4RIyDw0aPyUAStBngwQwOmSAcSFh'
logo += 'SgMsIdJJU6doUzN0dw7UUpmnNNvFIIt8AELjDxQ9t8hFceRo05AQu+TF6/LlhoTSagHEDSPSQh8g'
logo += 'vQzRMdHFXxJZqCwlaYbtzjknWgHQ2EAjT5HFQfIg/7GwwUKqKlXIiZNW6BkqWLAWjDgHrkgCrTIO'
logo += '53EjoQOAVTlt4A0yFzQijScLfOLKIW+8UQwWBBRRQFxm+ECDBUIJl0ARVIADACdXRCIOOk288kgZ'
logo += '2AzwwDiX5KFEXPXI4AAx2gnVARwujISECpi8s4wzzsgTgwqizBJOLVC5AAgZHThgRRWGAICCUD4Z'
logo += 'wAkH18zhSDfD8PDKGl0IYQc+QklQhBlmOIkBHTgAgIQPcG1wRBPm4LGPL4dUUw4LGsBTRxve3fWH'
logo += 'A1lYUQIdGBCBwk9MALBEJpgME082uNjyizRiwDMGgD3UY5MDCLDSCh2tEIGBCD+xAUAoIBDSjRSg'
logo += 'KP9TxiGelNHAFDKgUBMAZgDgRSPo0SGsVj/kIcMeuqBTAz2H0APLBNHYMAWhfOhgwU/QQKCFFvGQ'
logo += 'Y4IJSuCkD4AbrJFPGVKo8QksAaABgAgI6KADDUVQAkE7WpxwbhfwAADGoiqRYEwa9uDBCzcz1JJV'
logo += 'EfrI4IYLlMDTThejzCNHBHiQgwQAH8igDw0SLfKPJf6EwwgAcEjgqQ+AUAIDvkLIoYgokNgRAFRS'
logo += '+rABGylwMMI9UTCyQRG5UBZSHHeQE88oojwjYjl44LNBTTJgGFIf/izRjwIAQAEIIG5FMwMweHiQ'
logo += 'wzqK8HDMHZo0SoYPfNAQBF5IoNGPBQ7Uw2QCG3D/sYgpLzxgzSfBnGLJbpUU0Z9NbORBBVsA+CBD'
logo += 'FvV8UAQS/MzwgDCqCPPCG0mYIs010EjgQgFanRFGHooBIoGMWWTxh6+NTPAABDtcs8Y026iiRQba'
logo += 'JOACZaqJJEHrMiKQRajkiOHJK9fkzkAZKjBATfAJoF6EGygYr9jrk/eyAg7kNNJEBcIwIEYhHrgz'
logo += '2mJW5XTRRYol4BMAWTjwxypt6MKCHM4QAjKO4YFv3AAAi7nKBvrAwMYA4HhaEYqMRmKAFngAEn7I'
logo += 'xByuIIkNgMF+KvlICg7CtbbgpDQ/cIAbQniCJBjBCMhIRApIoDgZ5IEgjQnCFt5iwpBARQkSuAoJ'
logo += 'OBQwiTUswhsGgMrrzmABibDOBezYQhiYkAAmIGFnSHCD1xLgBO+MhAQkQIIIAPEBfRiHDz84XUAA'
logo += 'ADs='


ICONFILE = None

def constructor(master):
    global ICONFILE
    
    ICONFILE = tempfile.NamedTemporaryFile(mode='w+b', delete=False) # Temporary file for the icon.
    try:
        ICONFILE.write(base64.b64decode(logo)) # Write icon bytes by decoding base64.
    finally:
        ICONFILE.close()
    if os.path.isfile(ICONFILE.name):
        icon = PhotoImage(file=ICONFILE.name) # Now select our temporary file as application icon.
        master.tk.call("wm", "iconphoto", master, "-default", icon)


def destructor():
    global ICONFILE

    if ICONFILE: # Temporary icon file can be removed.
        try:
            os.unlink(ICONFILE.name)
            ICONFILE = None
        except:
            pass

