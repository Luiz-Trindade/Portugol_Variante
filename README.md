<image src="https://www.gnu.org/graphics/gplv3-127x51.png">

# Interpretador PORTUGOL Personalizado

Bem-vindo ao Interpretador PORTUGOL, uma variante personalizada desenvolvida por Luiz Gabriel Magalhães Trindade. Este interpretador permite a execução de programas escritos em uma linguagem de programação inspirada no PORTUGOL.

## Versão

A versão atual do interpretador é 1.0.

## Como Usar

Para utilizar o interpretador, siga as instruções abaixo:

1. **Defina o Programa:**
   Execute o interpretador fornecendo o arquivo do programa PORTUGOL como argumento. Por exemplo:
   ```bash
   python3 portugol.py MeuPrograma.por
   ```

2. **Visualize a Versão:**
   Se desejar verificar a versão do interpretador, utilize o argumento `-v`:
   ```bash
   python3 portugol.py -v
   ```

## Recursos da Linguagem

### Comandos Suportados

- **algoritmo:** Define o início do programa. O nome do algoritmo deve corresponder ao nome do programa.

- **texto:** Declaração de variáveis de texto.

- **numero:** Declaração de variáveis numéricas.

- **inicio:** Indica o início do programa.

- **escreva:** Comando para imprimir na saída.

- **fim:** Indica o fim do programa.

### Exemplo Básico

```portugol
algoritmo MeuPrimeiroPrograma

texto: mensagem
numero: preco

inicio

    mensagem <- "Olá, Mundo!"
    preco <- 10.5

    escreva mensagem
    escreva "O preço é:" preco

fim
```

Este exemplo imprime "Olá, Mundo!" e "O preço é: 10.5" na saída.

## Avisos Legais

Este programa é software livre; você pode redistribuí-lo e/ou modificá-lo sob os termos da [Licença Pública Geral GNU](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text) conforme publicada pela Free Software Foundation. Este programa é distribuído na esperança de que possa ser útil, mas SEM NENHUMA GARANTIA; sem uma garantia implícita de COMERCIALIZAÇÃO ou ADEQUAÇÃO a qualquer PROPÓSITO EM PARTICULAR. Consulte a [licença](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text) para obter mais detalhes.

---

*Este interpretador foi desenvolvido por Luiz Gabriel Magalhães Trindade, estudante de Ciência da Computação.*