import streamlit as st
import math

st.set_page_config(
    page_title='LogPowerConverter', 
    page_icon="https://cdn-icons-png.flaticon.com/512/3295/3295480.png",
    layout="centered"
    )
    
st.title('LogPowerConverter')
st.write('')

clicked = False

global si
global bsi

si = ['nW','uW','mW','W','KW','MW','GW']
bsi = [10**(-9),10**(-6),10**(-3),1,10**(3),10**(6),10**(9)]

def dBm_to_dB(power_in):

    power_out = power_in - 30

    return power_out

def dB_to_dBm(power_in):

    power_out = power_in + 30

    return power_out

def dBm_to_watts(power_in,unity):

    power_out = (10**(power_in/10))/10**(3)

    power_out = power_out / bsi[si.index(unity)]

    return power_out

def dB_to_watts(power_in,unity):

    power_out = 10**(power_in/10)

    power_out = power_out / bsi[si.index(unity)]

    return power_out


def watts_to_db(power_in, unity):

    power_out = power_in * bsi[si.index(unity)]

    power_out = 10*math.log10(power_out)

    return power_out

def watts_to_dbm(power_in, unity):
    power_out = power_in * bsi[si.index(unity)]

    power_out = 10*math.log10(power_out/10**(-3))

    return power_out


tab1, tab2, tab3, tab4, tab5, tab6  = st.tabs(["Watts To dB", "Watts To dBm", "dB to Watts", "dBm to Watts", "dB to dBm", "dBm to db"])

def watts_to_db_builder():
    with st.container():
        col1,col2 = st.columns([1,1])
        with col1:
            st.header('Watts')
        with col2:
            st.header('Decibel')
    
    col1,col2,col3,col4 = st.columns([0.6,0.6,0.5,1.5])

    with col1:
        power_watts = st.text_input("Power (Watts)", key='wdb_i1', value = 0)
        try:
            power_watts = float(power_watts)
        except:
            power_watts = 0

    with col2:
        usi = st.selectbox("ISU", si, key='wdb_s1', index = 3)
    
    with col3:
        st.write('')
        st.write('')
        clicked = st.button("Convert", key='wdb_b1')
    with col4:
        if clicked:
            if power_watts <= 0:
                st.error("Power must be greater than 0")
            else:
                st.write('')
                result = watts_to_db(power_watts,usi)
                st.success(f'{result:.4f} dB')

def watts_to_dbm_builder():
    with st.container():
        col1,col2 = st.columns([1,1])
        with col1:
            st.header('Watts')
        with col2:
            st.header('Decibel Miliwatts')
    
    col1,col2,col3,col4 = st.columns([0.6,0.6,0.5,1.5])

    with col1:
        
        power_watts = st.text_input("Power (Watts)", key='wdb_i2', value = 0)
        try:
            power_watts = float(power_watts)
        except:
            power_watts = 0
    with col2:
        usi = st.selectbox("ISU", si, key='wdb_s2', index = 3)
    
    with col3:
        st.write('')
        st.write('')
        clicked = st.button("Convert", key='wdb_b2')
    with col4:
        if clicked:
            if clicked:
                if power_watts <= 0:
                    st.error("Power must be greater than 0")
                else:
                    st.write('')
                    result = watts_to_dbm(power_watts,usi)
                    st.success(f'{result:.4f} dBm')

def dB_to_watts_builder():
    with st.container():
        col1,col2 = st.columns([1,1])
        with col1:
            st.header('Decibel')
        with col2:
            st.header('Watts')
    
    col1,col2,col3,col4 = st.columns([0.6,0.8,1,0.5])

    with col1:
        
        power_db = st.text_input("Power (Decibel)", key='wdb_i3', value = 0)
        try:
            power_db = float(power_db)
        except:
            power_db = 0

    with col2:
        st.write('')
        st.write('')
        clicked = st.button("Convert", key='wdb_b3')
    with col4:
        usi = st.selectbox("ISU", si, key='wdb_s3', index = 3)
    
    with col3:
        if clicked:
            if clicked:
                st.write('')
                result = dB_to_watts(power_db,usi)
                st.success(f'{result:.4f} {usi}')

def dBm_to_watts_builder():
    with st.container():
        col1,col2 = st.columns([1,1])
        with col1:
            st.header('Decibel Miliwatts')
        with col2:
            st.header('Watts')
    
    col1,col2,col3,col4 = st.columns([0.6,0.8,1,0.5])

    with col1:
        
        power_dbm = st.text_input("Power (Decibel Miliw.)", key='wdb_i4', value = 0)
        try:
            power_dbm = float(power_dbm)
        except:
            power_dbm = 0

    with col2:
        st.write('')
        st.write('')
        clicked = st.button("Convert", key='wdb_b4')
    with col4:
        usi = st.selectbox("ISU", si, key='wdb_s4', index = 3)
    
    with col3:
        if clicked:
            if clicked:
                st.write('')
                result = dBm_to_watts(power_dbm,usi)
                st.success(f'{result:.4f} {usi}')

def dB_to_dBm_builder():
    with st.container():
        col1,col2 = st.columns([1,1])
        with col1:
            st.header('Decibel')
        with col2:
            st.header('Decibel Miliwatts')
    
    col1,col2,col3,col4 = st.columns([0.6,0.8,1,0.5])

    with col1:
        
        power_dB = st.text_input("Power (dB)", key='wdb_i5', value = 0)
        try:
            power_dB = float(power_dB)
        except:
            power_dB = 0

    with col2:
        st.write('')
        st.write('')
        clicked = st.button("Convert", key='wdb_b5')
    
    with col3:
        if clicked:
            if clicked:
                st.write('')
                result = dB_to_dBm(power_dB)
                st.success(f'{result:.4f} dBm')

def dBm_to_dB_builder():
    with st.container():
        col1,col2 = st.columns([1,1])
        with col1:
            st.header('Decibel Miliwatts')
        with col2:
            st.header('Decibel')
    
    col1,col2,col3,col4 = st.columns([0.6,0.8,1,0.5])

    with col1:
        
        power_dbm = st.text_input("Power (dBm)", key='wdb_i6', value = 0)
        try:
            power_dbm = float(power_dbm)
        except:
            power_dbm = 0

    with col2:
        st.write('')
        st.write('')
        clicked = st.button("Convert", key='wdb_b6')
    
    with col3:
        if clicked:
            if clicked:
                st.write('')
                result = dBm_to_dB(power_dbm)
                st.success(f'{result:.4f} dB')

with tab1:
    watts_to_db_builder()

with tab2:
    watts_to_dbm_builder()

with tab3:
    dB_to_watts_builder()

with tab4:
    dBm_to_watts_builder()

with tab5:
    dB_to_dBm_builder()

with tab6:
    dBm_to_dB_builder()
 