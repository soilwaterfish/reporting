#' Run BMP Report
#'
#' @param fiscal_year A named list with fiscal_year, ex. list(fiscal_year = '2023').
#' @param output_file A file path to download file.
#' @return A rendered HTML report
#' @export
#'
get_nps_report <- function(fiscal_year, output_dir = r'{T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\documents\}'){

  rmarkdown::render(system.file('app/www', 'nps_accomplishment_reporting.Rmd', package = 'reporting'),
                    params = fiscal_year,
                    output_file = paste0('nps_accomplishment_reporting_FY', fiscal_year),
                    output_dir = output_dir,
                    output_format = rmarkdown::word_document(reference_docx = system.file('app/www', 'word_template.docx', package = 'reporting')))


}

