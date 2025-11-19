# Script para ejecutar el scraping de productos Herbalife
# Autor: Equipo Natursur
# Fecha: Noviembre 2025

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  SCRAPING DE PRODUCTOS HERBALIFE" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar que estamos en el directorio correcto
if (-Not (Test-Path "tienda_virtual")) {
    Write-Host "ERROR: No se encuentra el directorio 'tienda_virtual'" -ForegroundColor Red
    Write-Host "Asegurate de ejecutar este script desde la raiz del proyecto" -ForegroundColor Yellow
    exit 1
}

# Verificar que el entorno virtual existe
if (-Not (Test-Path "venv")) {
    Write-Host "ERROR: No se encuentra el entorno virtual 'venv'" -ForegroundColor Red
    Write-Host "Ejecuta primero: python -m venv venv" -ForegroundColor Yellow
    exit 1
}

# Activar entorno virtual
Write-Host "[1/4] Activando entorno virtual..." -ForegroundColor Green
& .\venv\Scripts\Activate.ps1

# Verificar que selenium está instalado
Write-Host "[2/4] Verificando dependencias..." -ForegroundColor Green
$seleniumInstalled = python -c "import selenium; print('OK')" 2>$null

if ($seleniumInstalled -ne "OK") {
    Write-Host "  Instalando Selenium..." -ForegroundColor Yellow
    pip install selenium --quiet
}

# Cambiar al directorio de Django
Write-Host "[3/4] Preparando scraping..." -ForegroundColor Green
Set-Location tienda_virtual

# Ejecutar el scraping
Write-Host "[4/4] Ejecutando scraping (esto puede tardar 2-3 minutos)..." -ForegroundColor Green
Write-Host ""
Write-Host "------------------------------------------------------------" -ForegroundColor DarkGray

python manage.py scrape_herbalife

Write-Host "------------------------------------------------------------" -ForegroundColor DarkGray
Write-Host ""

# Mostrar resumen
Write-Host "Verificando resultados..." -ForegroundColor Green
$totalProductos = python manage.py shell -c "from home.models import Product; print(Product.objects.count())" 2>$null

if ($totalProductos) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "  SCRAPING COMPLETADO EXITOSAMENTE" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  Total de productos en la BD: $totalProductos" -ForegroundColor Green
    Write-Host ""
    Write-Host "Los productos ya estan disponibles en:" -ForegroundColor White
    Write-Host "  - Pagina de inicio (3 productos destacados)" -ForegroundColor Gray
    Write-Host "  - /products/ (listado completo)" -ForegroundColor Gray
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "ADVERTENCIA: No se pudieron contar los productos" -ForegroundColor Yellow
    Write-Host "Revisa los mensajes anteriores para detectar errores" -ForegroundColor Yellow
    Write-Host ""
}

# Volver al directorio raíz
Set-Location ..

Write-Host "Presiona cualquier tecla para continuar..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
