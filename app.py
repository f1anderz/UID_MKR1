import streamlit as st
from PIL import Image, ImageEnhance
from io import BytesIO

def main():
    st.title("Image Upload and Filter App")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is None:
        return
        
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
        
    # Filter options
    st.subheader("Adjust Image")
    contrast = st.slider("Contrast", 0.5, 2.0, 1.0)
    brightness = st.slider("Brightness", 0.5, 2.0, 1.0)
    grayscale = st.checkbox("Grayscale")
        
    # Apply filters
    enhancer_contrast = ImageEnhance.Contrast(image)
    image_filtered = enhancer_contrast.enhance(contrast)
        
    enhancer_brightness = ImageEnhance.Brightness(image_filtered)
    image_filtered = enhancer_brightness.enhance(brightness)
        
    if grayscale:
        image_filtered = image_filtered.convert("L")
        
    # Display filtered image
    st.image(image_filtered, caption="Filtered Image", use_container_width=True)
        
    # Зберігаємо відфільтроване зображення в пам'яті
    img_bytes = BytesIO()
    image_filtered.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    st.download_button(
        label="Download Image",
        data=img_bytes,
        file_name="filtered_image.png",
        mime="image/png"
    )

if __name__ == "__main__":
    main()