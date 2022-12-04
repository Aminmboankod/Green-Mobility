from createHTML import createFile               #Importamos módulo para después de haber generado el contenido crear el archivo

def listofBikesForBrand(dictionaryBikes, brand):

    contentList = '''
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
        <title> List - Mobility </title>
        <!-- Logo de la pestaña del navegador -->
        <link rel="shorcut icon" type="image/x-icon" href="/docs/images/logoPestaña.png" >
        <!-- Hojas CSS -->
        <link rel="stylesheet" type="text/css" href="../css/commonCSS.css"> 
        <link rel="stylesheet" type="text/css" href="../css/bikelist.css">
    </head>

    <body>

        <header>
            <img src="../images/banner.png" alt="Green Mobility banner">
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
            
            <h1 id="title">Listado de bicicletas</h1>
            <hr>'''
    for bike in dictionaryBikes:
        for property in bike:
            if property['category'] == brand :
                
                    contentList +='''
            <div id="articles">
                <button>
                    <span id="topbutton">
                        {name}
                    </span>
                    <span>
                        <picture>
                            <img src="{image}" alt="bicicleta">
                        </picture>
                    </span>
                    <span class="formatnamecategory">
                        <span class="namecompany"></span>
                        <span class="categoryorbrand">{brand}</span>
                    </span>
                    <span class="price">{price}€/day</span>
                </button>
                '''.format( name = bike['name'], image = bike['image'], brand = bike['brand'], price = bike['price'])    #Añadimos los valores que necesitamos a nuestra plantilla HTML
                

                    contentList +='''
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
</html>'''
                            
                    directory = "docs/pages/"          #variable asigna directorio donde crear el archivo
                    file = brand +"list"                   #variable asigna nombre de archivo
                    extension = ".html"                #variable asigna extensión de archivo
                    path =  directory + file + extension

                    createFile(file + extension, contentList, directory, path) 