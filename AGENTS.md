# Instruções para agentes

Este repositório é um modelo de slides para palestras de Python, com o [Slidev](https://sli.dev). A pessoa palestrante escreve a palestra em `slides.md`. A marca vem do topo desse arquivo, e os estilos ficam em `styles/` e `brands/`. A sintaxe do Slidev está em [sli.dev/guide/syntax](https://sli.dev/guide/syntax).

## Arquivos

- `slides.md`: a apresentação. Os slides de exemplo mostram cada layout, com dicas nas anotações. O headmatter, no topo, tem:
  - `brand:`: a pasta da marca em `brands/`.
  - `colorSchema: auto`: o botão de lua e a tecla D trocam entre a versão clara e a escura durante a palestra. Com `light` ou `dark`, o Slidev mostra só essa versão e esconde o botão. Deixe `auto`, a não ser que a pessoa peça outra coisa.
  - `fonts:`: as fontes que o Slidev carrega do Google Fonts. Uma marca com fonte nova precisa da fonte aqui.
- `brands/<marca>/brand.css`: as cores, as fontes, o logo e o texto do rodapé de cada marca, como variáveis CSS. `brand:` no topo do `slides.md` escolhe a pasta.
- `styles/index.css`: o estilo comum a todas as marcas, escrito só com as variáveis da marca. Não mude esse arquivo para resolver um slide: use os layouts abaixo. Mude o arquivo só quando a pessoa pedir.
- `setup/shiki.ts`: as cores do código (GitHub Light nas duas versões).
- `setup/mermaid.ts`: as cores e os tamanhos dos diagramas. O Slidev desenha cada diagrama num shadow DOM, então o `styles/index.css` não chega neles; as cores dos diagramas mudam aqui.
- `global-top.vue`: lê `brand:` e marca o `<html>` com `data-brand`, para o CSS da marca valer.
- `slide-bottom.vue`: o rodapé com o logo ou o nome da marca, e o número do slide. Os layouts `cover`, `section`, `statement`, `end`, `image` e `full` ficam sem rodapé. Para tirar o rodapé de outro slide, use `semRodape: true` no front matter do slide.
- `public/`: imagens servidas na raiz, como `/qr.png`. As imagens em `public/exemplo/` são caixas cinza que marcam o lugar de uma imagem: troque pela imagem da pessoa, nunca use uma delas na palestra.
- `scripts/qr.py`: gera `public/qr.png` (`uv run scripts/qr.py https://endereco`).
- `scripts/previews.py`: gera as imagens do README em `docs/`. Rode depois de mudar `styles/`, `setup/`, `brands/` ou os slides que aparecem nas imagens. O [`CONTRIBUTING.md`](CONTRIBUTING.md) explica.

## Como um slide é escrito

Os slides são separados por `---`. O layout vem do front matter do slide:

```markdown
---
layout: two-cols
---
```

As anotações são um comentário HTML no fim do slide, com dois ou três tópicos curtos:

```markdown
<!--
- Uma dica por linha.
-->
```

## Layouts

| Layout | Markdown esperado |
|---|---|
| (nenhum) | `# Título` e uma lista de 3 a 5 tópicos, uma tabela, um bloco de código ou um diagrama |
| `cover` | `# Título`, subtítulo, `**Nome** · @usuario`. O logo da marca aparece à direita |
| `statement` | `# Frase` em até duas linhas, e uma linha de apoio |
| `quote` | `# Citação` sem aspas (o tema põe as aspas), autoria na linha seguinte |
| `section` | `<div class="numero">01</div>` e `# Título da seção` |
| `two-cols-header` | `# Título` nas duas colunas, `::left::`, `### Coluna` + conteúdo, `::right::`, `### Coluna` + conteúdo. Para comparar: antes e depois, dois trechos de código |
| `two-cols` | Coluna da esquerda, `::right::`, coluna da direita, sem título comum. Para foto ou imagem ao lado do texto |
| `two-cols` com `layoutClass: destaque` | `# Mensagem` na esquerda (vai no painel da cor de destaque) e até quatro tópicos na direita |

Outros recursos:

- Três números: `<div class="numeros">` com três `<div><strong>18</strong><span>rótulo</span></div>`.
- Marca-texto: `<mark>palavra</mark>`.
- Código pequeno de propósito (exemplo do que evitar): envolva o bloco em `<div class="miuda">`.
- Fluxograma ou gráfico: um bloco ` ```mermaid `. Para mudar o tamanho de um fluxograma, use `{scale: 0.8}` depois de `mermaid`.
- QR code: `<img src="/qr.png" alt="QR code para ..." class="qr" />` e uma legenda em `<p class="qr-legenda">`.
- Imagem: `<img src="/caminho.png" alt="..." />`, com o arquivo em `public/`.

## Regras da marca

- As cores vêm das variáveis da marca. Não escreva cores no Markdown. Para imagens ou diagramas que você criar, use as cores do `brand.css` da marca em uso.
- Texto na cor de destaque (`--fill`), só no fundo escuro. No fundo claro, destaque com `<mark>`.
- Barras, ícones e bordas precisam de contraste de 3:1 com o fundo. Cor de destaque clara sobre fundo claro precisa de borda escura.
- Código em cartão claro nas duas versões. Para código em fundo escuro, a pessoa troca `github-light` por `monokai` em `setup/shiki.ts`; nesse caso, use fonte grande.
- Tela de LED do tamanho de uma parede: versão escura. Projetor, TV ou monitor: versão clara.
- Para criar uma marca, siga "Uma marca nova" no [`README.md`](README.md#uma-marca-nova). Variáveis que uma marca define: `--bg`, `--text`, `--muted`, `--accent`, `--fill`, `--on-fill`, `--fill-edge`, `--card`, `--card-line`, `--link`, `--font-sans`, `--font-head`, `--head-weight`, `--head-transform`, `--logo` e `--footer`. `--footer-logo` e `--footer-logo-width` são opcionais. A versão escura redefine as cores em `html.dark[data-brand='...']`.

## Regras de conteúdo

- O conteúdo é da pessoa palestrante. Organize o que ela escreveu em slides, encurte e escolha os layouts, mas não invente fatos, exemplos, números nem opiniões. Se faltar alguma coisa, pergunte.
- Uma ideia por slide. De 3 a 5 tópicos curtos, de uma linha cada quando possível.
- Código: até 8 linhas e 60 colunas por slide (26 colunas em duas colunas). Marque a linguagem do bloco, como ` ```python `.
- Toda imagem tem texto alternativo no `alt`. Gráficos levam os números no texto alternativo ou nas anotações.
- O que não cabe no slide vai para as anotações.
- Escreva no idioma de `lang:`, no topo do arquivo. Use linguagem neutra de gênero quando possível ("pessoa palestrante", "o público", "quem assiste").
- O tom é de dica, não de regra: apoio, sem cobrança e sem prometer resultado. Evite "é só", "é fácil" e "todo mundo sabe".
- Conte mais ou menos 1 minuto por slide, depois de separar uns 5 minutos para perguntas. Pergunte a duração da palestra se não souber.

## Conferir o resultado

Exporte os slides em PNG e olhe os que mudaram:

```sh
npx slidev export --format png --output conferir
```

Para olhar só alguns slides, use `--range 3,7-9`. Para a versão escura, acrescente `--dark`. Com `colorSchema: light` ou `dark` no topo do `slides.md`, o `--dark` não muda nada: o Slidev usa a versão do topo. Apague a pasta `conferir` depois.
