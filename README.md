*imagen app api web: <img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/029854af-e123-4216-a28f-5a31931bb1b6" />

*subido a servidor: (RENDER.COM) https://dashboard.render.com/web/srv-d1s4c5p5pdvs73aduf4g/deploys/dep-d1s4c615pdvs73adufng?r=2025-07-17%4000%3A37%3A49%7E2025-07-17%4000%3A41%3A35 
USR RENDER -> GITHUB -> USR: JCHMKY _ E:FIUBA AR

*HECHO CON REPLIT.COM para no consumir recuros ram procesador PC
https://replit.com/@iaroskarel/api-mercado-flask#templates/index.html

🚀 Gracias por visitar este proyecto
Hecho con ❤️ para aprender cómo hacer una API web sencilla usando Flask, PokéAPI y Render.


------------------------------------------------- MAS DETALLES -----------------------------------------------------------------------------------------------
🌐 PokéAPI Flask - App con Flask + Render
Una pequeña aplicación web hecha con Python y Flask que consulta datos desde la PokéAPI. Permite ingresar el nombre de un Pokémon y ver información en pantalla (próximamente imagen y tipo).

🚀 ¿Dónde está online?
La app está desplegada gratis en Render.com:
🔗 https://api-flask-python-replit-colab-online-nopc.onrender.com


🔧 ¿Cómo funciona Render?
Usamos Render.com para publicar gratis la app.

Se conecta automáticamente con este repositorio de GitHub.

Cada vez que hacés git push, Render actualiza la app.

🕐 ¿Por qué a veces tarda en cargar?
Render apaga el servidor si nadie visita la app por 15 minutos.

Cuando alguien entra, se despierta y tarda unos 30 a 50 segundos en cargar la primera vez.

⚠️ Modo desarrollo vs producción
Actualmente la app corre con:

bash
python main.py
Lo cual es válido para pruebas.
Para producción se recomienda usar gunicorn, por ejemplo:

bash
gunicorn main:app
Pero para aprender y practicar, la configuración actual es perfecta. 💪

🔄 ¿Cómo actualizo la app?
Hacés cambios en tu código local.

Luego:

bash

git add .
git commit -m "Tu mensaje"
git push
Render detecta el cambio automáticamente y vuelve a desplegar la app.

---------------------------------------------------------------------------------------------------------------------------------------------------------

# 🌐 PokéAPI Flask - App con Flask + Render

Una aplicación web hecha con **Python + Flask** que permite consultar información de un Pokémon usando la PokéAPI. Ingresás un nombre y se muestra información (tipo, etc).

---

## 🔗 Link en línea

➡️ La app está funcionando online gracias a Render.com:  
🌍 https://api-flask-python-replit-colab-online-nopc.onrender.com

---

## ⚙️ Despliegue (Deploy) con Render

Render se encarga de instalar dependencias, ejecutar tu app y mantenerla online (gratis).  
Podés ver los detalles del despliegue aquí:  
📄 [Render Deploy Dashboard](https://dashboard.render.com/web/srv-d1s4c5p5pdvs73aduf4g/deploys/dep-d1s4c615pdvs73adufng)

---

## 🕒 ¿Por qué a veces tarda en cargar?

Render en su versión gratuita “duerme” tu app después de **15 minutos de inactividad**.  
Cuando alguien entra de nuevo, Render necesita **30 a 50 segundos** para despertarla y levantar el servidor.  
Es completamente normal.

---

## ⚠️ Desarrollo vs Producción

Actualmente la app se ejecuta con:

```bash
python main.py

----------------------------------------------------------------------------------------------
# 🌐 PokéAPI Flask – Consulta Pokémon con Flask y PokéAPI

Una aplicación web hecha con **Python + Flask** que permite consultar información de un Pokémon usando la [PokéAPI](https://pokeapi.co/). Ingresás un nombre y se muestra información como su tipo, estadísticas, etc.

---

## 🔗 Link en línea

➡️ La app está funcionando online gratis gracias a Render:  
🌍 https://api-flask-python-replit-colab-online-nopc.onrender.com

---

## ⚙️ Despliegue con Render

Render se encarga de instalar dependencias, ejecutar tu app y mantenerla online.  
📄 Ver el último despliegue:  
👉 [Render Deploy Dashboard](https://dashboard.render.com/web/srv-d1s4c5p5pdvs73aduf4g/deploys/dep-d1s4c615pdvs73adufng)

---

## 🕒 ¿Por qué a veces tarda en cargar?

Render, en su versión gratuita, pone tu aplicación en "modo suspensión" si no recibe visitas durante unos **15 minutos**.  
Cuando alguien vuelve a entrar, el servidor puede tardar entre **30 y 50 segundos** en "despertar".  
Esto es normal y no es un error.

---

## ⚠️ Modo desarrollo vs producción

Actualmente se ejecuta con:

```bash
python main.py

----------------------------------------------------------------------

gunicorn main:app
¿Qué es Gunicorn?
Es una herramienta que corre apps Python como Flask en modo producción.

Es más rápida y segura.

Soporta múltiples usuarios a la vez.

Se usa junto con un servidor como Nginx.


-----------------------------------------------------------------------------------

🛠️ Tecnologías usadas
Python 3

Flask

PokéAPI

HTML / CSS básico

Render (para hosting)

Git / GitHub (para versionado)

----------------------------------------------------------------------------------
🚧 Próximas mejoras
Mostrar imagen del Pokémon.

Manejo de errores si el nombre está mal escrito.

Mejorar diseño con CSS.

Agregar loading o animación de espera.

Usar Gunicorn para producción.

--------------------------------------------------------------------------------
✨ Créditos
Desarrollado como parte del curso de introducción a APIs y servidores Flask con Render.
Inspirado por la comunidad Python y el entusiasmo por aprender a crear proyectos reales.
