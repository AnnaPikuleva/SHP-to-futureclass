import arcpy
#������� ������� ������������ 
workspace = arcpy.GetParameterAsText(0)
#������ ������� ������������ 
arcpy.env.workspace = workspace

#����� �������� ������� ����� ������������� 
fileExt = r".shp"
inFeatures = [_ for _ in os.listdir(workspace) if _.endswith(fileExt)]

#����� ��� ���������� ��
out_folder_path=arcpy.GetParameterAsText(1)
#�������� �� (��������������, � ������� ����� ������ �������� ����� ��������) 
out_name = arcpy.GetParameterAsText(2)
#������� ��
arcpy.CreateFileGDB_management(out_folder_path, out_name)

path = os.path.join(out_folder_path,out_name)

#��� ��������� ������ ���������������� ��������.
name = arcpy.GetParameterAsText(3)
for list2 in inFeatures:
    arcpy.conversion.FeatureClassToFeatureClass (list2,path,name)


