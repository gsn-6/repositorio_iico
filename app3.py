import streamlit as st
import calculos
import presupuesto_pdf
productos = ["Alfajor", "Gaseosa", "Chicle", "Agua"]
precios = [1500, 2800, 500, 1800]
st.title("IICO Kiosco")
numero = st.number_input("Numero de presupuesto", min_value=1, step=1, value=1)
fecha = st.date_input("Fecha")
cliente = st.text_input("Ingrese el nombre del cliente:")
producto = st.selectbox("Elija el producto que desea comprar:", productos)
cantidad = st.number_input("Ingrese la cantidad:", min_value=1, step=1, value=1)
pago = st.radio("Seleccione la forma de pago:", [calculos.EFECTIVO, calculos.TRANSFERENCIA])
pos = calculos.buscar_posicion(productos, producto)
precio_unitario = precios[pos]
subtotal = precio_unitario * cantidad
monto_con_descuento = calculos.aplicar_descuento(subtotal, pago)
descuento_monto = round(subtotal - monto_con_descuento, 2)
iva = calculos.calcular_iva(monto_con_descuento)
total = round(monto_con_descuento + iva, 2)
st.write(f"Precio unitario: ${precio_unitario}")
st.write(f"Subtotal: ${subtotal}")
st.write(f"Descuento: ${descuento_monto}")
st.write(f"IVA 21%: ${iva}")
st.write(f"Total: ${total}")
archivo_pdf = presupuesto_pdf.armar_pdf(numero=numero, fecha=fecha, cliente=cliente, producto=producto, cantidad=cantidad, precio=precio_unitario, subtotal=subtotal, descuento=descuento_monto, iva=iva, total=total)
st.download_button(label="Descargar presupuesto (PDF)", data=archivo_pdf, file_name=f"presupuesto_{numero}.pdf", mime="application/pdf")