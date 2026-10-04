# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow"]
# ///
"""Gera as imagens do README a partir de slides.md.

    uv run scripts/previews.py

Exporta os slides em PNG com o Slidev (npx slidev export), nas variantes
Python Floripa clara e escura e Python Brasil clara e escura, e monta:

    docs/overview.png          seis slides da versão clara
    docs/overview-escura.png   os mesmos seis, na versão escura
    docs/python-brasil.png     três slides com a marca Python Brasil
    docs/python-brasil-escura.png  os mesmos três, na versão escura
    docs/codigo.png            o slide de código, na versão escura
    docs/cores/<HEX>.png       uma amostra para cada cor de brands/*/brand.css

Se o Slidev não achar o Chromium, rode `npx playwright install chromium` ou
aponte CHROMIUM_PATH para um Chrome ou Chromium instalado.
"""

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"

SLIDES_DA_VISAO_GERAL = [1, 7, 10, 14, 15, 18]
SLIDES_DA_PYTHON_BRASIL = [1, 10, 14]
SLIDE_DE_CODIGO = 10

LARGURA_DA_MINIATURA = 640
MARGEM = 6
COR_DA_MARGEM = "#d0d7de"


def variante(nome: str, substituicoes: dict[str, str]) -> Path:
    """Copia slides.md com outro headmatter, ao lado do original, para o Slidev achar setup/ e public/."""
    texto = (RAIZ / "slides.md").read_text(encoding="utf-8")
    for chave, valor in substituicoes.items():
        texto, trocas = re.subn(rf"^{chave}: .*$", f"{chave}: {valor}", texto, count=1, flags=re.M)
        if not trocas:
            raise SystemExit(f"slides.md não tem `{chave}:` no topo.")
    arquivo = RAIZ / f".preview-{nome}.md"
    arquivo.write_text(texto, encoding="utf-8")
    return arquivo


def exportar(arquivo: Path, destino: Path) -> dict[int, Path]:
    npx = shutil.which("npx") or "npx"
    comando = [npx, "slidev", "export", arquivo.name, "--format", "png", "--output", str(destino)]
    if os.environ.get("CHROMIUM_PATH"):
        comando += ["--executable-path", os.environ["CHROMIUM_PATH"]]
    subprocess.run(comando, cwd=RAIZ, check=True)
    return {int(png.stem): png for png in destino.glob("*.png")}


def grade(imagens: list[Path], colunas: int, saida: Path) -> None:
    miniaturas = []
    for caminho in imagens:
        with Image.open(caminho) as imagem:
            altura = round(imagem.height * LARGURA_DA_MINIATURA / imagem.width)
            miniaturas.append(imagem.convert("RGB").resize((LARGURA_DA_MINIATURA, altura), Image.LANCZOS))
    altura = miniaturas[0].height
    linhas = -(-len(miniaturas) // colunas)
    folha = Image.new(
        "RGB",
        (colunas * (LARGURA_DA_MINIATURA + 2 * MARGEM), linhas * (altura + 2 * MARGEM)),
        COR_DA_MARGEM,
    )
    for i, miniatura in enumerate(miniaturas):
        x = (i % colunas) * (LARGURA_DA_MINIATURA + 2 * MARGEM) + MARGEM
        y = (i // colunas) * (altura + 2 * MARGEM) + MARGEM
        folha.paste(miniatura, (x, y))
    folha.save(saida, optimize=True)


def amostras_de_cor() -> None:
    pasta = DOCS / "cores"
    pasta.mkdir(parents=True, exist_ok=True)
    cores = set()
    for css in RAIZ.glob("brands/*/brand.css"):
        cores |= {c.upper() for c in re.findall(r"#([0-9a-fA-F]{6})\b", css.read_text(encoding="utf-8"))}
    for cor in sorted(cores):
        amostra = ImageOps.expand(Image.new("RGB", (40, 40), f"#{cor}"), border=1, fill="#888888")
        amostra.save(pasta / f"{cor}.png")


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    variantes = {
        "clara": variante("clara", {"brand": "python-floripa", "colorSchema": "light"}),
        "escura": variante("escura", {"brand": "python-floripa", "colorSchema": "dark"}),
        "python-brasil": variante("python-brasil", {"brand": "python-brasil", "colorSchema": "light"}),
        "python-brasil-escura": variante("python-brasil-escura", {"brand": "python-brasil", "colorSchema": "dark"}),
    }
    try:
        with tempfile.TemporaryDirectory() as temporaria:
            slides = {nome: exportar(arquivo, Path(temporaria) / nome) for nome, arquivo in variantes.items()}
            grade([slides["clara"][n] for n in SLIDES_DA_VISAO_GERAL], 3, DOCS / "overview.png")
            grade([slides["escura"][n] for n in SLIDES_DA_VISAO_GERAL], 3, DOCS / "overview-escura.png")
            grade([slides["python-brasil"][n] for n in SLIDES_DA_PYTHON_BRASIL], 3, DOCS / "python-brasil.png")
            grade([slides["python-brasil-escura"][n] for n in SLIDES_DA_PYTHON_BRASIL], 3, DOCS / "python-brasil-escura.png")
            with Image.open(slides["escura"][SLIDE_DE_CODIGO]) as codigo:
                codigo.convert("RGB").resize((1280, round(codigo.height * 1280 / codigo.width)), Image.LANCZOS).save(
                    DOCS / "codigo.png", optimize=True
                )
    finally:
        for arquivo in variantes.values():
            arquivo.unlink(missing_ok=True)
    amostras_de_cor()
    print("Imagens atualizadas em docs/.")


if __name__ == "__main__":
    main()
