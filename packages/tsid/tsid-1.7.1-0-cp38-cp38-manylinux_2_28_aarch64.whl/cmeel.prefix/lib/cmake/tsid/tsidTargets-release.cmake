#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "tsid::tsid" for configuration "Release"
set_property(TARGET tsid::tsid APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(tsid::tsid PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libtsid.so"
  IMPORTED_SONAME_RELEASE "libtsid.so"
  )

list(APPEND _cmake_import_check_targets tsid::tsid )
list(APPEND _cmake_import_check_files_for_tsid::tsid "${_IMPORT_PREFIX}/lib/libtsid.so" )

# Import target "tsid::tsid_pywrap" for configuration "Release"
set_property(TARGET tsid::tsid_pywrap APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(tsid::tsid_pywrap PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/python3.8/site-packages/tsid/tsid_pywrap.cpython-38-aarch64-linux-gnu.so"
  IMPORTED_SONAME_RELEASE "tsid_pywrap.cpython-38-aarch64-linux-gnu.so"
  )

list(APPEND _cmake_import_check_targets tsid::tsid_pywrap )
list(APPEND _cmake_import_check_files_for_tsid::tsid_pywrap "${_IMPORT_PREFIX}/lib/python3.8/site-packages/tsid/tsid_pywrap.cpython-38-aarch64-linux-gnu.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
