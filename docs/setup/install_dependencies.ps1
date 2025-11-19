# Script para instalar/actualizar dependencias del proyecto
# Autor: Equipo Natursur
# Fecha: Noviembre 2025
#
# Este script:
# 1. Crea el entorno virtual si no existe
# 2. Instala/actualiza todas las dependencias desde requirements.txt
# 3. Actualiza el requirements.txt con las dependencias instaladas

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CONFIGURAR DEPENDENCIAS DEL PROYECTO" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar que existe requirements.txt
if (-Not (Test-Path "requirements.txt")) {
    Write-Host "ERROR: No se encuentra el archivo 'requirements.txt'" -ForegroundColor Red
    Write-Host "Asegurate de estar en el directorio raiz del proyecto" -ForegroundColor Yellow
    exit 1
}

# Verificar/crear entorno virtual
if (-Not (Test-Path "venv")) {
    Write-Host "[1/3] Creando entorno virtual..." -ForegroundColor Green
    python -m venv venv
    Write-Host "  Entorno virtual creado exitosamente" -ForegroundColor Gray
    Write-Host ""
} else {
    Write-Host "[1/3] Entorno virtual encontrado" -ForegroundColor Green
}

# Activar entorno virtual
Write-Host "[2/3] Activando entorno virtual..." -ForegroundColor Green
& .\venv\Scripts\Activate.ps1

# Instalar/actualizar dependencias
Write-Host "[3/3] Instalando/actualizando dependencias..." -ForegroundColor Green
Write-Host ""
Write-Host "------------------------------------------------------------" -ForegroundColor DarkGray

pip install -r requirements.txt --upgrade

Write-Host "------------------------------------------------------------" -ForegroundColor DarkGray
Write-Host ""

# Actualizar requirements.txt con las versiones instaladas
Write-Host "Actualizando requirements.txt con versiones instaladas..." -ForegroundColor Green
pip freeze > requirements.txt

# Verificar instalación
$installedPackages = pip list --format=freeze | Measure-Object -Line
$requirementsCount = (Get-Content requirements.txt).Count

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CONFIGURACION COMPLETADA" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Paquetes instalados: $($installedPackages.Lines)" -ForegroundColor Green
Write-Host "  Dependencias en requirements.txt: $requirementsCount" -ForegroundColor Green
Write-Host ""
Write-Host "Ya puedes ejecutar el proyecto:" -ForegroundColor White
Write-Host "  1. Ejecutar scraping: .\run_scraping.ps1" -ForegroundColor Gray
Write-Host "  2. Iniciar servidor: cd tienda_virtual; python manage.py runserver" -ForegroundColor Gray
Write-Host ""
Write-Host "Si actualizaste dependencias, haz commit:" -ForegroundColor Yellow
Write-Host "  git add requirements.txt" -ForegroundColor Gray
Write-Host "  git commit -m 'Actualizar dependencias'" -ForegroundColor Gray
Write-Host "  git push" -ForegroundColor Gray
Write-Host ""
