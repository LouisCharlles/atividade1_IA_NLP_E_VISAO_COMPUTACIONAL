import cv2
import matplotlib.pyplot as plt
import os


nome_da_imagem = 'imagem.png' 

if not os.path.exists(nome_da_imagem):
    print(f"❌ ERRO: O arquivo '{nome_da_imagem}' não foi encontrado!")
    exit()


img = cv2.imread(nome_da_imagem) 
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)


_, mascara = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


img_resultado = img_rgb.copy()

for contorno in contornos:
    area = cv2.contourArea(contorno)
    
   
    if area > 5000: 
        x, y, w, h = cv2.boundingRect(contorno)
        
        if w > h * 2: 
            cv2.rectangle(img_resultado, (x, y), (x+w, y+h), (0, 255, 0), 4)
            cv2.putText(img_resultado, 'Espada Identificada', (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        else:
            cv2.rectangle(img_resultado, (x, y), (x+w, y+h), (0, 0, 255), 4)
            cv2.putText(img_resultado, 'Machado', (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("1. Original")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("2. Segmentação (Otsu)")
plt.imshow(mascara, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("3. Detecção de Objetos")
plt.imshow(img_resultado)
plt.axis('off')

plt.savefig('resultado_segmentacao.png', bbox_inches='tight')
print("✅ Segmentação concluída! Abra o arquivo 'resultado_segmentacao.png'.")