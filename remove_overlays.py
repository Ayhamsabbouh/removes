import cv2
import numpy as np

def remove_overlays(image_path, output_path):
    # Bild laden
    image = cv2.imread(image_path)
    
    # In Graustufen konvertieren
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Schwellenwert anwenden, um binäres Bild zu erhalten
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    
    # Invertieren des binären Bildes
    thresh = cv2.bitwise_not(thresh)
    
    # Konturen finden
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Maske erstellen
    mask = np.ones(image.shape, dtype=np.uint8) * 255
    
    # Konturen auf die Maske zeichnen
    cv2.drawContours(mask, contours, -1, (0, 0, 0), -1)
    
    # Maske auf das Originalbild anwenden
    result = cv2.bitwise_and(image, mask)
    
    # Ergebnis speichern
    cv2.imwrite(output_path, result)

# Beispielverwendung
remove_overlays('input_image.jpg', 'output_image.jpg')
