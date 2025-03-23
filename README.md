# 🧟 Zombie Horde

**Zombie Horde** é um shooter top-down desenvolvido com **Python** e **Pygame**, onde o jogador precisa sobreviver por 20 segundos enfrentando uma horda de zumbis.  
Este projeto foi desenvolvido como parte da disciplina **Linguagem de Programação Aplicada** no curso de **Análise e Desenvolvimento de Sistemas** do **Centro Universitário Internacional Uninter**.

## 📦 Tecnologias e Arquitetura

- **Linguagem:** Python 3
- **Biblioteca:** [Pygame](https://github.com/pygame/pygame)
- **Banco de Dados:** SQLite (nativo do Python, para armazenamento de pontuações)

### 🧠 Padrões de Projeto Utilizados

- **Singleton:**
  - `SceneFactory` e `InputSystem` usam Singleton para manter instâncias únicas e globais.
- **Factory:**
  - `SceneFactory` e `EntityFactory` são responsáveis pela criação organizada de cenas e entidades.
- **Mediator:**
  - `EntityMediator` centraliza a lógica de colisão e interações entre entidades (tiros, zumbis, jogador).

### 🧩 Arquitetura Modular

O código é organizado em **cenas** e **entidades**, com responsabilidades bem definidas, como por exemplo:

- `Game.py`: Loop principal e ciclo de vida do jogo
- `Scene.py`: Classe base abstrata para as cenas
- `Menu.py`, `Level.py`, `GameOverMenu.py`: Cenas específicas
- `Entity.py`: Classe base para todas as entidades
- `Player.py`, `Zombie.py`, `PlayerShot.py`, `Background.py`: Entidades do jogo
- `InputSystem.py`, `AudioManager.py`, `EntityMediator.py`: Sistemas de suporte

## 🎮 Gameplay

### Objetivo

Sobreviva por **20 segundos** enquanto elimina o maior número possível de zumbis!

### Mecânicas

- Zumbis aparecem a cada segundo e atacam o jogador
- Cada zumbi tem 100 de vida e causa 10 de dano ao encostar
- O jogador tem 100 de vida e atira projéteis que causam 34 de dano
- Cada acerto em um zumbi vale **1 ponto**
- O jogo termina quando o tempo acaba ou o jogador morre

### Controles

- 🔼 🔽 ◀️ ▶️: Movimento
- **Espaço**: Atirar

## 📺 HUD

Durante o jogo, a interface exibe:

- ❤️ Vida do jogador
- 🧟‍♂️ Quantidade de zumbis
- ⏱️ Tempo restante
- ⭐ Pontuação atual

---

## 🔊 Áudio e Assets

O jogo conta com sprites animados, efeitos sonoros e música de fundo.

### Créditos dos Assets

Os seguintes assets foram utilizados sob a licença [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/), com possíveis modificações:

- 👤 [**Animated Top Down Survivor Player**](https://opengameart.org/content/animated-top-down-survivor-player) – por [rileygombart](https://opengameart.org/users/rileygombart)
- 🧟 [**Animated Top Down Zombie**](https://opengameart.org/content/animated-top-down-zombie) – por [rileygombart](https://opengameart.org/users/rileygombart)
- 🎵 [**Tragic ambient main menu**](https://opengameart.org/content/tragic-ambient-main-menu) – por brandon75689
- 🔫 [**Shotgun Shoot + Reload**](https://opengameart.org/content/shotgun-shoot-reload) – por Mike Koenig (Soundbible)

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/Gustavo-Aal/zombie-horde-game.git
cd zombie-horde-game

# Instale as dependências
pip install pygame

# Execute o jogo
python main.py
```
