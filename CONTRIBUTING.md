# Como contribuir

Correções e marcas novas são bem-vindas. Abra uma issue antes de uma mudança grande, para combinar o caminho.

## Preparar

Você vai precisar do [Node.js](https://nodejs.org) 22.12 ou mais novo e do [uv](https://docs.astral.sh/uv/).

```sh
npm install
npx playwright install chromium
npm run dev
```

## Atualizar as imagens do README

As imagens em `docs/` saem dos próprios slides. Depois de mudar `slides.md`, `styles/`, `setup/` ou `brands/`, gere as imagens de novo:

```sh
uv run scripts/previews.py
```

O script exporta os slides nas versões clara e escura das duas marcas, e regrava:

| Arquivo | Conteúdo |
|---|---|
| `docs/overview.png` | Seis slides da versão clara |
| `docs/overview-escura.png` | Os mesmos seis, na versão escura |
| `docs/python-brasil.png` | Capa, código e fluxograma com a marca Python Brasil |
| `docs/python-brasil-escura.png` | Os mesmos três, na versão escura |
| `docs/codigo.png` | O slide de código na versão escura |
| `docs/cores/*.png` | Uma amostra de cada cor dos arquivos `brands/*/brand.css` |

Os números dos slides de cada imagem ficam no topo de `scripts/previews.py`. Se você acrescentar ou tirar um slide, confira esses números. Se o Slidev não achar o Chromium, aponte `CHROMIUM_PATH` para um Chrome ou Chromium instalado:

```sh
CHROMIUM_PATH=/caminho/do/chrome uv run scripts/previews.py
```

Olhe as imagens antes do commit. Se uma imagem mudou sem você querer, a mudança no CSS pegou outro slide.

## Conferir uma mudança

- Exporte os slides que mudaram e olhe as versões clara e escura das duas marcas. O [`AGENTS.md`](AGENTS.md#conferir-o-resultado) mostra os comandos.
- Confira o contraste de cada cor nova no [verificador da WebAIM](https://webaim.org/resources/contrastchecker/): 4.5:1 para texto e 3:1 para barras, ícones e bordas.
- Rode `npm run build` para conferir que o site sai sem erro.

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/): `feat(brands): add Python Sul`, `fix(styles): keep the footer inside the slide`, `docs(readme): ...`. Separe mudanças de nome ou de lugar das mudanças de comportamento, em commits diferentes.

## Licença

Ao contribuir, você aceita publicar a sua contribuição sob a [CC0 1.0](LICENSE). Logos e identidades visuais continuam das comunidades donas de cada marca: inclua só marcas que a comunidade autorizou.
