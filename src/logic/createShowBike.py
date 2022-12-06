from logic.createHTML import createFile

def createShowBike(listOfDictionaryBikes):

    for bike in listOfDictionaryBikes:
        HTMLshowbikes = '''
<!DOCTYPE html>
<html lang="es">
    <head>
        <base target="_self">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content="Amin Mustafa & Antonio Maroto">
        <meta name="description" content="Green Mobility página principal para mostrar bicicletas">
        <meta name="copyright" content="Green Mobility">
        <meta name="generator" content="VS Code">
        <meta name="keywords" content="Bikes, Bicis, Bicicletas, Alquiler, Mallorca, Rent" >
        <title>Bikes - Green Mobility</title>
        <!-- Logo de la pestaña del navegador -->
        <link rel="shorcut icon" type="image/x-icon" href="../images/logoPestaña.png" >
        <!-- Hojas de estilos CSS -->
        <link rel="stylesheet" type="text/css" href="../css/commonCSS.css"> 
        <link rel="stylesheet" type="text/css" href="../css/showBike.css">
    </head>
    
    <body>
        
        <header>
            <a href="../index.html"><img src="../images/banner.png" alt="Green Mobility logo"></a>
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
        <section>
            <div class="one">
                <h1>{name}</h1>
            </div>
        </section>
        <section class="flex-container">
            <div class="imagen">
        
                <img class="imagenBicicleta" src="{image}"  alt="bicicleta" id="Bicicleta">
            </div> '''.format(name = bike["name"], image = bike["image"])

        if bike["available"] == True:
            bike.update({"available":"Disponible"})
        else:
            bike.update({"available":"No disponible"})

        HTMLshowbikes += '''
            <div class="tabla">
                <table>
                    <tr>
                        <th>Categoria</th>
                        <td>{category}</td>
                    </tr>
                    <tr>
                        <th>Marca</th>
                        <td>{brand}</td>
                    </tr>
                    <tr>
                        <th>Material</th>
                        <td>{material}</td>
                    </tr>
                    <tr>
                        <th>Talla</th>
                        <td>{frame_size}</td>
                    </tr>
                    <tr>
                        <th>Peso</th>
                        <td>{weight}</td>
                    </tr>
                    <tr>
                        <th>Tienda</th>
                        <td>{location}</td>
                    </tr>
                    <tr>
                        <th>Disponibilidad</th>
                        <td>{available}</td>
                    </tr>
                    <tr>
                        <th>Precio</th>
                        <td>{price}</td>
                    </tr>
                </table>
            </div>
            
        </section>
        <div class="footer-basic">
            <footer>
                <div class="social">
                    <a href="https://www.instagram.com/green_mobility_/ " target="_blank"><img src="../images/instagram.png" alt="Instagram Logo"></a>
                    <a href="https://github.com/Aminmboankod/Green-Mobility" target="_blank"><img src="../images/github.png" alt="GitHub Logo"></a>
                    <a href="#" target="_blank"><img src="../images/twitter.png" alt="twitter Logo"></a>
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
</html>'''.format(name = bike["name"], category = bike["category"], brand = bike["brand"],material = bike["material"], frame_size = bike["frame_size"], weight = bike["weight"], location = bike["company"]["company_name"], available = bike["available"], price = bike["price"], image = bike["image"])

        name = bike["name"]                #Variable asigna el nombre de la bici
        directory = "docs/pages/"          #variable asigna directorio donde crear el archivo
        file = name.replace(" ","")                        #variable asigna nombre de archivo
        extension = ".html"                #variable asigna extensión de archivo
        path =  directory + file + extension

        createFile(file + extension, HTMLshowbikes, directory, path) 