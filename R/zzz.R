# .onLoad <- function(libname, pkgname){
#
#   py_path <- r'{C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe}'
#
#   if(reticulate::py_exe() == py_path){stop('Need to have ....')}
#
#   reticulate::source_python(
#     system.file("gpas.py", package = "reporting"),
#     envir = pyfn_env
#   )
#
#
# }
