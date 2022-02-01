#CКРИПТ ДЛЯ ДАТАСЕТ

import arcpy

#выбрать рабочее пространство 
workspace = arcpy.GetParameterAsText(0)
#задаем рабочее пространство 
arcpy.env.workspace = workspace

#папка для сохранения бд
out_folder_path=arcpy.GetParameterAsText(1)
#название 
out_name = arcpy.GetParameterAsText(2)
#создаем основную бд
arcpy.CreateFileGDB_management(out_folder_path, out_name)

#создаем временную бд для хранения конвертированных объектов 
arcpy.env.scratchGDB(out_folder_path)
scratchGDB = arcpy.env.scratchGDB(out_folder_path)

#Имя выходного класса пространственных объектов
name = arcpy.GetParameterAsText(3)

#класс объектов который будет конвертирован 
fileExt = r".shp"
inFeatures = [_ for _ in os.listdir(workspace) if _.endswith(fileExt)]

#конвертируем 
for list2 in inFeatures:
    arcpy.conversion.FeatureClassToFeatureClass (list2,scratchGDB,name)

#Имя выходного dataset
dataset = arcpy.GetParameterAsText(4)

#созадем dataset
arcpy.management.CreateFeatureDataset(name,out_name,dataset)
