import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import datetime
import time
import pandas as pd

from models.passenger_model import PassengerModel
from models.passengers_model import PassengersModel


with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()

if st.session_state["authentication_status"]:

    
    with st.expander(f'Bem-vindo, *{st.session_state["name"]}*'):
        authenticator.logout()



    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.metric(label="Passageiros cadastrados", value="120")
    with col2:
        with st.container(border=True):
            st.metric(label="Passageiros ativos", value="120")
    with col3:
        with st.container(border=True):
            st.metric(label="Passageiros inativos", value="120")
   


    with st.form("My Form"):
        st.subheader("Cadastrar passageiro(a)")
        passenger_name = st.text_input('Nome do passageiro(a):')
        phone_number = st.text_input('Número do telefone')

        submitted = st.form_submit_button("Cadastrar passageiro(a)", type='primary')
        if submitted:
            with st.spinner('Cadastrando passageiro(a)'):
                
                new_passenger = PassengerModel({
                    "passenger_name": passenger_name,
                    "phone_number": phone_number
                })

                if new_passenger.register_passenger():
                    st.toast('Passageiro(a) cadastrado(a) com sucesso!', icon='✅')
                    #st.success('Passageiro(a) cadastrado(a) com sucesso!', icon='✅')
                else:
                    st.info(f'Já existe outro passageiro(a) cadastrado(a) com o telefone {phone_number}', icon="ℹ️")
    

        #st.info('This is a purely informational message', icon="ℹ️")
        #st.success('This is a success message!', icon="✅")

    with st.container(border=True):
        
        st.write('Passageiros cadastrados')
    
        if st.button("Mostrar todos os passageiros", type="secondary"):
            with st.spinner('Buscando passageiros'):
                passengers_df = PassengersModel().get_all_passengers()

                passengers_df = passengers_df[['passenger_name', 'phone_number', 'whatsapp_link']]

                st.data_editor(
                    passengers_df,
                    column_config={
                        "whatsapp_link": st.column_config.LinkColumn(
                            display_text="whatsapp"               
                        )

                    }
                )





elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
