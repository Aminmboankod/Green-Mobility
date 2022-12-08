from logic.createHTML import createFile


def createContentContact():

    contentOfContact = '''
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
        <title>Contact - Green Mobility</title>
        <!-- Logo de la pestaña del navegador -->
        <link rel="shorcut icon" type="image/x-icon" href="/docs/images/logoPestaña.png" >
        <!-- Hojas CSS -->
        <link rel="stylesheet" type="text/css" href="../css/commonCSS.css"> 
        <link rel="stylesheet" type="text/css" href="../css/contact.css">
    </head>

<body>

    <header>
        <a href="../index.html"><img src="../images/banner.png" alt="Green Mobility logo"></a>
    </header>

    <nav>
        <ul>
            <li><a href="pages/BikeList.html">Carretera</a></li>
            <li><a href="pages/BikeList.html">Ciudad</a></li>
            <li><a href="pages/BikeList.html">MTB</a></li>
            <li><a href="pages/BikeList.html">Eléctricas</a>
                <ul>
                    <li><a href="pages/BikeList.html">Carretera</a></li>
                    <li><a href="pages/BikeList.html">Ciudad</a></li>
                    <li><a href="pages/BikeList.html">MTB</a></li>
                </ul>
            </li>
        </ul>
    </nav>

    <section class="flex-container">

        <form action="" method="get">
            
            <fieldset class="formulario">
                
                <legend class="legend">Formulario de contacto</legend>
                
                <fieldset class="DatosPersonales">
                    <legend>Datos personales </legend>
                    
                    <label for="NombreYApellidos">Nombre y apellidos:</label>
                    <input type="text" name="Nombre y apellidos" id="NombreYApellidos" required> <br>
                
                    <label for="direccion">Dirección:</label>
                    <input type="text" name="Direccion" id="direccion" value="C/De la abundacia, 1." required> <br>
                
                    <label for="email">Email:</label>
                    <input type="tel" name="Email" id="email" required> <br>
                
                </fieldset>
                
                <fieldset class="InformacionAdicional">
                    
                    <legend class="legend">Información</legend>      
                
                <label for="descripcion"> Descripción </label> <br>
                <textarea id="descripcion" name="Descripción" maxlength="200"> Escribe aquí más detalles </textarea>
               
                </fieldset>
                <div class="botones">
                    <input type="submit" value="Enviar formulario">
                    <input type="reset" value="Restablecer formulario">
                </div>
            </fieldset>
        </form>

    </section>


    <div class="footer-basic">
        <footer>

            <div class="social">
                <a href="https://www.instagram.com/green_mobility_/ " target="_blank"><img src="../images/instagram.png" alt="Instagram Logo"></a>
                <a href="https://github.com/Aminmboankod/Green-Mobility" target="_blank"><img src="../images/github.png" alt="GitHub Logo"></a>
                <a href="https://twitter.com/GreenMobilityAS" target="_blank"><img src="../images/twitter.png" alt="twitter Logo"></a>
            </div>

            <ul class="list-inline">
                <li class="list-inline-item"><a href="contact.html">Contacto</a></li>
            </ul>

        <p class="copyright">Green Mobility 2022</p>

        </footer> 
    </div> 
    
</body>
</html>'''

    directory = "docs/pages/"                   #variable asigna directorio donde crear el archivo
    file = "contact"                            #variable asigna nombre de archivo
    extension = ".html"                         #variable asigna extensión de archivo
    path =  directory + file + extension

    createFile(file + extension, contentOfContact, directory, path) 