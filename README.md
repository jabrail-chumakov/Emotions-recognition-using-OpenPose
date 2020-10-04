# Emotions-recognition-using-OpenPose
Below you can observe detailed desctiption of how to run script of emotions recognition by using OpenPose

## Instal OpenPose
First of all you need to install OpenPose itself. In order to do that, go to the official release page and download it [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases).

## Dowload OpenPose Tutorial folder
1. Download adove folder and place it inside the folder, where OpenPose installed.
1. To detect and extract keypoints from videos you can use `parse_videos.py` script. Move your videos to the `videos` folder and run this script. Data will be saved in the `output` folder in `json`.
1. In order to save all data into one `csv` file run the `to_format.py` script.
1. In order to run the OpenPose on a webcam you can use the `webcam.py` script. Extracted files will be saved in the `output` folder in `HH_MM_SS` named new folder.

## Run `<emotion.py>` script
In my case I used three emotion: happy, neutral and surprise. On the official website of [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md) you can obserb location of keypoints. By importing your `<csv>` file to Python, Excel or online csv reader, you can observe `<x>` and `<y>` values. Thus, by comparing them you will achieve desired results. 

 ```javascript
It should be noted, that in case if emotion not in the list it should throw garbage. 
Also, you can modify `pos[]` for your emotion. 
```

## Good Luck!
