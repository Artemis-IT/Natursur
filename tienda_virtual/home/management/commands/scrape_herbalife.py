"""
Comando de gestión Django para scrapear productos de Herbalife y guardarlos en la BD.

Uso:
    python manage.py scrape_herbalife [--max-clicks=10] [--clear]

Opciones:
    --max-clicks: Número máximo de veces que se hace clic en 'Carga más' (default: 10)
    --clear: Borra todos los productos existentes antes de scrapear
"""

from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from home.models import Product


class Command(BaseCommand):
    help = 'Scrapea productos de Herbalife y los guarda en la base de datos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--max-clicks',
            type=int,
            default=10,
            help='Número máximo de veces que se hace clic en "Carga más" (default: 10)'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Borra todos los productos existentes antes de scrapear'
        )
        parser.add_argument(
            '--debug',
            action='store_true',
            help='Muestra información de depuración detallada'
        )

    def handle(self, *args, **options):
        max_clicks = options['max_clicks']
        clear_existing = options['clear']
        debug = options.get('debug', False)

        if clear_existing:
            count = Product.objects.count()
            Product.objects.all().delete()
            self.stdout.write(self.style.WARNING(f'Se eliminaron {count} productos existentes.'))

        self.stdout.write(self.style.SUCCESS('Iniciando scraping de Herbalife...'))

        # Configurar WebDriver
        driver = webdriver.Chrome()
        
        try:
            # Acceder a la página de productos
            url = "https://www.herbalife.com/es-es/u/category/all-products"
            driver.get(url)
            self.stdout.write(f'Navegando a: {url}')
            time.sleep(3)

            # Hacer clic en el botón "Cargar más" repetidamente hasta que no haya más
            clicks = 0
            max_attempts_without_button = 3  # Intentos consecutivos sin encontrar botón antes de parar
            attempts_without_button = 0
            
            while clicks < max_clicks and attempts_without_button < max_attempts_without_button:
                try:
                    # Hacer scroll al final primero para que el botón sea visible
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)
                    
                    # Intentar encontrar el botón varias veces (puede tardar en aparecer)
                    load_more = None
                    for attempt in range(3):  # 3 intentos para encontrar el botón
                        buttons = driver.find_elements(By.TAG_NAME, 'button')
                        for btn in buttons:
                            btn_text = btn.text.lower().strip()
                            if any(word in btn_text for word in ['cargar', 'load', 'más', 'more', 'ver más', 'mostrar']):
                                try:
                                    if btn.is_displayed() and btn.is_enabled():
                                        load_more = btn
                                        if debug:
                                            self.stdout.write(f'Botón encontrado: "{btn.text}"')
                                        break
                                except:
                                    continue
                        
                        if load_more:
                            break
                        
                        # Si no se encontró en este intento, esperar un poco más
                        if attempt < 2:
                            if debug:
                                self.stdout.write(f'Esperando botón... intento {attempt + 1}/3')
                            time.sleep(2)
                    
                    if load_more:
                        # Scroll hasta el botón
                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", load_more)
                        time.sleep(1)
                        
                        # Contar productos antes del clic
                        productos_antes = len(driver.find_elements(By.XPATH, "//a[contains(@href,'/u/products/')]"))
                        
                        # Intentar hacer clic
                        try:
                            load_more.click()
                        except:
                            driver.execute_script("arguments[0].click();", load_more)
                        
                        clicks += 1
                        attempts_without_button = 0
                        self.stdout.write(f'Clic #{clicks} en botón "Cargar más" - esperando...')
                        
                        # Esperar a que se carguen nuevos productos
                        time.sleep(4)
                        
                        # Verificar si se cargaron productos nuevos
                        productos_despues = len(driver.find_elements(By.XPATH, "//a[contains(@href,'/u/products/')]"))
                        if productos_despues > productos_antes:
                            self.stdout.write(f'  ✓ {productos_despues} productos (+{productos_despues - productos_antes})')
                    else:
                        attempts_without_button += 1
                        self.stdout.write(f'No se encontró botón "Cargar más" ({attempts_without_button}/{max_attempts_without_button})')
                        
                except Exception as e:
                    if debug:
                        self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
                    attempts_without_button += 1
            
            self.stdout.write(f'Finalizó carga: {clicks} clics realizados')
            time.sleep(3)

            # Extraer solo enlaces de productos reales (no categorías)
            items = driver.find_elements(By.XPATH, "//a[contains(@href,'/u/products/')]")
            self.stdout.write(f'Se encontraron {len(items)} enlaces de productos.')

            products_created = 0
            products_updated = 0
            products_skipped = 0

            for item in items:
                try:
                    # Extraer el enlace del producto (item ya es un enlace)
                    enlace = item.get_attribute('href')
                    
                    # Filtrar enlaces de categorías y otros no productos
                    if not enlace or '/u/products/' not in enlace or '/category/' in enlace:
                        products_skipped += 1
                        continue
                    
                    # Extraer nombre del producto
                    nombre = None
                    try:
                        # Primero intentar obtener el texto completo del elemento
                        if item.text and item.text.strip():
                            nombre = item.text.strip()
                        
                        # Si no hay texto o es muy corto, intentar selectores específicos
                        if not nombre or len(nombre) < 3:
                            nombre_selectors = [
                                ".//h3",
                                ".//h4",
                                ".//h2",
                                ".//p[contains(@class,'product')]",
                                ".//*[contains(@class,'product-name')]",
                                ".//*[contains(@class,'product-title')]",
                                ".//*[contains(@class,'title')]",
                                ".//*[@class='name']"
                            ]
                            for selector in nombre_selectors:
                                try:
                                    nombre_elem = item.find_element(By.XPATH, selector)
                                    nombre = nombre_elem.text.strip()
                                    if nombre and len(nombre) > 3:
                                        break
                                except NoSuchElementException:
                                    continue
                        
                        # Si aún no tenemos nombre, usar el enlace como última opción
                        if not nombre or len(nombre) < 3:
                            if enlace:
                                # Extraer el nombre del slug de la URL
                                partes = enlace.split('/')
                                slug = partes[-1] if partes else ''
                                # Limpiar el slug: quitar códigos y convertir guiones en espacios
                                nombre = slug.split('-')[0:-1]  # Quitar el último segmento que suele ser un código
                                nombre = ' '.join(nombre).title() if nombre else slug
                    except Exception as e:
                        if debug:
                            self.stdout.write(self.style.ERROR(f'Error extrayendo nombre: {e}'))
                        pass
                    
                    # Buscar imagen asociada (buscar en el elemento, padre y hermanos)
                    imagen_url = None
                    try:
                        # Estrategia 1: Buscar img dentro del enlace
                        img = item.find_element(By.TAG_NAME, 'img')
                        imagen_url = img.get_attribute('src') or img.get_attribute('data-src') or img.get_attribute('data-lazy-src')
                    except NoSuchElementException:
                        try:
                            # Estrategia 2: Buscar en el elemento padre (div que contiene el enlace)
                            parent = item.find_element(By.XPATH, '..')
                            img = parent.find_element(By.TAG_NAME, 'img')
                            imagen_url = img.get_attribute('src') or img.get_attribute('data-src') or img.get_attribute('data-lazy-src')
                        except NoSuchElementException:
                            try:
                                # Estrategia 3: Buscar hermano anterior (imagen antes del enlace)
                                img = item.find_element(By.XPATH, './preceding-sibling::img')
                                imagen_url = img.get_attribute('src') or img.get_attribute('data-src') or img.get_attribute('data-lazy-src')
                            except NoSuchElementException:
                                pass
                    
                    if debug and imagen_url:
                        self.stdout.write(f'  Imagen encontrada: {imagen_url[:60]}')

                    # Validar que tengamos nombre
                    if not nombre or len(nombre) < 3:
                        if debug:
                            self.stdout.write(self.style.WARNING(f'Omitido (sin nombre): {enlace}'))
                        products_skipped += 1
                        continue

                    # Crear o actualizar producto en la BD
                    product, created = Product.objects.update_or_create(
                        herbalife_url=enlace,
                        defaults={
                            'name': nombre[:200],  # Limitar longitud
                            'image_url': imagen_url,
                            'is_active': True
                        }
                    )

                    if created:
                        products_created += 1
                        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {nombre[:50]}'))
                    else:
                        products_updated += 1

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error procesando producto: {e}'))
                    products_skipped += 1

            # Resultados
            self.stdout.write(self.style.SUCCESS(f'\n✓ Scraping completado:'))
            self.stdout.write(f'  - Productos creados: {products_created}')
            self.stdout.write(f'  - Productos actualizados: {products_updated}')
            self.stdout.write(f'  - Productos omitidos: {products_skipped}')
            self.stdout.write(f'  - Total en BD: {Product.objects.count()}')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error durante el scraping: {e}'))
        
        finally:
            driver.quit()
            self.stdout.write('WebDriver cerrado.')
