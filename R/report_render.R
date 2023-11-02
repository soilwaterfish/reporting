#' Run BMP Report
#'
#' @param fiscal_year A character for fiscal year of report.
#' @return A rendered HTML report
#' @export
#'
get_bmp_report <- function(fiscal_year){

  rmarkdown::render(system.file('app/www', 'nps_accomplishment_reporting.Rmd', package = 'reporting'),
                    params = fiscal_year,
                    output_format = rmarkdown::word_document(reference_docx = system.file('app/www', 'word_template', package = 'reporting')))

  file.copy(from = system.file('app/www', 'nps_accomplishment_reporting.docx', package = 'reporting'),
            to = r'{T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\documents}')

}

