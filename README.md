# <i>Cifra de Vigenère</i>👨🏻‍💻
<p align="justify"> O código é uma implementação de um cifra de substituição polialfabética, conhecida como "cifra de Vigenère". Ele recebe uma string de texto `plain` e um valor inteiro `key` como entrada e retorna uma versão cifrada da string.</p>

1. Na primeira linha, a importação da biblioteca `string` é feita para obter a sequência de caracteres contendo todas as letras minúsculas do alfabeto inglês.

2. A função `poly` é definida com dois parâmetros: `plain` (a string de texto a ser cifrada) e `key` (a chave de cifra para determinar a substituição dos caracteres). A anotação `-> str` indica que a função retorna uma string.

3. A primeira linha dentro da função `poly` converte a string `plain` para letras minúsculas usando o método `lower()`.

4. Em seguida, é definido um dicionário vazio chamado `charset`, que será usado para mapear as letras originais para as letras cifradas.

5. A variável `letters` contém todas as letras minúsculas do alfabeto inglês.

6. O loop `for` itera sobre cada letra em `letters`. A cada iteração, a letra original (`letters[i-key]`) é mapeada para a letra cifrada correspondente (`letters[i]`). Essa operação é feita para criar um mapeamento de substituição para cada letra com base no valor da chave `key`. O mapeamento é armazenado no dicionário `charset`.

7. Em seguida, é definida uma função interna chamada `encdec` com dois parâmetros: `plain` (a string de texto a ser cifrada ou decifrada) e `charset` (o dicionário contendo o mapeamento de substituição).

8. A variável `es` é inicializada como uma string vazia. Essa variável será usada para armazenar o resultado da cifração ou decifração.

9. O loop `for` itera sobre cada caractere na string `plain`. Para cada caractere, verifica-se se ele está presente no dicionário `charset`. Se estiver presente, a letra cifrada correspondente é adicionada à string `es`. Caso contrário, o caractere original é mantido na string `es`.

10. Após iterar por todos os caracteres, a função `encdec` retorna a string resultante `es`.

11. A função `poly` retorna o resultado da função `encdec`, convertido para letras maiúsculas usando o método `upper()`.

12. Finalmente, um loop `for` é usado para testar todas as possíveis chaves de cifra de 1 a 26. Para cada chave, a função `poly` é chamada com a string "CKZPYAC QSZHCAR EYKC QSNNJW" e a chave atual. O resultado é armazenado na variável `possible_answer`.

13. O resultado e a chave correspondente são impressos na tela usando o comando `print(f'{possible_answer}, Key:{i+1}')`. A variável `i` é incrementada em 1 para exibir a chave atual começando de 1 em vez de 0.

Dessa forma, o código testa todas as possíveis chaves e imprime os resultados cifrados correspondentes para cada chave. Isso pode ser usado para determinar a chave correta e decifrar o texto original.
