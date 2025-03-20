# Zombie Horde

Projeto desenvolvido no **Curso Superior Técnologo de Análise de Desenvolimento de Sistemas** do **Centro Universitário Internacional Uninter** para a matéria de **Linguagem de Programação Aplicada**.

## Especificações do projeto

Desenvolvido com [Pygame](https://github.com/pygame/pygame).

O game loop é centralizado na classe `Game` instanciada pelo `Main` e a lógica de cada contexto do jogo é encapsulada por cenas. Isso remove a necessidade de múltiplos loops e de repetição de código que é compartilhado entre cada contexto (como a verificação do evento `pygame.QUIT`).

Utilizando o padrão de singletons para gerenciar as cenas e inputs.

O gerenciamento de inputs é realizado por um singleton `InputSystem` que fornece um método para vincular funções com as keys desejadas.

As cenas encapsulam a lógica de cada contexto do jogo, como Menu, Level 1, Level 2, etc.

## Créditos

Este projeto utiliza assets disponibilizados no [OpenGameArt.org](https://opengameart.org) sob a licença [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).

### Assets utilizados:

- **Animated Top Down Survivor Player** por [rileygombart](https://opengameart.org/users/rileygombart): https://opengameart.org/content/animated-top-down-survivor-player
- **"Animated Top Down Zombie"** por [rileygombart](https://opengameart.org/users/rileygombart): https://opengameart.org/content/animated-top-down-zombie

Os assets podem ter sido modificados para melhor se adequar ao projeto.
