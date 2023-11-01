import arcpy
import pandas as pd
from arcgis.features import GeoAccessor, GeoSeriesAccessor

def get_gpas(fiscal_year = "'2022'"):

    # Use the as_myself SDE connection file on the T:
    arcpy.env.workspace = r"T:\FS\Reference\GeoTool\agency\DatabaseConnection\edw_sde_default_as_myself.sde"
    
    # Specify the name of feature class after you find it from the .lyr file
    fc = "S_USA.Accomplishment_gPAS_PL"
    fc_line = "S_USA.Accomplishment_gPAS_LN"
    
    where = ("FISCAL_YEAR = " + fiscal_year + " And ADMIN_ORG_CODE IN ('0102','0103', '0110', '0111', '0114', '0115', '0116')")

    # filter fc by where clause

    arcpy.MakeFeatureLayer_management(fc, out_layer='gPAS_PL_Filtered', workspace=r"T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\reporting.gdb", where_clause = where)
    arcpy.MakeFeatureLayer_management(fc_line, out_layer='gPAS_LN_Filtered', workspace=r"T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\reporting.gdb", where_clause = where)

    # write filtered fc to .gdb

    arcpy.CopyFeatures_management('gPAS_PL_Filtered', r"T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\reporting.gdb\gPAS_PL_Filtered_MT_" + fiscal_year.replace("'", ""))
    arcpy.CopyFeatures_management('gPAS_LN_Filtered', r"T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\reporting.gdb\gPAS_LN_Filtered_MT_" + fiscal_year.replace("'", ""))



    
