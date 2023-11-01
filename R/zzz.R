.onLoad <- function(libname, pkgname){
  reticulate::use_python(r'{C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe}')
  reticulate::source_python(
    system.file("gpas.py", package = "reporting"),
    envir = pyfn_env
  )
}
