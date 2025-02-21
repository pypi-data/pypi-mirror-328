#----------------------------------------------------------------
# Generated CMake target import file for configuration "Debug".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "catalyst::catalyst" for configuration "Debug"
set_property(TARGET catalyst::catalyst APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(catalyst::catalyst PROPERTIES
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/libcatalyst.so.3"
  IMPORTED_SONAME_DEBUG "libcatalyst.so.3"
  )

list(APPEND _cmake_import_check_targets catalyst::catalyst )
list(APPEND _cmake_import_check_files_for_catalyst::catalyst "${_IMPORT_PREFIX}/lib/libcatalyst.so.3" )

# Import target "catalyst::catalyst_stub" for configuration "Debug"
set_property(TARGET catalyst::catalyst_stub APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(catalyst::catalyst_stub PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_DEBUG ""
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/catalyst/libcatalyst-stub.so"
  IMPORTED_NO_SONAME_DEBUG "TRUE"
  )

list(APPEND _cmake_import_check_targets catalyst::catalyst_stub )
list(APPEND _cmake_import_check_files_for_catalyst::catalyst_stub "${_IMPORT_PREFIX}/lib/catalyst/libcatalyst-stub.so" )

# Import target "catalyst::catalyst_replay" for configuration "Debug"
set_property(TARGET catalyst::catalyst_replay APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(catalyst::catalyst_replay PROPERTIES
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/bin/catalyst_replay"
  )

list(APPEND _cmake_import_check_targets catalyst::catalyst_replay )
list(APPEND _cmake_import_check_files_for_catalyst::catalyst_replay "${_IMPORT_PREFIX}/bin/catalyst_replay" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
