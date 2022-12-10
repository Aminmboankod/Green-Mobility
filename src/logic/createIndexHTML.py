from createHTML import createFile
from validatorHTML import validatorHTML

def createContentIndex():

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
        <link rel="shorcut icon" type="image/x-icon" href="images/logoPestaña.png" >
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
                <li><a href="pages/listBikeCategory/Roadlist.html">Carretera</a></li>
                <li><a href="pages/listBikeCategory/Citylist.html">Ciudad</a></li>
                <li><a href="pages/listBikeCategory/MTBlist.html">MTB</a></li>
                <li><a>Eléctrica</a>
                    <ul>
                        <li><a href="pages/listBikeCategory/E-Roadlist.html">Carretera</a></li>
                        <li><a href="pages/listBikeCategory/E-Citylist.html">Ciudad</a></li>
                        <li><a href="pages/listBikeCategory/E-MTBlist.html">MTB</a></li>
                    </ul>
                </li>
            </ul>
        </nav>

        
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

        <video src="videos/ciclismo_montaña.mp4" autoplay muted></video>

        <section class="Marcas">

            <h2>¿Tienes alguna marca preferida?</h2>

            <div class="MarcasDeBicis">

                <button role="link" onclick="window.location='pages/listBikeBrand/Bianchilist.html'">
                    <span>Bianchi</span>
                </button>

                <button role="link" onclick="window.location='pages/listBikeBrand/BHlist.html'">
                    <span>BH</span>
                </button>

                <button role="link" onclick="window.location='pages/listBikeBrand/Cannondalelist.html'">
                    <span>Cannondale</span>
                </button>

                <button role="link" onclick="window.location='pages/listBikeBrand/Canyonlist.html'">
                    <span>Canyon</span>
                </button>

                <button role="link" onclick="window.location='pages/listBikeBrand/Cubelist.html'">
                    <span>Cube</span>
                </button>

                <button role="link" onclick="window.location='pages/listBikeBrand/Giantlist.html'">
                    <span>Giant</span>
                </button>

            </div>
            
        </section>
        
        <section class="DondeEstamos">

            <h2>¿Dónde estamos?</h2>

            <p>Nuestras bicicletas están en diferentes puntos de Mallorca:</p>

            <ol>
                <li class="Localidad">Palma 
                    <ul>
                        <li>Mallorca Mobility</li>
                        <li>Ride Mallorca</li>
                        <li>Bike Palma</li>
                    </ul>
                </li>
                <li class="Localidad">Manacor
                    <ul>
                        <li>First Bike</li>
                    </ul>
                </li>
                <li class="Localidad">Alcúdia
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
                    <a href="https://twitter.com/GreenMobilityAS" target="_blank"><img src="images/twitter.png" alt="twitter Logo"></a>
                </div>

                <ul class="list-inline">
                    <li class="list-inline-item"><a href="pages/contact.html">Contacto</a></li>
                </ul>

            <p class="copyright">Green Mobility 2022</p>

            </footer> 
        </div>  
    </body>
</html>     
'''  

  
    directory = "docs/"                         #variable asigna directorio donde crear el archivo
    file = "index"                              #variable asigna nombre de archivo
    extension = ".html"                         #variable asigna extensión de archivo
    path =  directory + file + extension

    createFile(file + extension, contentOfIndex, directory, path)

    validatorHTML(contentOfIndex)

createContentIndex()