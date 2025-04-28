# 📅 Calculadora de Salário Proporcional

Este projeto é uma aplicação simples feita com **Streamlit** e **Workalendar** que calcula o salário proporcional baseado na quantidade de **dias úteis** entre duas datas, descontando automaticamente **finais de semana** e **feriados** nacionais do Brasil.

[Deploy Projeto aqui](https://caculadorasalarial.streamlit.app/) — Voçê pode visualiza o projeto aqui nesse link.

---

## 🚀 Funcionalidades

- Seleção de datas de início e fim.
- Cálculo de dias úteis (descontando sábados, domingos e feriados).
- Cálculo do salário proporcional ao período informado.
- Interface Web simples e rápida usando Streamlit.

---

## 🛠 Tecnologias utilizadas

- [Streamlit](https://streamlit.io/) — para criação da interface web.
- [Workalendar](https://workalendar.readthedocs.io/) — para cálculo de feriados e dias úteis no Brasil.
- [Python 3.10+](https://www.python.org/) — linguagem de programação usada.

---

## 📥 Como instalar e rodar o projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Rode a aplicação:

   ```bash
   streamlit run app.py
   ```

   *(supondo que seu arquivo principal se chama `app.py` — ajuste conforme o nome do seu arquivo.)*

---

## 📸 Tela da aplicação

*(adicione aqui um printscreen depois que estiver funcionando!)*

---

## 📋 Observações

- O salário diário é calculado considerando apenas os dias úteis entre as datas informadas.
- Atualmente, apenas feriados **nacionais** são considerados. (Pode ser expandido para estaduais/municipais.)

---

## 🤝 Contribuição

Pull requests são bem-vindos!  
Para mudanças maiores, abra uma issue primeiro para discutirmos o que você gostaria de mudar.

---

## 📄 Licença

Este projeto está sob a licença MIT.  
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### ✨ Desenvolvido com dedicação e café!

