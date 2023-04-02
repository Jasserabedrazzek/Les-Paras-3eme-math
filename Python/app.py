import streamlit as st
import datetime
import time
import calendar
#---------------------set page------------------------------
st.set_page_config(page_title="3eme Math 2023",page_icon=":ledger:",layout="wide")
#-------------------Title-----------------------------------
st.title('Les Parascolaires 3eme Math 2023 :books:')

# -----------------------Path-------------------------------
path1 = r"E:\Scripts\Python\Atomix_chimie_3eme_math.pdf"
path2 = r"E:\Scripts\Python\Atomix_physique_3eme_math.pdf"
path3 = r"E:\Scripts\Python\Collection_methodes_Chimie_3eme_secondaire_ocr.pdf"
path4 = r"E:\Scripts\Python\Cahiers_des_Mathematiques_Analyse_3eme_sec_Section_Math_ocr.pdf"
path5 = r"E:\Scripts\Python\Cahiers_des_Mathematiques_Proba_Geo_3eme_sec_Section_Math_ocr.pdf"
path6 = r"E:\Scripts\Python\Collection_bios_sv3_3eme_math_ocr.pdf"
path7 = r"E:\Scripts\Python\falsafa 3eme.pdf"
path8 = r"E:\Scripts\Python\Manuel_scolaire_3_math_section_math_t2.pdf"
path9 = r"E:\Scripts\Python\xy_plus_3_mathematiques_section_3em_math_tome1.pdf"
path10 = r"E:\Scripts\Python\xy_plus_3_mathematiques_section_3em_math_tome2.pdf"

#------------------------------read file------------------------
with open(path1, 'rb') as f:
    file_data1 = f.read()
with open(path2, 'rb') as f:
    file_data2 = f.read()
with open(path3, 'rb') as f:
    file_data3 = f.read()
with open(path4, 'rb') as f:
    file_data4 = f.read()
with open(path5, 'rb') as f:
    file_data5 = f.read()
with open(path6, 'rb') as f:
    file_data6 = f.read()
with open(path7, 'rb') as f:
    file_data7 = f.read()
with open(path8, 'rb') as f:
    file_data8 = f.read()
with open(path9, 'rb') as f:
    file_data9 = f.read()
with open(path10, 'rb') as f:
    file_data10 = f.read()

#------------Physique---------
st.write("-----")
st.title("Physique :magnet:")
#-----------columns-----------
col1,col2,col3 = st.columns(3)
#-----------cols-----------
with col1:
    st.write("Atomix_chimie_3eme_math:test_tube:")
# Create a download button for the binary data
    st.download_button(
        label='Download',
        data=file_data1,
        file_name='Atomix_chimie_3eme__ math.pdf',
        mime='application/pdf'
    )
with col2:
    st.write("Atomix_physique_3eme_math")
    st.download_button(
        label='Download',
        data=file_data2,
        file_name='Atomix_physique_3eme_math.pdf',
        mime='application/pdf'
    )
with col3:
    st.write("Collection_methodes_Chimie_3eme_secondaire_ocr")
    st.download_button(
        label='Download',
        data=file_data3,
        file_name='Collection_methodes_Chimie_3eme_secondaire_ocr.pdf',
        mime='application/pdf'
        )
st.write('---')
st.title("Mathematique :orange_book:")
col4,col5,col6,col7,col8= st.columns(5)
with col4:
    st.write("Cahiers_des_Mathematiques_Analyse_3eme_sec_Section_Math_ocr")
    st.download_button(
        label='Download',
        data=file_data4,
        file_name='Cahiers_des_Mathematiques_Analyse_3eme_sec_Section_Math_ocr.pdf',
        mime='application/pdf'
        )
with col5:
    st.write("Cahiers_des_Mathematiques_Proba_Geo_3eme_sec_Section_Math_ocr")
    st.download_button(
        label='Download',
        data=file_data5,
        file_name='Cahiers_des_Mathematiques_Proba_Geo_3eme_sec_Section_Math_ocr.pdf',
        mime='application/pdf'
        )
with col6:
    st.write("Manuel_scolaire_3_math_section_math_t2")
    st.download_button(
        label='Download',
        data=file_data8,
        file_name='Manuel_scolaire_3_math_section_math_t2.pdf',
        mime='application/pdf'
        )
with col7:
    st.write("xy_plus_3_mathematiques_section_3em_math_tome1")
    st.download_button(
        label='Download',
        data=file_data9,
        file_name='xy_plus_3_mathematiques_section_3em_math_tome1.pdf',
        mime='application/pdf'
        )
with col8:
    st.write("xy_plus_3_mathematiques_section_3em_math_tome2")
    st.download_button(
        label='Download',
        data=file_data10,
        file_name='xy_plus_3_mathematiques_section_3em_math_tome2.pdf',
        mime='application/pdf'
        )
st.write('---')
st.title("Science :dna:")
st.write("Collection_bios_sv3_3eme_math_ocr")
st.download_button(
    label='Download',
    data=file_data6,
    file_name='Collection_bios_sv3_3eme_math_ocr.pdf',
    mime='application/pdf'
)
st.write("---")
st.title("Philosohie :scroll:")
st.write("El Wajiz 3eme")
st.download_button(
    label='Download',
    data=file_data7,
    file_name='Philosophie.pdf',
    mime='application/pdf'
)
st.write("---")

col11,col12 = st.columns(2)
with col11:
    st.write("Crédits:","[Jasser ben abed razzek](https://www.facebook.com/jasser.razzek.3/)")
with col12:
    st.write("Copyright :copyright: 2023, Streamlit Inc")

current_time = st.empty()
current_time.text(datetime.datetime.now().strftime("%H:%M:%S"))

# Update the time every second
while True:
    current_time.text(datetime.datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)
