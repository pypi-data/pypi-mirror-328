import os
import sys
import ctypes
import importlib.util

# Get the package directory
package_dir = os.path.dirname(__file__)
lib_path = os.path.join(package_dir, "lib")

# Ensure shared libraries (`lib/*.so`) are found
os.environ["LD_LIBRARY_PATH"] = lib_path + ":" + os.environ.get("LD_LIBRARY_PATH", "")

os.environ["OPAL_PREFIX"] = package_dir

# Load HDF5-related libraries first
#hdf5_libs = ["libhdf5.so", "libhdf5_hl.so", "libhdf5_cpp.so", "libhdf5_tools.so"]
#for hdf5_lib in hdf5_libs:
#    hdf5_path = os.path.join(lib_path, hdf5_lib)
#    if os.path.exists(hdf5_path):
#        ctypes.CDLL(hdf5_path, mode=ctypes.RTLD_GLOBAL)

# Preload all shared libraries
for so_file in sorted(os.listdir(lib_path)):
    if so_file.endswith(".so") or ".so." in so_file:
        so_path = os.path.join(lib_path, so_file)
        try:
            ctypes.CDLL(so_path, mode=ctypes.RTLD_GLOBAL)
        except OSError as e:
            print(f"Warning: Could not load {so_path}: {e}")

# Explicitly load mufem.so
mufem_so_path = os.path.join(package_dir, "mufem.so")
if not os.path.exists(mufem_so_path):
    raise ImportError(f"Could not find {mufem_so_path}")

spec = importlib.util.spec_from_file_location("mufem", mufem_so_path)
mufem = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mufem)

# Expose mufem to package users
sys.modules["mufem"] = mufem

