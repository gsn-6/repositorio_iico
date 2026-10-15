import streamlit as st
import calculos
productos = ["Alfajor", "Gaseosa", "Chicle", "Agua"]
precios = [1500, 2800, 500, 1800]
st.title("IICO Kiosco")
cliente = st.text_input("ingrese el nombre del cliente:")
producto = st.selectbox("elija el producto que desea comprar:", productos)
cantidad = st.number_input("ingrese la cantidad:", min_value=1, step=1, value=1)
pago = st.radio("seleccione la forma de pago:", [calculos.EFECTIVO, calculos.TRANSFERENCIA])
pos = calculos.buscar_posicion(productos, producto)
precio_unitario = precios[pos]
subtotal = precio_unitario * cantidad
monto_con_descuento = calculos.aplicar_descuento(subtotal, pago)
descuento_monto = round(subtotal - monto_con_descuento, 2)
iva = calculos.calcular_iva(monto_con_descuento)
total = round(monto_con_descuento + iva, 2)
st.write(f"precio unitario: ${precio_unitario}")
st.write(f"subtotal: ${subtotal}")
st.write(f"descuento: ${descuento_monto}")
st.write(f"IVA 21%: ${iva}")
st.write(f"total: ${total}")