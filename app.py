import streamlit as st
PRECIO_ALFAJOR = 1500
PRECIO_GASEOSA = 2800
def calcular_total(cantidad, precio):
    subtotal = cantidad * precio
    return subtotal
st.title("IICO Kiosco")
cliente = st.text_input("Ingrese el nombre del cliente:")
if cliente.strip() != "":
    st.write(f"Pedido de {cliente}")
cantidad = st.number_input(
    "Ingrese la cantidad de alfajores:", min_value=0, step=1
)
st.write(f"los alfajores valen ${PRECIO_ALFAJOR}")
cantidad_gaseosas = st.number_input(
    "Ingrese la cantidad de gaseosas:", min_value=0, step=1
)
st.write(f"las gaseosas valen ${PRECIO_GASEOSA}")
grupos_de_3 = cantidad // 3
sueltos = cantidad % 3
alfajores_a_pagar = (grupos_de_3 * 2) + sueltos
subtotal_gaseosas = calcular_total(cantidad_gaseosas, PRECIO_GASEOSA)
st.write(f"Total de gaseosas a pagar: ${subtotal_gaseosas}")
subtotal_alfajores = calcular_total(alfajores_a_pagar, PRECIO_ALFAJOR)
st.write(f"Total de alfajores a pagar: ${subtotal_alfajores}")
ahorro = (cantidad - alfajores_a_pagar) * PRECIO_ALFAJOR
st.write(f"Ahorro por promo 3x2: ${ahorro}")
st.write(f"Total a pagar: ${subtotal_alfajores + subtotal_gaseosas}")
if cliente.strip() != "":
    st.write(f" Gracias {cliente} por su compra")