import arcpy

def get_gpas(fiscal_year = "'2023'"):

    # Use the as_myself SDE connection file on the T:
    arcpy.env.workspace = r"T:\FS\Reference\GeoTool\agency\DatabaseConnection\edw_sde_default_as_myself.sde"
    
    # Specify the name of feature class after you find it from the .lyr file
    # Specify the name of feature class after you find it from the .lyr file
    fc = "S_USA.Accomplishment_gPAS_PL"
    fc_line = "S_USA.Accomplishment_gPAS_LN"
    where_poly = ("FISCAL_YEAR = " + fiscal_year + " And ADMIN_ORG_CODE IN ('0102','0103', '0110', '0111', '0114', '0115', '0116') And SPATIAL_SIZE >= 0.0 AND ACTIVITY_CODE IN ('Abandoned Mine Reclamation','AOP Barrier Construction','AOP Barrier Removed-Non-Road','AOP Barrier Removed-Road','AOP Eliminate Fish Entrainment','AOP Fish Passage Structure','AOP Improvement','AOP Improvement-Road','AOP Removed','Beaver Dam Analog','Channel Reconstruction','Crossing Improvement-Fish','Crossing Improvement-NonFish','Crossing Removal','Dam Removal','Decommission','Decommission-Treatment Scale 0','Decommission-Treatment Scale 1','Decommission-Treatment Scale 2','Decommission-Treatment Scale 3','Decommission-Treatment Scale 4','Decommission-Treatment Scale 5','Diversion Improvement','Eliminate Stream Diversion','ERFO Road Repair','Erosion Control','Erosion Control-Riparian','Fencing-Riparian','Fish Passage Structure','Fish Passage-Stream Chnl Mod','Fish Population Suppression','Fish Population Supression','Floodplain Reconstruction','Increase Large Wood','Instream Flow Secured','InvasiveSpeciesMgmt-AqNonPlant','InvasiveSpeciesMgmt-AqPlant','InvasiveSpeciesMgmt-Riparian','Lake Habitat Improvement','Lakeshore Habitat Improvement','Lakeshore Stabilization','Mine Reclamation','Mine Reclamation-Abandoned','Open side-channel Habitat','Planting-Riparian','Riparian Native Plant Restore','Road Closure','Road Maintenance','Road Realignment','Road Repair','Road Stormproofing','Road-To-Trail-Foot','Road-To-Trail-Two-Wheel','Seeding-Riparian','Spring Improvement','Spring Protection','Streambank Stabilization','Trail Decommission','Trail Realignment','Trail Stormproofing','Wetland Protection','Wetland Restoration')")
    where_line = ("FISCAL_YEAR = " + fiscal_year + " And ADMIN_ORG_CODE IN ('0102','0103', '0110', '0111', '0114', '0115', '0116') And SPATIAL_SIZE >= 0.0 AND ACTIVITY_CODE IN ('AOP Barrier Construction','AOP Barrier Removed-Non-Road','AOP Barrier Removed-Road','AOP Eliminate Fish Entrainment','AOP Fish Passage Structure','AOP Improvement','AOP Improvement-Road','AOP Removed','Channel Reconstruction','Crossing Improvement-Fish','Crossing Improvement-NonFish','Crossing Removal','Decommission','Decommission-Treatment Scale 0','Decommission-Treatment Scale 1','Decommission-Treatment Scale 2','Decommission-Treatment Scale 3','Decommission-Treatment Scale 4','Decommission-Treatment Scale 5','Eliminate Stream Diversion','Erosion Control-Riparian','Fencing-Riparian','Fish Passage Structure','Fish Passage-Stream Chnl Mod','Increase Large Wood','Install Water Control Device','Instream Flow Secured','InvasiveSpeciesMgmt-Riparian','Open side-channel Habitat','Planting-Riparian','Prescribed Fire-Riparian','Riparian Native Plant Restore','Road Closure','Road Maintenance','Road Realignment','Road Repair','Road Stormproofing','Road-To-Trail-Foot','Seeding-Riparian','Storage-Level 1','Storage-Level 2','Storage-Level 3','Streambank Stabilization','Structure Addition-Habitat','Structure Addition-Spawning','Structure Maintenance-Aquatic','Trail Decommission','Water Quality Improvement','Wetland Protection','Wetland Restoration')")
    
    # remove a layer if it already exists

    if arcpy.Exists('gPAS_PL_Filtered'):
        arcpy.Delete_management('gPAS_PL_Filtered')

    if arcpy.Exists('gPAS_LN_Filtered'):
        arcpy.Delete_management('gPAS_LN_Filtered')
    
    # remove existing fc from .gdb
  
    arcpy.Delete_management(r"T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\reporting.gdb\gPAS_PL_Filtered_MT_" + fiscal_year.replace("'", ""), "")
    arcpy.Delete_management(r"T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\reporting.gdb\gPAS_LN_Filtered_MT_" + fiscal_year.replace("'", ""), "")

    # filter fc by where clause

    arcpy.MakeFeatureLayer_management(fc, out_layer='gPAS_PL_Filtered', workspace=r"T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\reporting.gdb", where_clause = where_poly)
    arcpy.MakeFeatureLayer_management(fc_line, out_layer='gPAS_LN_Filtered', workspace=r"T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\reporting.gdb", where_clause = where_line)

    # write filtered fc to .gdb

    arcpy.CopyFeatures_management('gPAS_PL_Filtered', r"T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\reporting.gdb\gPAS_PL_Filtered_MT_" + fiscal_year.replace("'", ""))
    arcpy.CopyFeatures_management('gPAS_LN_Filtered', r"T:\FS\NFS\R01\Program\2500WatershedAirMgmt\GIS\WorkSpace\jerickson\Spatial\reports\reporting.gdb\gPAS_LN_Filtered_MT_" + fiscal_year.replace("'", ""))


get_gpas(fiscal_year = "'2022'")
