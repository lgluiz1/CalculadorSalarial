import streamlit as st
from workalendar.america import Brazil
from datetime import date

cal = Brazil()

def calcularDias(data_inicial, data_final):
    # Não precisa converter, já são objetos date
    dias_uteis = cal.get_working_days_delta(data_inicial, data_final)
    return dias_uteis

def main():
    st.title('Calculadora de Salário Proporcional')

    # Cria duas colunas para as datas
    col1, col2 = st.columns(2)

    with col1:
        calendario_de = st.date_input('Início de')
    with col2:
        calendario_ate = st.date_input('Final até')

    # Valor do salário
    salario = st.number_input('Salário mensal', value=0.0, step=0.01, format="%.2f")

    # Botão para calcular
    if st.button('Calcular'):
        if calendario_de > calendario_ate:
            st.error('A data inicial não pode ser depois da data final.')
        else:
            dias_uteis = calcularDias(calendario_de, calendario_ate)
            
            if dias_uteis > 0:
                salario_por_dia = salario / 22  # Considerando 22 dias úteis no mês em média
                salario_proporcional = salario_por_dia * dias_uteis

                st.write('Dias úteis no período:', dias_uteis)
                st.write('Salário por dia (base 22 dias úteis/mês): R$', f"{salario_por_dia:.2f}")
                st.write('Salário proporcional para o período: R$', f"{salario_proporcional:.2f}")
            else:
                st.warning('Nenhum dia útil no período selecionado.')

if __name__ == '__main__':
    main()
