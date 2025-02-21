#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "conduit" for configuration ""
set_property(TARGET conduit APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(conduit PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libconduit.so"
  IMPORTED_SONAME_NOCONFIG "libconduit.so"
  )

list(APPEND _cmake_import_check_targets conduit )
list(APPEND _cmake_import_check_files_for_conduit "${_IMPORT_PREFIX}/lib/libconduit.so" )

# Import target "conduit_relay" for configuration ""
set_property(TARGET conduit_relay APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(conduit_relay PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libconduit_relay.so"
  IMPORTED_SONAME_NOCONFIG "libconduit_relay.so"
  )

list(APPEND _cmake_import_check_targets conduit_relay )
list(APPEND _cmake_import_check_files_for_conduit_relay "${_IMPORT_PREFIX}/lib/libconduit_relay.so" )

# Import target "conduit_relay_mpi" for configuration ""
set_property(TARGET conduit_relay_mpi APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(conduit_relay_mpi PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libconduit_relay_mpi.so"
  IMPORTED_SONAME_NOCONFIG "libconduit_relay_mpi.so"
  )

list(APPEND _cmake_import_check_targets conduit_relay_mpi )
list(APPEND _cmake_import_check_files_for_conduit_relay_mpi "${_IMPORT_PREFIX}/lib/libconduit_relay_mpi.so" )

# Import target "conduit_relay_mpi_io" for configuration ""
set_property(TARGET conduit_relay_mpi_io APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(conduit_relay_mpi_io PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libconduit_relay_mpi_io.so"
  IMPORTED_SONAME_NOCONFIG "libconduit_relay_mpi_io.so"
  )

list(APPEND _cmake_import_check_targets conduit_relay_mpi_io )
list(APPEND _cmake_import_check_files_for_conduit_relay_mpi_io "${_IMPORT_PREFIX}/lib/libconduit_relay_mpi_io.so" )

# Import target "conduit_blueprint" for configuration ""
set_property(TARGET conduit_blueprint APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(conduit_blueprint PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libconduit_blueprint.so"
  IMPORTED_SONAME_NOCONFIG "libconduit_blueprint.so"
  )

list(APPEND _cmake_import_check_targets conduit_blueprint )
list(APPEND _cmake_import_check_files_for_conduit_blueprint "${_IMPORT_PREFIX}/lib/libconduit_blueprint.so" )

# Import target "conduit_blueprint_mpi" for configuration ""
set_property(TARGET conduit_blueprint_mpi APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(conduit_blueprint_mpi PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libconduit_blueprint_mpi.so"
  IMPORTED_SONAME_NOCONFIG "libconduit_blueprint_mpi.so"
  )

list(APPEND _cmake_import_check_targets conduit_blueprint_mpi )
list(APPEND _cmake_import_check_files_for_conduit_blueprint_mpi "${_IMPORT_PREFIX}/lib/libconduit_blueprint_mpi.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
