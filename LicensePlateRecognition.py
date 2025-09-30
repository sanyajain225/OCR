import cv2
import easyocr
import matplotlib.pyplot as plt

# Load the image1
image_path = 'car1.jpg'  # replace with your image file
image = cv2.imread(image_path)

# Optional: Resize for consistency
image = cv2.resize(image, (600, 400))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load OCR Reader
reader = easyocr.Reader(['en'])  # English language

# Detect text from image
results = reader.readtext(gray)

# Draw bounding boxes and print text
for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))

    # Draw rectangle and text
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(image, text, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    print(f"Detected Text: {text} (Confidence: {prob:.2f})")

# Display the image using OpenCV
cv2.imshow("Detected Number Plate", image)
cv2.waitKey(0)
cv2.destroyAllWindows()