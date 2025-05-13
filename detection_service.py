import cv2
import numpy as np
from datetime import datetime
from detection import AccidentDetectionModel

# Load YOLO
net = cv2.dnn.readNet("./Yolo_Folder/yolov3.weights", "./Yolo_Folder/yolov3.cfg")
classes = []
with open("./Yolo_Folder/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers_indices = net.getUnconnectedOutLayers()
output_layers_indices = [tuple([i]) for i in output_layers_indices]  
output_layers = [layer_names[i[0] - 1] for i in output_layers_indices]

# Accident detection model
model = AccidentDetectionModel("./model/model.json", './model/model_weights.h5')

font = cv2.FONT_HERSHEY_DUPLEX

def startapplication(video_path):
    video = cv2.VideoCapture(video_path)
    
    while True:
        ret, frame = video.read()
        if not ret:
            print("Frame read failed. Video might have ended.")
            break

        # YOLO object detection
        height, width, channels = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)  

        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 and class_id in [2, 5, 7, 3]:  # Car, bus, truck, bike
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)


                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    roi = cv2.resize(gray_frame, (250, 250))
                    pred, prob = model.predict_accident(roi[np.newaxis, :, :])

                    if pred == "Accident" and confidence > 0.5 and class_id in [2, 5, 7, 3]:
                        prob = round(prob[0][0] * 100, 2)
                        if prob >= 90:
                            # Display red rectangle
                            cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 5)
                            cv2.putText(frame, f"Warning {pred} {prob}%", (180, 300), font, 1, (0, 0, 255), 1)
                            
                            # Save screenshot with date and time
                            current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
                            screenshot_filename = f"./Accidents_Screen/screenshot_{current_datetime}.png"
                            cv2.imwrite(screenshot_filename, frame)
                

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                class_id = class_ids[i]
                label = classes[class_id]
                color = (0, 255, 0)  # Default color for cars
                if class_id == 5:  # Change color for bus
                    color = (0, 0, 255)
                elif class_id == 7:  # Change color for truck
                    color = (255, 0, 0)
                elif class_id == 3:  # Change color for bike
                    color = (255, 255, 0)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y - 10), font, 0.5, color, 1)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])

        if pred == "Accident" and confidence > 0.5 and class_id in [2, 5, 7, 3]:
            prob = round(prob[0][0] * 100, 2)
            if prob >= 70:
                # Display red rectangle
                cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 5)
                cv2.putText(frame, f"Warning {pred} {prob}%", (180, 300), font, 1, (0, 0, 255), 1)
                
                # Save screenshot with date and time
                current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
                screenshot_filename = f"./Accidents_Screen/screenshot_{current_datetime}.png"
                cv2.imwrite(screenshot_filename, frame)
        cv2.imshow('Video', frame)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()