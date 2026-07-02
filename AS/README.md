# AS — Avaliação Substitutiva (recuperação)

Este é o **código-base** da Avaliação Substitutiva. A **prova em si — o que você deve
fazer em cada arquivo — é entregue à parte (SIGAA), no dia.** Aqui ficam só o **sistema**
e a sua **documentação**, para você conhecer o domínio e já deixar o seu *fork* pronto.

> ⚠️ **Antes da prova:** atualize o seu *fork* para receber esta pasta (veja abaixo) e
> confirme que tudo roda no seu Codespace. Você vai trabalhar **dentro desta pasta `AS/`**.

## O sistema: uma locadora de veículos 🚲

Uma **locadora** aluga veículos (bike, patinete, bike elétrica…). O cliente **aluga** um
veículo informando a hora de início e por quantas horas pretende ficar; depois **devolve**.
Na devolução, o sistema:

1. calcula o valor do **aluguel** (uma base fixa + um valor por hora, que depende do tipo);
2. soma a **multa** se a devolução passou do horário previsto;
3. **cobra** o cliente (serviço de cobrança); e
4. **avisa** os setores interessados (manutenção, painel, financeiro).

Há ainda uma função **`simular`**, que mostra quanto sairia **sem** devolver de fato.

## O que tem aqui
```
AS/
├── locadora.py        ← o sistema (alugar, devolver, simular)
├── precos.py          ← quanto custa cada tipo de veículo
├── cobranca.py        ← serviço externo de cobrança (o "gateway")
├── test_locadora.py   ← testes que passam — a sua rede de segurança
├── pyproject.toml     ← config do linter (ruff) e da cobertura
└── ci.yml             ← o pipeline de CI (copie p/ .github/workflows/ no seu fork)
```

## Como rodar (no Codespaces)
```bash
cd AS
pytest                       # a rede de segurança
ruff check .                 # estilo do código
pytest --cov=. --cov-report=term-missing --cov-fail-under=80
```

## Como atualizar o seu fork (pegar esta pasta)
No seu *fork*, pela interface do GitHub, use **Sync fork** (Sincronizar fork) para trazer
as novidades do repositório da disciplina. Ou, no terminal do seu Codespace:
```bash
git remote add upstream https://github.com/fab-araujo/bsi-fpsm-2026.1-ESII.git   # 1ª vez só
git fetch upstream
git merge upstream/main
```
Depois abra a pasta `AS/` — ela deve estar lá.

---
*Prof. Fabrício A. Araújo · fabricio.araujo@ufra.edu.br*
