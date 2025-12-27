import cv2
import numpy as np
import time

def measure_from_stream(url, pixels_per_mm=10):
    """
    Connects to an old phone's IP Camera stream and measures grass width.
    url example: "http://192.168.1.100:8080/video"
    """
    print(f"Connecting to {url}...")
    cap = cv2.VideoCapture(url)
    
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 1. Pre-process
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # 2. Edge Detection
        edged = cv2.Canny(blurred, 50, 150)
        
        # 3. Find Largest Contour (The Grass Strand)
        contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            # Find the largest contour by area
            c = max(contours, key=cv2.contourArea)
            
            if cv2.contourArea(c) > 500:
                rect = cv2.minAreaRect(c)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                
                # Draw for visual confirmation
                cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)
                
                # Calculate width
                (x, y), (w, h), angle = rect
                width_mm = min(w, h) / pixels_per_mm
                
                cv2.putText(frame, f"Width: {width_mm:.2f}mm", (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the frame
        cv2.imshow("Sweetgrass Vision Node", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # To test, install "IP Webcam" on an old Android phone
    # and replace the URL below with the one shown in the app.
    # measure_from_stream("http://192.168.1.XX:8080/video")
    print("Vision script ready. Set your phone IP and run.")
