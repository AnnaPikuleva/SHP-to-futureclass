import arcpy
#выбрать рабочее пространство 
workspace = arcpy.GetParameterAsText(0)
#задаем рабочее пространство 
arcpy.env.workspace = workspace

#класс объектов который будет конвертирован 
inFeatures = arcpy.ListDatasets()
#папка для сохранения бд
out_folder_path=arcpy.GetParameterAsText(1)
#название бд  
out_name = arcpy.GetParameterAsText(2)
#создаем бд
arcpy.CreateFileGDB_management(out_folder_path,out_name)

#Имя выходного класса пространственных объектов.
name = arcpy.GetParameterAsText(3)
for list2 in inFeatures:
    arcpy.conversion.FeatureClassToFeatureClass(list2,out_name,name)


