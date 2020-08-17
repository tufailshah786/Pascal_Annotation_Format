# Pascal_Annotation_Format

Creating Pascal Voc Format with the help of annotation file that contain the points (cx,cy,w,h,angle)

First of all you need the latest version of python installed in your pc

step 1: Download the zip file and extract the file in C:/ folder after extraction you will get this folder"Pascal_Annotation_Format-master"

step 2: Open the folder "Pascal_Annotation_Format-master\Pascal_Format" and create folders name as it is "results" and store the annotations in "results" folder (its only for the rotated bounding box, xml file that contains the point cx,cy,w,h,angle)

step 3: Open the command prompt and then go to the extract folder "C:\Pascal_Annotation_Format-master\Pascal_Format" by writing 
this command "cd C:\Pascal_Annotation_Format-master\Pascal_Format"

step 4: write command "python allangle.py" and you will get pascal voc annotation files in "results" folder 
