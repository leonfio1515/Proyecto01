ruta raiz:
localhost:8000
ruta admin:
localhost:8000/admin


usuario administrador - staff
user: admin
pass: 1234

usuario comun
user: local1
pass: user1234

Vista inicio.
Tanto para el usuario Admin, como para el Local1,
se vera una seccion de Cards con informacion relevante a la tarea o al personal.
Podran encontrar una seccion de Promociones, y otra de Noticias

Vista de inicio desde usuario "Local1"
"Pedidos Formularios".
	Distintos modulos usados para solicitar insumos desde los puntos de venta hacia administracion

"Cajas"
	"Manuales"- documentacion de apollo e informacion relevante a la tarea
	"Calculo descuento"-"Cotiza orden"- 	Son formularios auxiliares de calculo de procesos
	"Orden sin cotizar"-"Calcula disponible" (renderisa en un nuevo template con la informacion necesaria)

"Doc impresion"
	Son distintos formularios con el unico proposito de completar informacion e imprimir.
	
"Sugerencias"
	Modulo de mensajeria.


Dentro del panel "Perfil"
"Pedidos realizados"
	Hace un Crud de todos los formularios de solicitudes completados, correspondientes a ese usuario
	y de los ultimos 180 dias.

"Vale creditel y Vale correo"
	Gestiona el estado de compra de determinados clientes.
	Los cuales por defecto estan habilitados segun una importacion del archivo correspondiente en el modelo
	Luego de realizada la compra, se cargan los datos del cliente X, y este se deshabilita del listado
	guardando en el modelo los datos correspondientes a la compra.



vista inicio desde usuario "Admin"
De momento creados se encuentran 2 modulos centrales.
"Cajas" - Donde se encuentran formularios de registro de informacion.

"Convenios" - Donde se encuentran formularios de actualizacion de informacion.
(desde el admin de django, se importa un archivo con datos, donde el usuario "local1" debera confirmar la 
informacion dentro de "Convenios"-"Cobranzas convenios"
una vez editado todos los campos solicitados, cambia el estado automatico, y ya no mostrara
el objeto dentro de la lista.

