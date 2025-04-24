<h1 align="center">¡Bienvenidos, somos SellPhones</h1>
<p align="center">
<a href="[https://kasroudra.github.io/](https://github.com/HenriqueAlvarado/Avance_Proyecto_DevOps)" target="_blank"><img align="center" src="[https://github.com/KasRoudra/kasroudra.github.io/raw/main/icons/android-512x512.png](https://www.google.com/url?sa=i&url=https%3A%2F%2Fsupport.apple.com%2Fes-mx%2F121032&psig=AOvVaw0VdMMqa-UYKf4WhEtNTZYD&ust=1745539483638000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCODPsbiv74wDFQAAAAAdAAAAABAE)" alt="SellPhone Logo" height="100" width="100"></a>
</p>
<h3 align="center">SellPhones: Conecta con lo mejor</h3>
<h2 align="center"><u>¿Por qué elegir SellPhones?</u></h2>
<p align="center">

 - 📱 Amplia variedad de modelos: Desde los últimos lanzamientos hasta opciones económicas, encuentra el celular perfecto para ti.
 
 - 💰 Precios competitivos: Ofertas irresistibles y descuentos especiales todo el año.

 - ⚡ Compra rápida y segura: Plataforma intuitiva, métodos de pago confiables y protección al comprador.

 - 🚚 Envío rápido a todo el país: Recibe tu celular en la puerta de tu casa en tiempo récord.
 
 - 🛠️ Garantía en todos los equipos: Tranquilidad asegurada con cobertura ante cualquier inconveniente.

 - 👨‍💻 Atención al cliente personalizada: Nuestro equipo está listo para ayudarte antes, durante y después de tu compra.

</p>

<h2 align="center"><u>Roles del Equipo</u></h2>

| Name                  | Description                                                |
| ---------------------------------|--------------------------------------------------------------- |
| _[Henrique Alvarado: Dev Infraestructura](https://github.com/HenriqueAlvarado)_            | Encargado de diseñar y desplegar toda la infraestructura del proyecto mediante Terraform, asegurando entornos eficientes, escalables y seguros para su funcionamiento.            |
| _[Jorge Marroquín: Dev QA](https://github.com/Eliuddd)_                          | Responsable de integrar correctamente la base de datos con el backend, garantizando la calidad del sistema mediante pruebas y validaciones que aseguren su correcto desempeño.     |
| _[Eros Palma: Ingeniero en software](https://github.com/erospalma)_                  | Apoya en el desarrollo de scripts en Python y en la construcción del frontend, contribuyendo a crear una experiencia de usuario funcional, fluida y visualmente atractiva. 
| _[Juan Espinoza: Ingeniero en software](https://github.com/erospalma)_                  | Especializado en el desarrollo de scripts en Python y en su integración con la base de datos, asegurando que los procesos internos del sistema funcionen correctamente y sin errores.            |

<h4 align="center">Diagrama de Lucid</h4>

<h2 align="center"><u>Infraestructura de nuestro proyecto</u></h2>
<p align="center">
  <img src="Infraestructura (2).png" alt="Infraestructura del proyecto" width="600">
</p>

<h2 align="center"><u>Infraestructura de nuestro proyecto</u></h2>

<p align="center">
  <img src="Infraestructura (2).png" alt="Infraestructura del proyecto" width="600">
</p>

<h3 align="center">Descripción de Nuestra Arquitectura en AWS</h3>
<p>
  En este proyecto, diseñamos una arquitectura en AWS que combina seguridad, segmentación de red y acceso controlado a la base de datos. Toda la infraestructura se encuentra dentro de una VPC con el rango de IPs 10.10.0.0/20, desplegada en una sola zona de disponibilidad.
</p>

<h3 align="center">🌐 Subred Pública (10.10.0.0/24)</h3>
<ul>
  <li>Desplegamos una instancia EC2 configurada como Linux Jump Server.</li>
  <li>Este servidor actúa como punto de entrada a la infraestructura.</li>
  <li>Un Security Group permite conexiones SSH (puerto 22) desde el exterior para administración segura.</li>
</ul>

<h3 align="center">🔒 Subred Privada</h3>
<ul>
  <li>Contiene un Linux Web Server inaccesible directamente desde Internet.</li>
  <li>Solo se puede acceder a él vía SSH a través del Jump Server.</li>
  <li>Este servidor realiza operaciones sobre la base de datos y es el único autorizado para comunicarse con Amazon DynamoDB.</li>
</ul>

<h3 align="center">🗃️ Acceso a DynamoDB</h3>
<ul>
  <li>DynamoDB está fuera de la VPC como servicio gestionado por AWS.</li>
  <li>El servidor web se conecta mediante un IAM Role, evitando el uso de claves estáticas.</li>
  <li>Esto garantiza una conexión segura y escalable.</li>
</ul>




### I've little contribution in:

<a href="https://github.com/htr-tech/zphisher">Zphisher  <img src="https://img.shields.io/github/stars/htr-tech/zphisher.svg?style=social&label=Star&maxAge=2592000"> </a>

<a href="https://github.com/rajkumardusad/Tool-X">Tool-X  <img src="https://img.shields.io/github/stars/rajkumardusad/Tool-X.svg?style=social&label=Star&maxAge=2592000"> </a>

<a href="https://github.com/ashutosh1919/masterPortfolio">masterPortfolio  <img src="https://img.shields.io/github/stars/ashutosh1919/masterPortfolio.svg?style=social&label=Star&maxAge=2592000"> </a>

<a href="https://github.com/rajkumardusad/onex">Onex  <img src="https://img.shields.io/github/stars/rajkumardusad/onex.svg?style=social&label=Star&maxAge=2592000"> </a>

<a href="https://github.com/coderjojo/creative-profile-readme">Creative Profile Readme  <img src="https://img.shields.io/github/stars/coderjojo/creative-profile-readme.svg?style=social&label=Star&maxAge=2592000"> </a>

<a href="https://github.com/jaykali/maskphish">MaskPhish  <img src="https://img.shields.io/github/stars/jaykali/maskphish.svg?style=social&label=Star&maxAge=2592000"> </a>

<a href="https://github.com/durgeshsamariya/awesome-github-profile-readme-templates">Awesome Github Profile Readme Templates  <img src="https://img.shields.io/github/stars/durgeshsamariya/awesome-github-profile-readme-templates.svg?style=social&label=Star&maxAge=2592000"> </a>

### Contact me:

<a href="https://github.com/KasRoudra" target="_blank"><img src="https://img.shields.io/badge/Github-KasRoudra-green?style=for-the-badge&logo=github"></a>

<a href="https://facebook.com/KasRoudra" target="_blank"><img src="https://img.shields.io/badge/FaceBook-KasRoudra-purple?style=for-the-badge&logo=facebook"></a>

<a href="https://m.me/KasRoudra" target="_blank"><img src="https://img.shields.io/badge/Messenger-KasRoudra-red?style=for-the-badge&logo=messenger"></a>

<a href="mailto:kasroudrakrd@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Email-kasroudrakrd@gmail.com-teal?style=for-the-badge&logo=gmail"></a>

------
Credit: [KasRoudra](https://github.com/KasRoudra)

Last Edited on: 12/12/2021
