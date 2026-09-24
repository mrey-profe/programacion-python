#!/bin/bash
#
# Convierte notebooks (.ipynb) a PDF sin los outputs de las celdas.
#
# Uso:
#   ./script-conversion.sh [-o DIR_SALIDA] NOTEBOOK|DIRECTORIO...
#
# - NOTEBOOK: ruta a un .ipynb concreto.
# - DIRECTORIO: se convierten todos los .ipynb que contiene (sin entrar en subdirectorios).
# - -o DIR_SALIDA: carpeta de destino de los PDF (por defecto: pdf/ junto al script).
#
# Ejemplo (apuntes del tema 01):
#   ./script-conversion.sh 01Tipos_y_operadores/{01print,02Literales_y_tipos,03operadores,04variables_comentarios,05input}.ipynb

script_dir=$(cd "$(dirname "$0")" && pwd)
output_dir="${script_dir}/pdf"

usage() {
    sed -n '4,13p' "$0" | sed 's/^# \{0,1\}//'
    exit 1
}

while getopts "o:h" opt; do
    case "$opt" in
        o) output_dir=$(mkdir -p "$OPTARG" && cd "$OPTARG" && pwd) || exit 1 ;;
        *) usage ;;
    esac
done
shift $((OPTIND - 1))

[ $# -eq 0 ] && usage

# Usar el jupyter del entorno virtual del repo si existe
jupyter="${script_dir}/.venv/bin/jupyter"
[ -x "$jupyter" ] || jupyter=jupyter

mkdir -p "$output_dir"

# Directorio temporal para las copias sin outputs
tmp_dir=$(mktemp -d)
trap 'rm -rf "$tmp_dir"' EXIT

# Recopilar los notebooks indicados (los directorios se expanden a sus .ipynb, ordenados)
notebooks=()
for arg in "$@"; do
    if [ -d "$arg" ]; then
        mapfile -t found < <(find "$arg" -maxdepth 1 -name "*.ipynb" | sort)
        notebooks+=("${found[@]}")
    elif [ -f "$arg" ] && [[ "$arg" == *.ipynb ]]; then
        notebooks+=("$arg")
    else
        echo "Ignorado (no es un .ipynb ni un directorio): $arg"
    fi
done

counter=1
for notebook in "${notebooks[@]}"; do
    base_name=$(basename "$notebook" .ipynb)

    # Subdirectorio propio para evitar colisiones de nombre entre notebooks de distintos directorios
    notebook_tmp_dir="${tmp_dir}/${counter}"
    mkdir -p "$notebook_tmp_dir"

    # Las imágenes se referencian con rutas relativas al notebook: copiar images/ junto a la copia temporal para poder incrustarlas
    notebook_dir=$(dirname "$notebook")
    [ -d "${notebook_dir}/images" ] && cp -r "${notebook_dir}/images" "$notebook_tmp_dir/"

    # Crear copia temporal sin outputs de celdas
    "$jupyter" nbconvert --to notebook \
        --ClearOutputPreprocessor.enabled=True \
        --output-dir "$notebook_tmp_dir" \
        "$notebook" 2>/dev/null

    tmp_notebook="${notebook_tmp_dir}/${base_name}.ipynb"

    if [ -f "$tmp_notebook" ]; then
        # Convertir la copia limpia a PDF (--embed-images: el PDF se genera sin ruta base, las imágenes deben ir incrustadas)
        if "$jupyter" nbconvert --to webpdf "$tmp_notebook" \
            --template webpdf_wrap \
            --embed-images \
            --TemplateExporter.extra_template_basedirs="['${script_dir}/nbconvert_templates']" \
            --output "${output_dir}/${base_name}"; then
            echo "Converted: $notebook -> ${output_dir}/${base_name}.pdf"
        else
            echo "Failed to convert: $notebook"
        fi
    else
        echo "Failed to clear outputs for: $notebook"
    fi

    counter=$((counter + 1))
done
