#C����� ��� �������

import arcpy

#������� ������� ������������ 
workspace = arcpy.GetParameterAsText(0)
#������ ������� ������������ 
arcpy.env.workspace = workspace

#����� ��� ���������� ��
out_folder_path=arcpy.GetParameterAsText(1)
#�������� 
out_name = arcpy.GetParameterAsText(2)
#������� �������� ��
arcpy.CreateFileGDB_management(out_folder_path, out_name)

#������� ��������� �� ��� �������� ���������������� �������� 
arcpy.env.scratchGDB(out_folder_path)
scratchGDB = arcpy.env.scratchGDB(out_folder_path)

#��� ��������� ������ ���������������� ��������
name = arcpy.GetParameterAsText(3)

#����� �������� ������� ����� ������������� 
fileExt = r".shp"
inFeatures = [_ for _ in os.listdir(workspace) if _.endswith(fileExt)]

#������������ 
for list2 in inFeatures:
    arcpy.conversion.FeatureClassToFeatureClass (list2,scratchGDB,name)

#��� ��������� dataset
dataset = arcpy.GetParameterAsText(4)

#������� dataset
arcpy.management.CreateFeatureDataset(name,out_name,dataset)
