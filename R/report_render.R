#' Run BMP Report
#'
#' @param fiscal_year A quoted character.
#' @return A rendered HTML report
#' @export
#'
get_bmp_report <- function(fiscal_year = "'2022'"){

  get_gpas(fiscal_year = fiscal_year)

  rmarkdown::render(system.file('app/www', 'nps_accomplishment_reporting', package = 'reporting'),
                    output_format = rmarkdown::word_document(reference_docx = system.file('app/www', 'word_template', package = 'reporting')))

  file.copy(from = system.file('app/www', 'nps_accomplishment_reporting.docx', package = 'reporting'),
            to = r'{T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\documents}')

}
