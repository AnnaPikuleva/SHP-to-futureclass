import arcpy
#������� ������� ������������ 
workspace = arcpy.GetParameterAsText(0)
#������ ������� ������������ 
arcpy.env.workspace = workspace

#����� �������� ������� ����� ������������� 
inFeatures = arcpy.ListDatasets()
#����� ��� ���������� ��
out_folder_path=arcpy.GetParameterAsText(1)
#�������� ��  
out_name = arcpy.GetParameterAsText(2)
#������� ��
arcpy.CreateFileGDB_management(out_folder_path,out_name)

#��� ��������� ������ ���������������� ��������.
name = arcpy.GetParameterAsText(3)
for list2 in inFeatures:
    arcpy.conversion.FeatureClassToFeatureClass(list2,out_name,name)


