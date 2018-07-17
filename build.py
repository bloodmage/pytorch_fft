import os
import torch
from torch.utils.ffi import create_extension

this_file = os.path.dirname(__file__)

sources = []
headers = []
defines = []
with_cuda = False

if torch.cuda.is_available():
    print('Including CUDA code.')
    sources += ['pytorch_fft/src/th_fft_cuda.c', 'pytorch_fft/src/thc_state_init.cpp']
    headers += ['pytorch_fft/src/th_fft_cuda.h']
    defines += [('WITH_CUDA', None)]
    with_cuda = True

ffi = create_extension(
    'pytorch_fft._ext.th_fft',
    package=True,
    headers=headers,
    sources=sources,
    define_macros=defines,
    relative_to=__file__,
    with_cuda=with_cuda,
    include_dirs=[os.getcwd() + '/pytorch_fft/src', r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\include'],
    library_dirs=[r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64', r'C:\Anaconda\envs\py3\Lib\site-packages\torch\lib', '.'], 
    libraries=['cufft', 'cudart', 'thc', 'aten'],
)

if __name__ == '__main__':
    ffi.build()
