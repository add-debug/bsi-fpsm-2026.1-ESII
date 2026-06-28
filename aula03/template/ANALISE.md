# Análise — as 3 responsabilidades da classe `Academia` (v1.0)

**Sua tarefa (Parte 2 da atividade, 0,3):** responder com **suas palavras**
(2–4 frases por item), olhando o arquivo `academia.py` da pasta da aula.
Substitua cada `...` pela sua resposta.

---

## 1. Quais são as 3 responsabilidades grudadas na classe `Academia`?
A classe Academia faz regras de negócio e gerenciamento da interface de tela  e o envio de notificações externas.
> ...

## 2. Aponte, no código, **uma linha** de cada responsabilidade
•	Regra de Negócio: Linhas 18 a 24.
•	Interface: Linhas 14 a 16.
•	Notificação: Linha 33.

## 3. Como o SRP separa essas responsabilidades?
A Regra de Negócio passa a morar na classe AcademiaService.
Interface passa a morar na função main().
Notificação passa a morar na classe Notificador.
> ...

## 4. Por que ficou melhor? Cite **um** RNF
Testabilidade. No código original, é impossível testar as regras de negócio de forma automatizada sem que o código trave esperando uma digitação do usuário (input). Ao separar as responsabilidades, podemos testar a lógica de cálculo de planos e check-ins isoladamente de forma rápida e automática.
> ...
