# SPRINT 4 - GoodWe Smart Charging Station (Simulador)

Este repositório contém a documentação técnica e o código-fonte da solução final integrada para o gerenciamento inteligente de recarga de veículos elétricos (EVs). O projeto foi desenvolvido como uma simulação educacional para a **FIAP** (Turma 1CCPW), utilizando um **Raspberry Pi Pico** e **MicroPython** no ambiente Wokwi, com inspiração na lógica da *GoodWe Smart Energy Controller*.

## 🎯 Objetivo do Projeto
Demonstrar, de forma funcional, como um sistema computacional embarcado recebe informações, processa dados e gerencia de forma inteligente e autônoma a distribuição de uma quantidade limitada de energia entre múltiplos veículos, aplicando conceitos fundamentais de Arquitetura de Computadores.

## 👥 Integrantes
* Enzo Yudi de Oliveira Hino (RM: 570173)
* Inaldo Pereira Freitas (RM: 569672)
* Felipe Elze (RM: 572024)
* Henrique Eduardo da Silveira (RM: 571803)
* Arthur Micarelli (RM: 571476)

## ⚙️ Arquitetura de Hardware (Simulação no Wokwi)
O hardware simulado foi projetado para focar na resposta do sistema. Utiliza os seguintes componentes:
* **Processador Central:** Raspberry Pi Pico.
* **Sinalização Visual (Saída):** 3 LEDs conectados via pinos GPIO para indicar o status de saúde da rede (Grid).
  * 🟢 **LED Verde (GP2):** Recarga Ativa (Sobra de energia no sistema).
  * 🟡 **LED Amarelo (GP3):** Recarga Controlada (Demanda excedeu a rede, redução aplicada).
  * 🔴 **LED Vermelho (GP4):** Recarga Limitada (Rede em risco, veículos em fila de espera).

## 🧠 Lógica de Gerenciamento de Energia
O algoritmo monitora ativamente a energia disponível na rede e a compara com a demanda de três veículos simultâneos (Demandas fixadas em: EV1 = 2.000W, EV2 = 2.500W, EV3 = 3.000W. Demanda Total = 7.500W). O sistema reage dinamicamente em três cenários:

| Cenário | Condição de Energia | Ação do Algoritmo | Status Visual |
| :--- | :--- | :--- | :--- |
| **Alta Disponibilidade** | `Energia >= 7.500W` | **Fornecimento Total:** A rede suporta o consumo. 100% da potência solicitada é entregue a todos os veículos. | 🟢 LED Verde |
| **Disponibilidade Limitada** | `3.000W <= Energia < 7.500W` | **Rateio Proporcional:** A demanda ultrapassa a rede. O sistema calcula um fator de redução baseado na proporção (`Energia / Demanda Total`) e corta a potência de todos os veículos de forma igualitária para não derrubar o grid. | 🟡 LED Amarelo |
| **Baixa Disponibilidade** | `Energia < 3.000W` | **Corte e Prioridade:** Há risco de queda geral. Para evitar um carregamento ineficiente, o sistema bloqueia totalmente o EV2 e EV3 (0W) e direciona a carga crítica restante apenas para o EV1. | 🔴 LED Vermelho |

## 💻 Aplicação dos Conceitos de Arquitetura de Computadores
O funcionamento da solução está diretamente ligado à teoria de sistemas computacionais:

* **Processamento (CPU e ULA):** O Raspberry Pi Pico atua como o cérebro. A sua Unidade Lógica e Aritmética (ULA) é responsável por executar as comparações condicionais (`if/elif/else`) e realizar os cálculos matemáticos de redução proporcional da potência no cenário de disponibilidade limitada.
* **Memória RAM:** Utilizada para alocar as variáveis de execução durante o ciclo de gerenciamento, como os dados de bateria, limites de demanda (`ev1_req`, `ev2_req`) e os resultados dinâmicos do fator de corte, permitindo acesso rápido do processador.
* **Entrada/Saída (I/O) e Comunicação:** O sistema utiliza os pinos GPIO para converter instruções lógicas de software em sinais elétricos de saída (Output) que acendem os LEDs. Adicionalmente, utiliza **Comunicação Serial** para enviar os dados detalhados da simulação para a interface do Monitor Serial.
* **Representação de Dados:** O algoritmo evidencia a camada física da computação ao converter e exibir os valores de energia do sistema Decimal padrão para suas verdadeiras representações de máquina: **Binário** (ex: `0b1001110001000`) e **Hexadecimal** (ex: `0x1388`).
* **Automação:** O sistema demonstra a capacidade de tomar decisões de bloqueio e liberação de carga em tempo real, sem a necessidade de intervenção de um operador humano.

## 🚀 Como Executar a Simulação
1. Acesse o ambiente Wokwi através do link da simulação: `[Cole o link do seu projeto no Wokwi aqui]`
2. Inicie a execução clicando no botão **Play**.
3. O software executará um loop de demonstração, simulando alterações drásticas na rede de energia a cada 8 segundos.
4. Acompanhe a atuação autônoma dos LEDs no circuito e verifique o Monitor Serial na parte inferior da tela para analisar os logs de distribuição de energia, cálculos matemáticos e a conversão das bases numéricas.
