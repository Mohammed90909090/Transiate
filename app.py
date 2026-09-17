import streamlit as st
import PyPDF2
from deep_translator import GoogleTranslator

# إعداد واجهة البرنامج
st.set_page_config(page_title="المترجم القانوني", page_icon="⚖️")
st.title("⚖️ برنامج الترجمة القانونية")
st.write("ارفع المستند ليتم استخراج النص وترجمته مجاناً")

# زر رفع الملف
uploaded_file = st.file_uploader("اختر ملف PDF", type="pdf")

if uploaded_file is not None:
    if st.button("ترجم الآن"):
        st.info("جاري المعالجة...")
        
        # استخراج النص من الملف
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
                
        # الترجمة الفورية المجانية
        if text.strip():
            translator = GoogleTranslator(source='auto', target='ar')
            # تقسيم النص لتجنب قيود الترجمة المجانية
            chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
            translated_text = ""
            for chunk in chunks:
                translated_text += translator.translate(chunk) + " "
                
            st.success("تمت الترجمة بنجاح!")
            st.write("---")
            st.write(translated_text)
        else:
            st.error("لم يتم العثور على نص قابل للقراءة في الملف.")
