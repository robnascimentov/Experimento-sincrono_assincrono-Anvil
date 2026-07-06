# Experimento Prático: Concorrência e Bloqueio de Interfaces (Anvil Python)

Este repositório apresenta a resolução da atividade acadêmica prática voltada ao estudo de sistemas concorrentes. O objetivo é demonstrar o impacto do bloqueio da thread principal de interface gráfica (User Interface Thread) e as vantagens arquiteturais do processamento assíncrono em sistemas multimídia.

## Link do Aplicativo Web Funcionando
O projeto foi desenvolvido e publicado de forma totalmente online através da plataforma Anvil. Você pode testar e interagir com o experimento em tempo real clicando no link público abaixo:
=> https://impish-yearly-jay.anvil.app

## Funcionamento do Teste Acadêmico
O software simula visualmente duas formas de requisições computacionais de longa duração (5 segundos):
* **Botão Síncrono:** Ao ser acionado, desativa temporariamente os demais componentes da interface gráfica (`enabled = False`), simulando o congelamento total que ocorre em threads lineares pesadas e ilustrando o problema clássico de concorrência visual.
* **Botão Assíncrono:** Dispara eventos de temporização em background (segundo plano) via componentes `Timer` nativos da biblioteca, destruindo o componente após a execução. A interface do usuário permanece totalmente livre e responsiva para cliques simultâneos no botão de interatividade.

## Estrutura de Arquivos do Repositório
* `main.py`: Código-fonte completo em Python das rotinas do front-end e lógica de manipulação de estados do aplicativo.
* `ARTIGO_Analise do Tempo de Resposta em Interfaces Multimidia.pdf`: Artigo científico de fundamentação teórica acoplado na raiz do repositório (Padrão SBC).
