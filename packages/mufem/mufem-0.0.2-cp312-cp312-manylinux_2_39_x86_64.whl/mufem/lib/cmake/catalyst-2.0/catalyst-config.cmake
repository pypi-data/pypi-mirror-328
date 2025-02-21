# Catalyst Package config file.

if (CMAKE_VERSION VERSION_LESS "3.12")
  set("${CMAKE_FIND_PACKAGE_NAME}_FOUND" 0)
  set("${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE"
    "Catalyst requires CMake 3.12 in order to reliably be used.")
  return ()
endif ()

cmake_policy(PUSH)
cmake_policy(VERSION 3.12)

set(CATALYST_VERSION "2.0")
set(CATALYST_ABI_VERSION "2")
set(CATALYST_BUILD_SHARED_LIBS "ON")
set(CATALYST_USE_MPI "ON")
set(CATALYST_PYTHONPATH "${CMAKE_CURRENT_LIST_DIR}/../../../")
set(CATALYST_USE_PYTHON "OFF")

if (CATALYST_USE_MPI)
  include(CMakeFindDependencyMacro)
  find_dependency(MPI COMPONENTS C)
endif ()

if (CATALYST_USE_PYTHON)
  find_package(Python3 COMPONENTS Development REQUIRED)
endif()


####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was catalyst-config.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

macro(check_required_components _NAME)
  foreach(comp ${${_NAME}_FIND_COMPONENTS})
    if(NOT ${_NAME}_${comp}_FOUND)
      if(${_NAME}_FIND_REQUIRED_${comp})
        set(${_NAME}_FOUND FALSE)
      endif()
    endif()
  endforeach()
endmacro()

####################################################################################

include("${CMAKE_CURRENT_LIST_DIR}/catalyst-conduit-targets.cmake" OPTIONAL)
include("${CMAKE_CURRENT_LIST_DIR}/catalyst-targets.cmake")

if ("SDK" IN_LIST "${CMAKE_FIND_PACKAGE_NAME}_FIND_COMPONENTS")
  # if SDK was explicitly requested, include the macros.
  include("${CMAKE_CURRENT_LIST_DIR}/catalyst-macros.cmake" OPTIONAL
    RESULT_VARIABLE ${CMAKE_FIND_PACKAGE_NAME}_SDK_FOUND)
endif()

check_required_components(catalyst)
cmake_policy(POP)
