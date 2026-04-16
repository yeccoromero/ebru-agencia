# Bitácora de Proyecto

## [2026-04-15]
**Contexto:** El plan de implementación original proponía usar Next.js (App Router) basado en las reglas globales por defecto para aplicaciones web.
**Problema:** Al intentar inicializar el proyecto (`npx create-next-app`), el sistema arrojó error `command not found: npx`. Node.js no está instalado o disponible en este entorno.
**Fix:** Pivotar el proyecto a un stack de **HTML/CSS/JS puro (Vanilla)**. Para un portafolio estático, esto cumple igualmente con los requisitos de alto rendimiento, SEO y control milimétrico de la UI, sin necesidad de dependencias externas.
**Lección:** Next time: Always verify toolchain (Node/npm) availability before proposing and committing to framework-dependent architectural plans.
## [2026-04-15]
Context: El usuario solicitó cambiar las imágenes generadas por IA de los portafolios en el home por las reales de la marca.
Decision: Revertir las URL de `cover-render.png` a `extracted-images/slide_01.jpg` en el `index.html`.
Problem: Se generaron imágenes con IA asumiendo que el usuario quería renders hiperrealistas para las asimetrías de su grid en proyectos que carecían de Mockups, cuando prefieren 100% el trabajo original plasmado en el PDF.
Fix: Se eliminaron las referencias a las imágenes creadas con IA y se estandarizó `slide_01.jpg` como imagen de portada para todas las tarjetas.
Lesson: Next time: Never generate synthetic placeholder images for a portfolio unless explicitly instructed to create *fake* mockups; portfolios must exclusively showcase the client's genuine work as present in the source files.



## [2026-04-15] 2nd Update
Context: El usuario indicó que la Diapositiva 1 del PDF (Slide 01) generalmente no es un render real y que debía escogerse una imagen de la presentación que muestre la marca de forma 'real' (Mockup / Aplicación).
Decision: Utilicé un análisis de datos sobre el tamaño de archivo de las imágenes extraídas (las imágenes con textura fotográfica/renders pesan entre 2MB - 3MB, frente a los 100KB de un vector plano). Con esto identifiqué exactamente qué slide contenía la foto/render más detallado para Vixmed, Lulas, La Sazón, etc.
Problem: Asumí erróneamente que la diapositiva 1 era la portada definitiva, cuando a nivel de diseño corporativo ese rol recae en el Mockup Real (aplicación).
Fix: Actualicé el `index.html` asignando dinámicamente las slides con mayor peso de datos (ej: Vixmed usó slide_14, Lulas usó slide_11) para garantizar que la miniatura de la card sea fotográfica.
Lesson: Next time: Never use 'slide 01' by default for portfolio thumbnails; filter the raw extracted media to prioritize files with heavy pixel density (photographic mockups) to represent the project's real-world application.

## [2026-04-15] 3rd Update
Context: El usuario reportó que el Bento Grid continuaba teniendo enormes espacios vacíos negros en la página de Inicio a pesar de las adiciones CSS.
Decision: Analicé el orden en el DOM de las tarjetas (`index.html`).
Problem: Asumí que `grid-auto-flow: row dense;` resolvería algorítmicamente cualquier desorden espacial, pero introduje en el HTML el proyecto 'Samay' (12 columnas) justo después de 'Pilot's Cafe' (5 columnas), arrastrando a 'Samay' hacia la siguiente fila y dejando a 'Pilot's Cafe' solo, con un hoyo de 7 columnas que el navegador no empalmó bien.
Fix: Modifiqué directamente el HTML (`index.html`) alterando el orden de las tarjetas para colocar a 'Swipe' (7 columnas) explícitamente pegado a 'Pilot\'s Cafe' (5 columnas). Así, el DOM suma nativamente 12 columnas exactas fila a fila sin delegar responsabilidad al motor del navegador.
Lesson: Next time: Never rely entirely on CSS `row dense` to fix asymmetric bento grids; mathematically sequence the DOM elements so that complimentary cards (like spans 5+7) always sit consecutively.

## [2026-04-15] 4th Update (Bugfix)
Context: El usuario indicó que la foto de la sección About no cargaba.
Decision: Analizar el directorio `assets/img` para verificar nombres.
Problem: El código estaba esperando el nombre `profile.jpg`, pero el archivo fue guardado con el nombre nativo de la cámara (`IMG_0304.JPG`).
Fix: Enruté la etiqueta `<img>` en el `index.html` directamente hacia su archivo `IMG_0304.JPG`.
Lesson: Next time: Never rely on users to manually rename their image assets to match hardcoded developer strings; always scan the directory and map the code to match whatever original raw file the user loads.

## [2026-04-15] 5th Update (Bugfix)
Context: El usuario indicó que los textos internos de los proyectos no se estaban traduciendo al hacer clic en el toggle ES/EN.
Decision: Analicé el HTML interno de las páginas de proyecto como `lulas.html` y `catleya-cafeteria.html`.
Problem: Mi generador automático de atributos i18n buscaba 'strings' literales y exactos para inyectarse (ej: `replace('<p>Una marca que entiende...', ...)`), pero en el HTML real esos textos contenían tags extra como `<strong>` o espacios extra que impedían el 'match', dejando los textos invisibles para el traductor.
Fix: Reescribí la lógica usando Expresiones Regulares (Regex) para encontrar la primera etiqueta `<p>` hija del contenedor `project-description` en las 11 páginas simultáneamente e inyectarle el atributo `data-i18n` correcto ignorando qué texto de relleno contengan.
Lesson: Next time: Never rely on exact string-matching code replacements when injecting attributes globally onto dynamic text blocks; use structural Regex targeting or proper DOM parsing to ensure bindings stick.

## [2026-04-15] 6th Update (Bugfix)
Context: El usuario notó que al traducir al inglés, los párrafos no se reemplazaban, sino que aumentaban y se hacían larguísimos.
Decision: Analicé las llaves del diccionario JS (`i18n.js`).
Problem: En la lista de traducciones al inglés (`en:`), el JSON original que generé contenía tanto el texto en español como la frase '(Translated: ...)' en un mismo string para todos los proyectos, por lo que estéticamente daba la impresión de inyectar párrafos clonados al cambiar al modo EN.
Fix: Limpié el diccionario interno en `i18n.js`, eliminando los prefijos en español de las llaves en inglés para que la sustitución sea completamente pura e impecable, reemplazando un texto por el otro.
Lesson: Next time: Double check JSON dictionary payloads to ensure translation literals are completely disjointed and free of debugging tags before committing them to the frontend state.

## [2026-04-15] 7th Update (Bugfix)
Context: El usuario reportó que páginas específicas (como Vixmed y Cattleya) traducían solo la mitad de la pantalla, dejando los segundos párrafos y footers colgados en español.
Decision: Inspección visual a fondo de los documentos tempranos.
Problem: Los proyectos más viejos tenían una estructura rica de múltiples párrafos en HTML (separados por `<br>` y varios `<p>`). Mi motor de traducción inicial usando Regex solo escaneaba el *primer* renglón aislando a los demás.
Fix: Agregué llaves secundarias explicitas (`vixmed.desc2`, `catleya.desc2`, `project.year`, `project.next`) al HTML y reconstruí el diccionario.
Lesson: Next time: Complex data objects generated at different project stages have morphological discrepancies. Translation engines must account for multiple paragraph objects (`<p>`), not just default to index [0].
