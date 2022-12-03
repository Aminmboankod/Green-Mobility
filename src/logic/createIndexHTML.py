

def createIndexHTML():

    contentOfIndex = '''
<!DOCTYPE html>

<html lang="en">

    <head>
        <base target="_self">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content="Amin Mustafa & Antonio Maroto">
        <meta name="description" content="Green Mobility página principal para mostrar bicicletas">
        <meta name="copyright" content="Green Mobility">
        <meta name="generator" content="VS Code">
        <meta name="keywords" content="Bikes, Bicis, Bicicletas, Alquiler, Mallorca, Rent" >
        <title>Green Mobility</title>
        <!-- Logo de la pestaña del navegador -->
        <link rel="shorcut icon" type="image/x-icon" href="/docs/images/logoPestaña.png" >
        <!-- Hojas CSS -->
        <link rel="stylesheet" type="text/css" href="css/commonCSS.css"> 
        <link rel="stylesheet" type="text/css" href="css/index.css">
    </head>

    <body>

        <header>
            <img src="images/banner.png" alt="Green Mobility banner">
        </header>

        <nav>
            <ul>
                <li><a href="/docs/pages/list.html">Carretera</a></li>
                <li><a href="/docs/pages/list.html">Ciudad</a></li>
                <li><a href="/docs/pages/list.html">MTB</a></li>
                <li><a href="/docs/pages/list.html">Eléctricas</a>
                    <ul>
                        <li><a href="/pages/list.html">Carretera</a></li>
                        <li><a href="/pages/list.html">Ciudad</a></li>
                        <li><a href="/pages/list.html">MTB</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
                -------------------------------------------------------------------------
        
        <div class="imageContainer">
            
        <h1 class="text">¡El primer buscador <br>
        de bicicletas de alquiler <br>
        de Mallorca!</h1>

        <img class="image" src="images/bikeMallorca.png" alt="Bicicleta frente catedral de Mallorca">

        </div>

        <section class="QuienesSomos">

            <h2>¿Quiénes somos?</h2>

            <p>¿Nunca te has planteado alquilar una bici en Mallorca? Eso es porque aún no conoces todas sus ventajas. Visitar tus rincones favoritos de la ciudad en una bicis es la manera más ràpida, cómoda y mágica de conocer o redescubrir su esencia más auténtica. Mallorca y las bicicletas forman un binomio que parece compuesto de manera natural. Descarta la posibilidad de caminar pasivamente por sus espectaculares calles y de reducir el número y la intensidad de las sensaciones al encerrarte en un vehículo con puertas. Con el alquiler de bicicletas, tu visión de la ciudad cambiará, descubrirás lugares inaccesibles para otros, porque la bici no te lleva, la conduces hacia un mundo de aventura.</p>
        
        </section>
        
        <section class="DondeEstamos">

            <h3>¿Dónde estamos?</h3>

            <p>Nos puedes encontrar en diferentes puntos de Mallorca. Tenemos a tu disposición tiendas en:</p>

            <ol>
                <li class="Palma">Palma
                    <ul>
                        <li>Mallorca Mobility</li>
                        <li>Ride Mallorca</li>
                        <li>Bike Palma</li>
                    </ul>
                </li>
                <li>Manacor
                    <ul>
                        <li>First Bike</li>
                    </ul>
                </li>
                <li>Alcúdia
                    <ul>
                        <li>Haste Mobility</li>
                    </ul>
                </li>
            </ol>

        </section>
        
        <div class="footer-basic">
            <footer>

                <div class="social">
                    <a href="https://www.instagram.com/green_mobility_/ " target="_blank"><img src="images/instagram.png" alt="Instagram Logo"></a>
                    <a href="https://github.com/Aminmboankod/Green-Mobility" target="_blank"><img src="images/github.png" alt="GitHub Logo"></a>
                    <a href="#" target="_blank"><img src="images/twitter.png" alt="twitter Logo"></a>
                </div>

                <ul class="list-inline">
                    <li class="list-inline-item"><a href="#">Términos y condiciones</a></li>
                    <li class="list-inline-item"><a href="#">Aviso Legal</a></li>
                    <li class="list-inline-item"><a href="#">Política de privacidad</a></li>
                </ul>

            <p class="copyright">Green Mobility 2022</p>

            </footer> 
        </div>  

    </body>
</html>

    '''

    # El W+ sirve para que: Si no existe el documento lo crea y escribe.
    # Si existe pero esta vacío escribe dentro
    # Y si existe y está escrito dentro lo sobreescribe
    htmlFile = open("docs/" + "index" + ".html", "w+")
    htmlFile.write(contentOfIndex)
    print("docs/" + ".html" + "has been created")

createIndexHTML()