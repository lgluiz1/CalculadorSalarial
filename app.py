import streamlit as st

def calcular_dias_trabalhados(data_inicial, data_final):
    dias_trabalhados = (data_final - data_inicial).days
    return dias_trabalhados

def calcular_salario_bruto(dias_trabalhados, salario):
    salario_bruto = dias_trabalhados * salario
    return salario_bruto

def main():
    st.title('Calculadora')

    # Cria duas colunas
    col1, col2 = st.columns(2)

    # Inputs em colunas separadas
    with col1:
        calendario_de = st.date_input('Inicio de')
        st.write('Data inicial:', calendario_de)
    with col2:
        calendario_ate = st.date_input('Final até')
        st.write('Data final:', calendario_ate)

    # Valor Salario
    salario = st.number_input('Salario', value=0, step=1)
    st.write('Salario:', salario)


    # Botão para calcular
    if st.button('Calcular'):

        st.write('Data inicial:', calendario_de)
        st.write('Data final:', calendario_ate)
    

if __name__ == '__main__':
    main()
