# yolo_auto


What is yolo_auto? <br>
<br>
A library that allows you to train custom yolv3 object detectors in one line!
<br>
How does yolo_auto work?<br>
<br>

Syntax = <br>

x = Yolov3Train(Path to Labels, Path To images,number of classes, classnames in an array, Path to Working Directory, Subdivisions=8,batches-16, Image size=608) 	<br>
x.train()<br><br>

Sample:

x = Yolov3Train("/Users/arjunpandey/Desktop/AI-Stuff/newlib/data/labels","/Users/arjunpandey/Desktop/AI-Stuff/newlib/data/images",classes,classnames,"/Users/arjunpandey/Desktop/AI-Stuff/newlib/") <br>
x.train()<br>
