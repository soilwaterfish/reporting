# .onLoad <- function(libname, pkgname){
#
#   if (!reticulate::py_module_available("arcpy")) {
#
#     message('Need to have arcpy within Python environment')
#
#   } else {
#
#   reticulate::source_python(
#     system.file("gpas.py", package = "reporting"),
#     envir = pyfn_env
#   )
#
#   }
#
# }

