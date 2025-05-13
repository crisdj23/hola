import tkinter as tk
from view.producto_view import ProductoView
from view.cliente_view import ClienteView
from view.venta_view import VentaView
from view.ventas_view import VentasView

def main():
    root = tk.Tk()
    root.title("Sistema de Ventas")
    root.geometry("400x300")

    tk.Button(root, text="Registrar Producto", command=lambda: ProductoView(root)).pack(pady=10)
    tk.Button(root, text="Registrar Cliente", command=lambda: ClienteView(root)).pack(pady=10)
    tk.Button(root, text="Registrar Venta", command=lambda: VentaView(root)).pack(pady=10)
    tk.Button(root, text="Ver Ventas", command=lambda: VentasView(root)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()