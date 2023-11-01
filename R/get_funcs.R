#' Get GPAS Data
#'
#' @param fiscal_year A quoted character.
#'
#' @return Nothing. Writes to a file gdb.
#' @export
#'
get_gpas <- function(fiscal_year){

reticulate::use_python(r'{C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe}')

pyfn_env$get_gpas(fiscal_year = fiscal_year)


}
